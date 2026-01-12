## O que são Regex Paths?

São **caminhos que usam expressões regulares** para definir padrões de URLs, em vez de caminhos fixos.

Eles permitem:

* Capturar partes da URL
* Validar formatos (números, letras, datas, etc.)
* Criar rotas mais flexíveis

---

## Exemplo simples de Regex

```regex
^posts/\d+/$
```

Significa:

* `^` → início da URL
* `posts/` → texto fixo
* `\d+` → um ou mais números
* `/` → barra final
* `$` → fim da URL

URLs válidas:

* `posts/1/`
* `posts/42/`

Inválidas:

* `posts/abc/`
* `posts/1/extra/`

---

## Regex Paths no Django (re_path)

No Django, você usa `re_path`:

```python
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^posts/(?P<id>\d+)/$', views.post_detail),
]
```

### O que está acontecendo:

* `(?P<id>\d+)` → captura um número
* Esse valor chega na view como argumento `id`

```python
def post_detail(request, id):
    return HttpResponse(f"Post {id}")
```

---

## Comparação: `path` vs `re_path`

### path (mais simples, recomendado hoje)

```python
path('posts/<int:id>/', views.post_detail)
```

### re_path (regex puro)

```python
re_path(r'^posts/(?P<id>\d+)/$', views.post_detail)
```

👉 **Hoje em dia, use `path` sempre que puder**
👉 `re_path` só quando precisar de regras muito específicas

---

## Regex úteis para URLs

| Regex       | Significado                |
| ----------- | -------------------------- |
| `\d+`       | números                    |
| `[a-zA-Z]+` | letras                     |
| `[\w-]+`    | letras, números, `_` e `-` |
| `.*`        | qualquer coisa             |
| `{3,10}`    | tamanho mínimo e máximo    |

Exemplo:

```regex
^user/[a-zA-Z0-9_-]{3,16}/$
```

---

## Quando usar Regex Paths?

Use quando precisar:

* Validar formatos complexos
* Capturar padrões fora do comum
* Migrar código Django antigo

