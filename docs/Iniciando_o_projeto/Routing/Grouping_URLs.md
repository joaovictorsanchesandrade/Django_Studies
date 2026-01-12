## 🎯 O que é Grouping URLs?

É o ato de **separar e agrupar URLs por responsabilidade** (app, domínio ou funcionalidade), ao invés de definir todas as rotas no `urls.py` principal do projeto.

👉 Cada **app** cuida de suas próprias URLs.

---

## 📁 Estrutura típica com Grouping

```text
meuprojeto/
│
├── meuprojeto/
│   └── urls.py        # URLs globais
│
├── blog/
│   ├── urls.py        # URLs do app blog
│   └── views.py
│
├── accounts/
│   ├── urls.py        # URLs do app accounts
│   └── views.py
```

---

## 🧠 URLs sem agrupamento (má prática)

```python
# meuprojeto/urls.py
from blog import views as blog_views
from accounts import views as acc_views

urlpatterns = [
    path('blog/', blog_views.index),
    path('blog/post/<int:id>/', blog_views.post),
    path('login/', acc_views.login),
    path('logout/', acc_views.logout),
]
```

❌ Problemas:

* Arquivo cresce rápido
* Difícil manutenção
* Forte acoplamento entre apps

---

## ✅ Grouping URLs com `include()`

### urls.py do projeto

```python
# meuprojeto/urls.py
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]
```

---

### urls.py do app (blog)

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post/<int:id>/', views.post, name='blog-post'),
]
```

📌 Agora:

* `blog/` → `index`
* `blog/post/1/` → `post`

---

## 🏷️ Grouping com namespaces (muito importante)

Evita conflito de nomes entre URLs de apps diferentes.

### blog/urls.py

```python
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post, name='post'),
]
```

### Uso no projeto

```python
path('blog/', include('blog.urls')),
```

### Uso em templates

```html
<a href="{% url 'blog:post' id=1 %}">Ver post</a>
```

---

## 🔗 include com lista de URLs (menos comum)

```python
from django.urls import path, include
from blog import views

blog_patterns = [
    path('', views.index),
    path('post/<int:id>/', views.post),
]

urlpatterns = [
    path('blog/', include(blog_patterns)),
]
```

👉 Útil para projetos pequenos ou URLs muito simples.

---

## 🧩 Grouping por versão de API (caso comum)

```python
urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('api/v2/', include('api.v2.urls')),
]
```

Excelente para **versionamento de APIs REST**.

---

## 📌 Boas práticas

✅ Um `urls.py` por app
✅ Usar `app_name` sempre
✅ URLs legíveis e semânticas
✅ Evitar lógica nas URLs
✅ Manter consistência nos nomes

---

## 🔍 Quando o Grouping se torna essencial?

* Projetos médios ou grandes
* APIs REST
* Sistemas modulares
* Times com múltiplos devs

---

## 🧠 Resumo rápido

| Conceito          | Função                      |
| ----------------- | --------------------------- |
| `include()`       | Inclui URLs de outro módulo |
| `app_name`        | Cria namespace              |
| `urls.py` por app | Organização                 |
| Grouping          | Separação por domínio       |

