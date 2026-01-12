Os **Routers** no Django REST Framework (DRF) são responsáveis por **mapear automaticamente URLs para ViewSets**, reduzindo código repetitivo e garantindo um padrão consistente para APIs REST.

Eles são especialmente úteis em APIs baseadas em **resources**, onde cada endpoint segue operações CRUD bem definidas.

---

## O Que é um Router?

Um **Router**:

* gera automaticamente as URLs
* conecta **ViewSets** aos endpoints
* segue convenções REST
* reduz boilerplate

Sem router, cada rota precisa ser definida manualmente.

---

## Por Que Usar Routers?

✔️ Menos código
✔️ URLs padronizadas
✔️ Manutenção simples
✔️ Integração natural com ViewSets
✔️ APIs mais consistentes

---

## Router vs URLs Manuais

### Sem Router

```python
urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]
```

### Com Router

```python
router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
```

---

## Tipos de Routers no DRF

### `SimpleRouter`

* Gera rotas básicas
* Não inclui endpoint raiz

```python
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'posts', PostViewSet)
```

---

### `DefaultRouter` (Mais Usado)

* Inclui endpoint raiz (`/`)
* Exibe APIs disponíveis

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)
```

---

## Rotas Geradas Automaticamente

Ao registrar um ViewSet:

```python
router.register(r'posts', PostViewSet)
```

São criadas:

| Método | URL          | Ação           |
| ------ | ------------ | -------------- |
| GET    | /posts/      | list           |
| POST   | /posts/      | create         |
| GET    | /posts/{id}/ | retrieve       |
| PUT    | /posts/{id}/ | update         |
| PATCH  | /posts/{id}/ | partial_update |
| DELETE | /posts/{id}/ | destroy        |

---

## Usando Routers com ViewSets

```python
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

📌 Routers funcionam apenas com **ViewSets**.

---

## Custom Actions com Routers

### `@action`

```python
from rest_framework.decorators import action

class PostViewSet(ModelViewSet):

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        return Response({'status': 'published'})
```

Cria:

```text
POST /posts/{id}/publish/
```

---

### Action de Lista

```python
@action(detail=False, methods=['get'])
def recent(self, request):
    ...
```

Cria:

```text
GET /posts/recent/
```

---

## Nomeando Rotas

```python
router.register(
    r'posts',
    PostViewSet,
    basename='post'
)
```

📌 `basename` é obrigatório quando não há `queryset`.

---

## Versionamento com Routers

```python
router.register(r'v1/posts', PostViewSet)
```

Ou melhor:

```text
/api/v1/posts/
```

Com `include()`:

```python
path('api/v1/', include(router.urls))
```

---

## Routers e Namespaces

```python
app_name = 'api'

urlpatterns = [
    path('', include((router.urls, app_name)))
]
```

---

## Custom Router

Exemplo simples:

```python
from rest_framework.routers import SimpleRouter

class CustomRouter(SimpleRouter):
    pass
```

📌 Útil para projetos grandes.

---

## Boas Práticas

* Use `DefaultRouter` como padrão
* Use `ViewSets` sempre que possível
* Padronize nomes de endpoints
* Evite lógica de negócio nos ViewSets
* Versione sua API
* Documente endpoints

---

## Erros Comuns

* Misturar routers e URLs manuais sem padrão
* Não definir `basename`
* Criar ViewSets muito genéricos
* Não versionar endpoints
* Expor endpoints desnecessários

---

## Routers em Projetos Reais

Em produção, routers facilitam:

* crescimento da API
* consistência entre endpoints
* integração com Swagger / OpenAPI
* manutenção do código

---

## Quando NÃO Usar Routers?

❌ Endpoints muito customizados
❌ APIs sem padrão REST
❌ Casos onde cada rota é única

Nestes casos, URLs manuais podem ser melhores.

---

## Conclusão

Os **Routers** são uma das principais vantagens do DRF, permitindo criar APIs REST **limpas, padronizadas e escaláveis** com mínimo esforço.

Dominar routers é essencial para qualquer backend Django moderno.

