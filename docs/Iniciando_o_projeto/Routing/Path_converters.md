# 📌 O que são *Path Converters*?

**Path converters** definem **como um trecho da URL será interpretado pelo Django**.
Eles permitem especificar o **tipo de dado esperado** em cada parte da rota, como por exemplo:

* Um número inteiro
* Um texto
* Um UUID
* Um *slug* amigável
* Ou até um formato **personalizado**

Eles são utilizados dentro da função `path()` no arquivo `urls.py`.

---

## 🧩 Sintaxe básica

```python
path("<converter:nome>", view)
```

### Exemplo

```python
path("post/<int:id>/", views.post_detail)
```

Se o usuário acessar:

```
/post/14/
```

A *view* receberá:

```python
def post_detail(request, id: int):
    # id já chega como inteiro
```

---

## 🔹 Converters padrão do Django

O Django fornece alguns *path converters* prontos para uso.

---

### 1️⃣ `str`

* **Converter padrão**
* Captura qualquer string **exceto `/`**

```python
path("user/<str:username>/", views.profile)
```

Exemplo:

```
/user/joaovictorsanches/
```

---

### 2️⃣ `int`

* Aceita apenas **números inteiros positivos**

```python
path("produtos/<int:id>/", views.produto)
```

---

### 3️⃣ `slug`

* Aceita letras, números, hífens (`-`) e underscores (`_`)
* Muito usado para URLs amigáveis (*SEO-friendly*)

```python
path("blog/<slug:slug>/", views.post)
```

Exemplo:

```
/blog/como-aprender-django/
```

---

### 4️⃣ `uuid`

* Aceita apenas UUIDs válidos

```python
path("pedido/<uuid:pedido_id>/", views.pedido)
```

---

### 5️⃣ `path`

* Captura **toda a URL**, incluindo `/`
* Muito útil para arquivos e caminhos aninhados

```python
path("media/<path:caminho>/", views.media)
```

Exemplo:

```
/media/imagens/fotos/2026/img.png
```

---

## 🔒 Vantagens dos *Path Converters*

✔️ Validação automática da URL
✔️ Conversão automática para tipos Python
✔️ URLs mais legíveis e profissionais
✔️ Menos código de validação nas *views*
✔️ Redução de erros de roteamento

---

## 🛠 Criando um *Path Converter* personalizado

Você pode criar seus próprios converters quando os padrões não forem suficientes.

---

### 1️⃣ Criar o converter

```python
class AnoConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
```

---

### 2️⃣ Registrar o converter

```python
# urls.py
from django.urls import register_converter
from .converters import AnoConverter

register_converter(AnoConverter, "ano")
```

---

### 3️⃣ Usar na URL

```python
path("arquivo/<ano:ano>/", views.arquivo_por_ano)
```

---

## 🧠 Como funciona por baixo dos panos?

1. O Django compara a URL com os padrões definidos
2. Aplica a *regex* do converter
3. Se houver correspondência, executa `to_python()`
4. Envia o valor convertido para a *view*
5. Ao gerar URLs (`reverse()`), utiliza `to_url()`

---

## 📎 Exemplo completo

```python
# urls.py
path("cliente/<int:id>/", views.cliente_detail)
```

```python
# views.py
from django.http import HttpResponse

def cliente_detail(request, id: int):
    return HttpResponse(f"Cliente número: {id}")
```

---

## 📚 Quando usar *Path Converters*?

* Rotas baseadas em **ID**
* URLs amigáveis com **slug**
* Controle rigoroso do formato da URL
* APIs REST
* Para evitar validações manuais nas *views*

---

## 🚀 Conclusão

**Path converters** são essenciais para criar URLs profissionais em Django, tornando o código:

* Mais limpo
* Mais seguro
* Mais legível
* Mais fácil de manter

👉 Dominar *path converters* é um passo importante para escrever **projetos Django bem estruturados e escaláveis**.
