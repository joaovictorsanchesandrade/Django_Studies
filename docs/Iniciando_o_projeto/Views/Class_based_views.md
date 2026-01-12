## 1. O que é uma Class-Based View (sem abstrações)

Uma **Class-Based View** é uma **classe Python que controla o ciclo completo de uma requisição HTTP**, organizada por **métodos**, em vez de uma função única.

Ela existe para resolver **problemas estruturais**, não apenas para “economizar código”.

A ideia central é:

> **Cada verbo HTTP vira um método da classe.**

---

## 2. Comparação direta com FBV (nível estrutural)

### Function-Based View

* Uma função
* Controle manual de tudo
* Fluxo linear
* Cresce mal quando a lógica aumenta

### Class-Based View

* Uma classe
* Separação clara por responsabilidade
* Métodos bem definidos
* Escala melhor com complexidade

CBV **não substitui** FBV — ela resolve **outro tipo de problema**.

---

## 3. A classe base `View`

Toda CBV começa aqui:

```python
from django.views import View
```

Essa classe fornece:

* O método `as_view()`
* O método `dispatch()`
* A estrutura do ciclo HTTP

Ela **não faz nada sozinha**, apenas define o contrato.

---

## 4. Ciclo real de execução de uma CBV

Este é o ponto mais importante.

### Fluxo completo:

1. URL chama `MinhaView.as_view()`
2. `as_view()` cria uma instância da classe
3. A instância recebe o `request`
4. O Django chama `dispatch()`
5. `dispatch()` escolhe o método HTTP correto
6. O método retorna um `HttpResponse`

Visualmente:

```
URL
 ↓
as_view()
 ↓
instância da classe
 ↓
dispatch()
 ↓
get() | post() | put() | delete()
 ↓
HttpResponse
```

---

## 5. CBV mínima funcional

```python
from django.http import HttpResponse
from django.views import View

class MinhaView(View):
    def get(self, request):
        return HttpResponse("GET funcionando")

    def post(self, request):
        return HttpResponse("POST funcionando")
```

URLs:

```python
path('', MinhaView.as_view())
```

Aqui você já tem:

* Controle explícito de métodos HTTP
* Código organizado
* Estrutura extensível

---

## 6. O método `dispatch()`

`dispatch()` é o **coração da CBV**.

Ele:

* Recebe a requisição
* Verifica o verbo HTTP
* Chama o método correspondente

Você **raramente sobrescreve** `dispatch()`, mas quando sobrescreve, faz isso conscientemente.

Exemplo de controle global:

```python
def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return HttpResponse("Acesso negado", status=403)
    return super().dispatch(request, *args, **kwargs)
```

Isso afeta **todos os métodos HTTP** da view.

---

## 7. Organização por responsabilidade (vantagem real)

Em CBV, cada método tem um papel claro:

* `get()` → exibir dados
* `post()` → processar envio
* `put()` → atualizar
* `delete()` → remover

Isso evita:

* `if request.method == ...`
* Funções longas
* Lógica misturada

---

## 8. Estado interno da classe

Uma CBV **tem estado**, diferente de uma FBV.

Você pode usar `self` para compartilhar dados:

```python
class ExampleView(View):
    def setup(self, request, *args, **kwargs):
        self.user = request.user
        super().setup(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(self.user.username)
```

Esse estado vale **apenas para a requisição atual**.

---

## 9. Quando usar CBV (sem genéricas)

Use CBV quando:

* A view responde a múltiplos métodos HTTP
* Há validações comuns entre métodos
* Existe lógica compartilhada
* A view tende a crescer

Evite CBV quando:

* A lógica é trivial
* Um único GET simples resolve
* Clareza é mais importante que estrutura

---

## 10. Erros comuns ao aprender CBV

* Usar CBV sem entender `dispatch`
* Criar classes para views simples
* Misturar lógica de GET e POST
* Copiar código sem saber o papel dos métodos
* Achar que CBV é “mais avançada” por si só

---

## 11. Regra prática de desenvolvedor experiente

> **CBV não é sobre menos código.
> É sobre código melhor organizado.**
