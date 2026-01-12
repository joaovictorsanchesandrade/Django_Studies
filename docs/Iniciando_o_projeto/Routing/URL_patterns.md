# URL Patterns no Django

No Django, **URL patterns** definem como as URLs da sua aplicação são mapeadas para **views** — funções ou classes responsáveis por responder às requisições HTTP.

---

## Estrutura básica

Tudo começa no arquivo `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]
```

**Explicação dos elementos:**

* `path()` → define uma rota
* `''` → URL vazia (página inicial)
* `views.home` → view que será executada
* `name="home"` → nome da rota (usado em templates e redirects)

---

## URLs com parâmetros

Você pode capturar valores diretamente da URL:

```python
path("post/<int:id>/", views.post_detail, name="post_detail")
```

Na view:

```python
def post_detail(request, id: int):
    return HttpResponse(f"Post: {id}")
```

**Tipos de parâmetros mais comuns:**

* `<int:>` → números inteiros
* `<str:>` → strings
* `<slug:>` → texto amigável para URLs
* `<uuid:>` → identificadores únicos

---

## Separando URLs entre apps com `include()`

Separar URLs por app é o **padrão profissional** em projetos Django.

### `urls.py` do projeto

```python
from django.urls import path, include

urlpatterns = [
    path("blog/", include("blog.urls")),
]
```

### `urls.py` do app

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_blog"),
    path("post/<int:id>/", views.post_detail, name="post_blog"),
]
```

---

## URLs com Class-Based Views (CBVs)

```python
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home_blog"),
]
```

---

## Reverse e uso em templates

### Template HTML

```html
<a href="{% url 'post_detail' id=15 %}">Ver post</a>
```

### Python

```python
from django.urls import reverse

reverse("post_detail", args=[5])
```

---

## Boas práticas

* Sempre utilize `name` nas URLs
* Separe as URLs por app
* Evite URLs longas ou confusas
* Use `slug` para melhorar SEO e legibilidade

---

# Slug — explicação adicional

## Exemplo

**Título do post:**

```
Como aprender Django do zero
```

**Slug gerado:**

```
como-aprender-django-do-zero
```

**URL final:**

```
meusite.com/post/como-aprender-django-do-zero/
```

---

## Por que usar slug?

* ✅ URLs mais bonitas
* ✅ Melhor SEO (motores de busca entendem melhor)
* ✅ Fácil de ler e compartilhar
* ✅ Evita IDs visíveis (`/post/12/`)

---

## Slug no Django (Model)

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
```

---

## Usando slug nas URLs

```python
path("post/<slug:slug>/", views.post_detail, name="post_detail")
```

View:

```python
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
```

---

## Gerando slug automaticamente

```python
from django.utils.text import slugify

def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)
```

---

## Regras de um slug

* Letras minúsculas
* Sem acentos
* Espaços viram `-`
* Apenas letras, números e hífen

---

## Quando usar ID ou slug?

* **ID** → simples, interno e rápido
* **Slug** → público, ideal para SEO, blogs e artigos
