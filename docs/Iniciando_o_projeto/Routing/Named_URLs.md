Named URLs no Django servem para dar um nome a uma rota, permitindo referenciá-la sem depender do caminho literal. Isso deixa o projeto mais organizado, seguro e fácil de manter.

--- 

## 1️⃣ Definindo uma URL com nome

No `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('perfil/<int:id>/', views.perfil, name='perfil'),
]
```

➡️ O parâmetro `name` é o **nome da URL**.

---

## 2️⃣ Usando Named URLs no template

Em vez de escrever o caminho fixo:

```html
<a href="/login/">Login</a>
```

Use:

```html
<a href="{% url 'login' %}">Login</a>
```

Com parâmetros:

```html
<a href="{% url 'perfil' user.id %}">Perfil</a>
```

---

## 3️⃣ Usando Named URLs nas views (Python)

Para redirecionar:

```python
from django.shortcuts import redirect

def minha_view(request):
    return redirect('login')
```

Com argumentos:

```python
return redirect('perfil', id=10)
```

---

## 4️⃣ Usando `reverse()`

Útil fora de views/templates:

```python
from django.urls import reverse

url = reverse('perfil', kwargs={'id': 5})
```

---

## 5️⃣ Namespaces (muito importante)

Quando o projeto cresce:

```python
# app/urls.py
app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
]
```

Uso:

```html
{% url 'usuarios:login' %}
```

Ou:

```python
redirect('usuarios:login')
```

---

## ✅ Vantagens dos Named URLs

* Evita links quebrados
* Facilita refatoração
* Código mais limpo
* Essencial em projetos médios/grandes

