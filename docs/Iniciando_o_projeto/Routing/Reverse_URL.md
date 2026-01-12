**Reverse URL** no Django é o processo de **gerar uma URL a partir do nome da rota**, em vez de escrever o caminho “na mão”.
Isso deixa o código mais organizado, seguro e fácil de manter.

---

## 1️⃣ Por que usar Reverse URL?

* Evita URLs hardcoded (`/users/1/`)
* Se a URL mudar, o código continua funcionando
* É a forma **correta e profissional** de trabalhar no Django

---

## 2️⃣ Definindo uma URL nomeada

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('perfil/<int:id>/', views.perfil, name='perfil'),
]
```

👉 Aqui o nome da rota é **`perfil`**

---

## 3️⃣ Usando `reverse()` no Python

```python
from django.urls import reverse

url = reverse('perfil', args=[5])
# Resultado: /perfil/5/
```

Também pode usar `kwargs`:

```python
reverse('perfil', kwargs={'id': 5})
```

---

## 4️⃣ `reverse_lazy` (muito usado em CBVs)

```python
from django.urls import reverse_lazy

success_url = reverse_lazy('perfil')
```

✔️ Use quando a URL só deve ser resolvida **depois** (ex: `CreateView`, `DeleteView`).

---

## 5️⃣ Reverse URL no template (mais comum)

```html
<a href="{% url 'perfil' 5 %}">Ver perfil</a>
```

Com variável:

```html
<a href="{% url 'perfil' user.id %}">Ver perfil</a>
```

---

## 6️⃣ URLs com namespace

```python
# app urls.py
app_name = 'usuarios'

urlpatterns = [
    path('perfil/<int:id>/', views.perfil, name='perfil'),
]
```

Uso:

```python
reverse('usuarios:perfil', args=[5])
```

Template:

```html
{% url 'usuarios:perfil' user.id %}
```

---

## 🧠 Resumo mental

* **name** → identidade da URL
* **reverse / {% url %}** → gera o caminho
* **Nunca escreva URLs fixas**
* Namespace evita conflitos entre apps
