As **Function-Based Views** são funções Python que recebem uma requisição HTTP e retornam uma resposta. São diretas, fáceis de entender e ótimas para ter controle total da lógica.

---

## Estrutura básica

```python
from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Resposta da view")
```

* `request` → objeto com dados da requisição
* retorno → sempre uma `HttpResponse`

---

## Renderizando templates

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

---

## Passando contexto para o template

```python
def dashboard(request):
    context = {
        "usuario": "João",
        "online": True
    }
    return render(request, "dashboard.html", context)
```

No HTML:

```html
{{ usuario }}
{% if online %} Online {% endif %}
```

---

## Tratando métodos HTTP (GET / POST)

```python
def contato(request):
    if request.method == "POST":
        email = request.POST.get("email")
        return HttpResponse("Formulário enviado")

    return render(request, "contato.html")
```

---

## Recebendo parâmetros da URL

**urls.py**

```python
path("produto/<int:id>/", views.produto)
```

**views.py**

```python
def produto(request, id):
    return HttpResponse(f"Produto {id}")
```

---

## Trabalhando com Models

```python
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})
```

---

## Redirecionamento

```python
from django.shortcuts import redirect

def login(request):
    if request.method == "POST":
        return redirect("home")
```

---

## Retornando JSON (API simples)

```python
from django.http import JsonResponse

def api_status(request):
    return JsonResponse({"status": "ok"})
```

---

## Quando usar FBV?

✔️ Views simples
✔️ Lógica personalizada
✔️ Aprendizado e controle total
✔️ Menos abstração

❌ Pode ficar repetitivo em CRUDs grandes

---

## Boas práticas

* Uma view = uma responsabilidade
* Evite lógica pesada (use services/helpers)
* Use `get_object_or_404`
* Nomeie bem as views

```python
from django.shortcuts import get_object_or_404
```

