No Django, os **Fields** (campos) definem **como os dados serão armazenados no banco de dados** e **como serão representados em Python**.
Cada campo de um `Model` é uma instância de uma classe que herda de `django.db.models.Field`.

Exemplo básico:

```python
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
```

Neste exemplo:

* `CharField` → campo de texto
* `IntegerField` → campo numérico inteiro

---

## Principais Tipos de Campos

### 1. Campos de Texto

#### `CharField`

* Usado para **textos curtos**
* **Obrigatório** definir `max_length`

```python
models.CharField(max_length=255)
```

Uso comum:

* nomes
* títulos
* emails
* usernames

---

#### `TextField`

* Usado para **textos longos**
* Não exige `max_length`

```python
models.TextField()
```

Uso comum:

* descrições
* comentários
* artigos

---

### 2. Campos Numéricos

#### `IntegerField`

* Números inteiros

```python
models.IntegerField()
```

---

#### `BigIntegerField`

* Inteiros muito grandes

```python
models.BigIntegerField()
```

---

#### `FloatField`

* Números decimais (ponto flutuante)

```python
models.FloatField()
```

⚠️ **Não recomendado para valores financeiros**

---

#### `DecimalField`

* Números decimais com precisão fixa
* Ideal para **valores monetários**

```python
models.DecimalField(max_digits=10, decimal_places=2)
```

---

### 3. Campos Booleanos

#### `BooleanField`

* Valores `True` ou `False`

```python
models.BooleanField(default=False)
```

---

### 4. Campos de Data e Hora

#### `DateField`

* Armazena apenas a data

```python
models.DateField()
```

---

#### `TimeField`

* Armazena apenas o horário

```python
models.TimeField()
```

---

#### `DateTimeField`

* Armazena data e hora

```python
models.DateTimeField(auto_now_add=True)
```

Parâmetros comuns:

* `auto_now=True` → atualiza sempre que salvar
* `auto_now_add=True` → define apenas na criação

---

### 5. Campos Relacionados a Arquivos

#### `FileField`

* Upload de arquivos genéricos

```python
models.FileField(upload_to='uploads/')
```

---

#### `ImageField`

* Upload de imagens
* Requer a biblioteca **Pillow**

```python
models.ImageField(upload_to='imagens/')
```

---

### 6. Campos de Relacionamento

#### `ForeignKey`

* Relacionamento **muitos-para-um**

```python
models.ForeignKey(Autor, on_delete=models.CASCADE)
```

---

#### `OneToOneField`

* Relacionamento **um-para-um**

```python
models.OneToOneField(User, on_delete=models.CASCADE)
```

---

#### `ManyToManyField`

* Relacionamento **muitos-para-muitos**

```python
models.ManyToManyField(Tag)
```

---

### 7. Campos Especiais

#### `EmailField`

* Valida emails automaticamente

```python
models.EmailField()
```

---

#### `URLField`

* Armazena URLs

```python
models.URLField()
```

---

#### `UUIDField`

* Identificador único universal (UUID)

```python
import uuid

models.UUIDField(default=uuid.uuid4, editable=False)
```

---

#### `JSONField`

* Armazena dados em formato JSON (bancos modernos)

```python
models.JSONField()
```

---

### 8. Campos Automáticos

#### `AutoField`

* Campo inteiro autoincrementado
* Usado por padrão como `id`

```python
models.AutoField(primary_key=True)
```

---

#### `BigAutoField`

* Versão com suporte a números maiores

```python
models.BigAutoField(primary_key=True)
```

---

## Boas Práticas

* Use `CharField` sempre que souber o tamanho máximo do texto
* Prefira `DecimalField` para dinheiro
* Use relacionamentos ao invés de armazenar IDs manualmente
* Nomeie campos de forma clara e sem ambiguidade

---

## Conclusão

Os **Field Types** são a base dos Models no Django.
Escolher corretamente o tipo de campo:

* melhora a integridade dos dados
* facilita validações
* otimiza o banco de dados
