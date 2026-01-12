As **Function-Based Views** são funções Python que recebem uma requisição HTTP e retornam uma resposta. São diretas, fáceis de entender e Abaixo está um **guia completo e aprofundado sobre Function-Based Views (FBV) no Django**, cobrindo **tudo o que é relevante na prática e em nível profissional**.

---

## 1. O que é uma Function-Based View

Uma **Function-Based View** é uma função Python que:

* Recebe um objeto `HttpRequest`
* Executa uma lógica
* Retorna um objeto `HttpResponse`

Assinatura padrão:

```python
def view_name(request, *args, **kwargs):
    return HttpResponse(...)
```

---

## 2. Ciclo de vida da requisição (request lifecycle)

```
Cliente → URLconf → Middleware → View (FBV) → Template → Response → Middleware → Cliente
```

A FBV é chamada **depois** dos middlewares de entrada e **antes** dos de saída.

---

## 3. Objeto `HttpRequest`

Principais atributos:

### Dados gerais

```python
request.method        # GET, POST, PUT, DELETE
request.path          # /produtos/1/
request.scheme        # http / https
request.user          # usuário autenticado
request.session       # sessão atual
request.COOKIES       # cookies
request.META          # headers e info do servidor
```

### Query params (GET)

```python
request.GET.get("search")
```

### Dados de formulário (POST)

```python
request.POST.get("email")
```

### Upload de arquivos

```python
request.FILES["arquivo"]
```

---

## 4. Tipos de resposta (HttpResponse)

### Texto simples

```python
HttpResponse("Olá")
```

### HTML

```python
HttpResponse("<h1>Olá</h1>")
```

### JSON

```python
JsonResponse({"status": "ok"})
```

### Redirecionamento

```python
redirect("home")
redirect("/login/")
```

### Resposta customizada

```python
HttpResponse(status=204)
```

---

## 5. Renderização de templates

```python
render(
    request,
    "template.html",
    context,
    status=200
)
```

O Django automaticamente:

* carrega o template
* injeta o contexto
* retorna `HttpResponse`

---

## 6. Contexto e Template Context Processors

Além do contexto manual:

```python
{"produtos": produtos}
```

O Django injeta automaticamente:

* `request`
* `user`
* `messages`
* `csrf_token`

---

## 7. Tratamento de métodos HTTP

Forma manual:

```python
def minha_view(request):
    if request.method == "GET":
        ...
    elif request.method == "POST":
        ...
```

Forma recomendada:

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def view(request):
    ...
```

Outros decorators:

```python
@require_GET
@require_POST
@require_safe
```

---

## 8. Decorators essenciais em FBV

### Autenticação

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...
```

### Permissões

```python
from django.contrib.auth.decorators import permission_required

@permission_required("app.add_produto")
def criar_produto(request):
    ...
```

### Cache

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def home(request):
    ...
```

### CSRF

```python
@csrf_exempt        # evitar (só para APIs)
@csrf_protect
```

---

## 9. Parâmetros de URL

```python
path("post/<slug:slug>/", views.post)
```

```python
def post(request, slug):
    ...
```

---

## 10. Uso com Models

### Query básica

```python
Produto.objects.all()
Produto.objects.filter(preco__gt=100)
Produto.objects.get(id=1)
```

### get_object_or_404

```python
obj = get_object_or_404(Produto, id=id)
```

---

## 11. CRUD completo com FBV (exemplo)

### Create

```python
def criar(request):
    if request.method == "POST":
        Produto.objects.create(nome=request.POST["nome"])
        return redirect("lista")
    return render(request, "criar.html")
```

### Read

```python
def lista(request):
    produtos = Produto.objects.all()
    return render(request, "lista.html", {"produtos": produtos})
```

### Update

```python
def editar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.nome = request.POST["nome"]
        produto.save()
        return redirect("lista")
```

### Delete

```python
def deletar(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("lista")
```

---

## 12. Forms com FBV

### Forms do Django

```python
from .forms import ProdutoForm

def criar(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista")
```

---

## 13. Validações manuais

```python
if not nome:
    return render(request, "form.html", {"erro": "Campo obrigatório"})
```

---

## 14. Mensagens (django messages)

```python
from django.contrib import messages

messages.success(request, "Salvo com sucesso")
messages.error(request, "Erro ao salvar")
```

---

## 15. Paginação

```python
from django.core.paginator import Paginator

paginator = Paginator(produtos, 10)
page = paginator.get_page(request.GET.get("page"))
```

---

## 16. Upload de arquivos

```python
if request.method == "POST":
    arquivo = request.FILES["file"]
```

---

## 17. Headers e status HTTP

```python
response = HttpResponse()
response["X-App"] = "Django"
response.status_code = 201
```

---

## 18. Erros e exceções

```python
from django.http import Http404

raise Http404("Não encontrado")
```

---

## 19. Logging dentro da FBV

```python
import logging
logger = logging.getLogger(__name__)

logger.info("View acessada")
```

---

## 20. Organização profissional de FBVs

Boas práticas:

* separar lógica em `services.py`
* evitar views grandes
* uma view = uma ação
* usar helpers
* usar forms

Estrutura:

```
views/
 ├── __init__.py
 ├── auth.py
 ├── produto.py
 └── api.py
```

---

## 22. Quando usar FBV em projetos reais

✔ APIs simples
✔ Fluxos customizados
✔ Controle de permissões
✔ Projetos pequenos e médios
✔ Quando clareza é prioridade

---

## 23. Erros comuns

* Lógica pesada na view
* Não tratar métodos HTTP
* Não validar dados
* Não usar `get_object_or_404`
* Misturar responsabilidades

---

## 24. Checklist profissional FBV

✔ Tratamento de método
✔ Validação
✔ Segurança
✔ Status HTTP correto
✔ Organização
✔ Testes

---

## 25. Testes para FBV

```python
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
```

