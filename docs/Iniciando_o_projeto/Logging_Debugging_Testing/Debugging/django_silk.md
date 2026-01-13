O **Django Silk** é uma ferramenta de **profiling e monitoramento de performance** para aplicações Django. Ele permite **analisar tempo de execução de views, queries SQL, cache e requisições HTTP**, ajudando a identificar **gargalos e otimizar a aplicação**.

---

## 1. Instalando Django Silk

Para instalar, use pip:

```bash
pip install django-silk
```

---

## 2. Configuração Básica

1. **Adicionar à lista de INSTALLED_APPS:**

```python
# settings.py
INSTALLED_APPS = [
    ...
    'silk',
]
```

2. **Adicionar middleware** logo após o `CommonMiddleware`:

```python
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
]
```

3. **Configurar URLs do Silk:**

```python
# projeto/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]

if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
```

> A interface do Silk ficará disponível em `/silk/` no navegador, mostrando métricas detalhadas.

---

## 3. Funcionalidades do Django Silk

| Recurso                 | Descrição                                                  |
| ----------------------- | ---------------------------------------------------------- |
| **Requisições HTTP**    | Mostra tempo total de cada requisição.                     |
| **SQL Queries**         | Lista todas as queries executadas, tempo e parâmetros.     |
| **Views**               | Tempo gasto em cada view.                                  |
| **Cache**               | Mostra hits/misses do cache.                               |
| **Profiling de código** | Permite adicionar profiling manual em funções ou métodos.  |
| **Filtros de pesquisa** | Permite filtrar requisições por tempo, método ou endpoint. |

---

## 4. Perfilando Queries SQL

A Silk permite analisar todas as queries executadas em uma view:

```python
from myapp.models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})
```

* No painel do Silk, você verá:

  * Quantas queries foram executadas.
  * Tempo total gasto.
  * Possibilidade de identificar **N+1 queries**.

---

## 5. Perfilando Funções com Decorators

Você pode medir o tempo de execução de funções específicas usando o decorator `@silk_profile`:

```python
from silk.profiling.profiler import silk_profile

@silk_profile(name='Processamento de Pedidos')
def processar_pedido(pedido):
    # lógica complexa
    total = pedido.quantidade * pedido.preco
    return total
```

* Cada execução será registrada no painel do Silk, mostrando tempo e métricas detalhadas.

---

## 6. Boas Práticas

1. **Use Silk apenas em desenvolvimento (`DEBUG = True`)** – não recomendado em produção.
2. **Combine com Django Debug Toolbar** para análise detalhada de queries.
3. **Perfis longos** podem gerar muitos dados, limpe regularmente usando o comando:

```bash
python manage.py silk_clear
```

4. **Monitore endpoints críticos** para otimizar performance.
5. **Use profiling manual apenas quando necessário**, para não gerar overhead excessivo.

---

## 7. Exemplo de Uso Completo

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'silk',
]

MIDDLEWARE = [
    ...,
    'silk.middleware.SilkyMiddleware',
]

# urls.py
from django.urls import path, include
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
```

* Execute o servidor Django (`python manage.py runserver`).
* Acesse `/silk/` no navegador.
* Navegue pelas requisições, veja queries SQL, tempo de views e profiling de funções.

---

## 8. Referências

* [Django Silk GitHub](https://github.com/jazzband/django-silk)
* [Documentação Django Silk](https://django-silk.readthedocs.io/en/latest/)
* [Profiling Django Applications](https://docs.djangoproject.com/en/stable/topics/performance/)

