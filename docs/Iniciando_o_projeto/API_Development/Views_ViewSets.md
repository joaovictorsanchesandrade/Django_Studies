No **Django REST Framework (DRF)**, as Views são responsáveis por processar requisições e retornar respostas, enquanto os **ViewSets** permitem agrupar operações CRUD em uma única classe, tornando a API mais organizada e padronizada.

Este documento aborda os conceitos, tipos, usos e boas práticas de **Views e ViewSets** em APIs REST.

---

## 1. Views no DRF

As Views no DRF podem ser:

* **APIView** (classe base)
* **GenericAPIView** (com mixins)
* **Function-based views (FBV)** (menos comum em projetos grandes)

---

### 1.1 APIView

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

📌 Permite total controle da requisição e da resposta.

---

### 1.2 GenericAPIView + Mixins

O DRF oferece mixins prontos para operações comuns:

```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

Mixins comuns:

* `CreateModelMixin`
* `ListModelMixin`
* `RetrieveModelMixin`
* `UpdateModelMixin`
* `DestroyModelMixin`

---

### 1.3 Function-based Views (FBV)

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        # listar posts
        pass
    elif request.method == 'POST':
        # criar post
        pass
```

📌 Útil para endpoints simples ou protótipos rápidos.

---

## 2. ViewSets

Um **ViewSet** agrupa várias ações (list, create, retrieve, update, delete) em uma única classe.
Ele é pensado para uso com **Routers**, gerando URLs automaticamente.

---

### 2.1 ModelViewSet (mais usado)

```python
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

Rotas criadas automaticamente:

| Método | URL          | Ação           |
| ------ | ------------ | -------------- |
| GET    | /posts/      | list           |
| POST   | /posts/      | create         |
| GET    | /posts/{id}/ | retrieve       |
| PUT    | /posts/{id}/ | update         |
| PATCH  | /posts/{id}/ | partial_update |
| DELETE | /posts/{id}/ | destroy        |

---

### 2.2 ReadOnlyModelViewSet

Para recursos somente leitura:

```python
from rest_framework.viewsets import ReadOnlyModelViewSet

class PostReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

---

### 2.3 Custom Actions

Você pode adicionar ações extras ao ViewSet usando `@action`:

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(ModelViewSet):

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.published = True
        post.save()
        return Response({'status': 'published'})
```

Cria endpoint:

```text
POST /posts/{id}/publish/
```

---

### 2.4 ViewSets vs Views

| Aspecto           | View   | ViewSet                    |
| ----------------- | ------ | -------------------------- |
| Código repetitivo | Mais   | Menos                      |
| URLs manuais      | Sim    | Não (com Router)           |
| Flexibilidade     | Máxima | Alta (mas limitada a CRUD) |
| Custom Actions    | Manual | `@action`                  |

---

## 3. Boas Práticas

* Use **ModelViewSet** sempre que possível
* Crie **Serializers separados** para leitura e escrita quando necessário
* Evite lógica de negócio complexa no ViewSet
* Use `permissions` para controle de acesso
* Versione endpoints quando necessário
* Documente endpoints (Swagger/OpenAPI)

---

## 4. Erros Comuns

* Colocar validação pesada no ViewSet
* Criar ViewSet sem Router
* Não tratar exceções corretamente
* Criar endpoints muito genéricos ou grandes demais
* Misturar várias responsabilidades em uma ViewSet

---

## 5. ViewSets em Projetos Reais

* CRUD completo de recursos
* APIs REST consistentes e padronizadas
* Integração natural com Routers
* Redução de boilerplate
* Fácil integração com Swagger / OpenAPI

---

## 6. Conclusão

As **Views e ViewSets** são fundamentais para criar APIs REST com Django.
Dominar a diferença entre Views, Generic Views e ViewSets permite construir **APIs limpas, padronizadas e escaláveis**.

