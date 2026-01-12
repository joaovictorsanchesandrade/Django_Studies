No Django, **middleware de roteamento** não é um conceito oficial com esse nome (como no Express), mas dá pra **interceptar e controlar rotas antes/depois da view** usando **Middleware** + **URL routing**.

Vou te explicar do jeito certo e prático 👇

---

## 🔁 Como o fluxo de uma request funciona no Django

1. Request chega
2. **Middlewares (request)**
3. URL resolver (`urls.py`)
4. View
5. **Middlewares (response)**
6. Response sai

Ou seja: **middleware roda antes e depois da rota**.

---

## 🧠 Para que usar middleware no roteamento?

Você usa middleware quando quer:

* Proteger rotas (auth, admin, API)
* Redirecionar URLs
* Bloquear paths específicos
* Fazer lógica global de acesso
* Criar “guards” de rota (igual frontend)

---

## 🛠️ Exemplo simples: bloquear rota pelo path

### `middleware.py`

```python
from django.shortcuts import redirect

class BlockAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin'):
            return redirect('/login')

        return self.get_response(request)
```

### Registrar o middleware

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ...
    'core.middleware.BlockAdminMiddleware',
]
```

➡️ Qualquer acesso a `/admin` é interceptado **antes da view**.

---

## 🔐 Middleware como “Route Guard” (auth)

```python
class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_paths = ['/dashboard', '/profile']

        if request.path in protected_paths and not request.user.is_authenticated:
            return redirect('/login')

        return self.get_response(request)
```

---

## 🧩 Middleware + URLs nomeadas (boa prática)

Em vez de usar strings fixas:

```python
from django.urls import reverse

if request.path == reverse('dashboard'):
    ...
```

Mais seguro e profissional.

---

## ⚠️ O que NÃO fazer em middleware

❌ Lógica pesada
❌ Acessar banco sem necessidade
❌ Substituir views
❌ Criar regras específicas demais (isso é da view)

Middleware é **global**, não específico.

---

## 🧪 Alternativa melhor em muitos casos

### Decorator (mais limpo para rotas específicas)

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...
```

👉 Use **middleware** quando a regra for **global**
👉 Use **decorators** quando for **pontual**

---

## 🧠 Resumo rápido

* Django **não tem routing middleware nativo**
* Middleware intercepta requests **antes das rotas**
* Dá pra criar guards, redirects e bloqueios
* Ideal para regras globais
* Combine com URLs nomeadas (`reverse`)

---
