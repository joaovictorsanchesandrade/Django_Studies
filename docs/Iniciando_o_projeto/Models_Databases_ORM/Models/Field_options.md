As **Field Options** definem **como um campo se comporta**, **como ele é validado**, **como aparece em formulários/admin** e **como interage com o banco de dados**.

Elas são passadas como **parâmetros** ao definir um campo em um `Model`.

Exemplo:

```python
class Usuario(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
```

---

## Opções Mais Comuns

### `null`

* Define se o campo aceita `NULL` no banco de dados

```python
null=True
```

✔️ Banco pode armazenar `NULL`
❌ **Não afeta validação de formulários**

---

### `blank`

* Define se o campo pode ser vazio em formulários

```python
blank=True
```

✔️ Afeta validação no Django
❌ Não altera o banco de dados

📌 **Regra prática:**

* `null` → banco
* `blank` → validação

---

### `default`

* Valor padrão do campo

```python
default=0
default=True
default='ativo'
```

Também pode receber funções:

```python
from django.utils import timezone

default=timezone.now
```

---

### `unique`

* Garante que o valor seja único no banco

```python
unique=True
```

Uso comum:

* email
* CPF
* username

---

### `choices`

* Limita os valores possíveis do campo

```python
STATUS_CHOICES = [
    ('A', 'Ativo'),
    ('I', 'Inativo'),
]

status = models.CharField(
    max_length=1,
    choices=STATUS_CHOICES
)
```

📌 No admin e formulários, vira um **select**

---

### `max_length`

* Define o tamanho máximo (obrigatório em `CharField`)

```python
max_length=255
```

---

## Opções Relacionadas a Texto

### `verbose_name`

* Nome legível do campo (admin/forms)

```python
verbose_name="Nome completo"
```

---

### `help_text`

* Texto de ajuda no admin e formulários

```python
help_text="Digite seu nome completo"
```

---

## Opções de Banco de Dados

### `db_index`

* Cria um índice no banco

```python
db_index=True
```

📌 Melhora consultas, mas aumenta custo de escrita

---

### `primary_key`

* Define o campo como chave primária

```python
primary_key=True
```

⚠️ Substitui o `id` padrão

---

### `db_column`

* Define o nome da coluna no banco

```python
db_column="nome_usuario"
```

---

### `editable`

* Define se o campo pode ser editado

```python
editable=False
```

Uso comum:

* UUID
* campos automáticos

---

## Opções de Data e Hora

### `auto_now`

* Atualiza o campo sempre que salvar

```python
models.DateTimeField(auto_now=True)
```

---

### `auto_now_add`

* Define valor apenas na criação

```python
models.DateTimeField(auto_now_add=True)
```

---

## Opções de Relacionamentos

### `on_delete`

* Define o comportamento ao excluir o objeto relacionado
  (**Obrigatório** em `ForeignKey` e `OneToOneField`)

```python
on_delete=models.CASCADE
```

Principais opções:

* `CASCADE` → apaga dependentes
* `PROTECT` → impede exclusão
* `SET_NULL` → define `NULL`
* `SET_DEFAULT` → define valor padrão
* `DO_NOTHING` → nenhuma ação

---

### `related_name`

* Nome para acessar o relacionamento reverso

```python
related_name="posts"
```

```python
autor.posts.all()
```

---

## Opções de Upload de Arquivos

### `upload_to`

* Define o diretório de upload

```python
upload_to="uploads/"
```

Também pode ser uma função:

```python
def caminho_upload(instance, filename):
    return f"user_{instance.id}/{filename}"
```

---

## Opções Avançadas

### `validators`

* Lista de validadores customizados

```python
from django.core.validators import MinValueValidator

models.IntegerField(validators=[MinValueValidator(0)])
```

---

### `error_messages`

* Mensagens de erro personalizadas

```python
error_messages={
    'unique': 'Este valor já existe'
}
```

---

## Boas Práticas

* Use `blank=True` para campos opcionais em formulários
* Evite `null=True` em campos de texto (`CharField`)
* Utilize `choices` para valores controlados
* Use `verbose_name` e `help_text` para um admin mais claro

---

## Conclusão

As **Field Options** permitem um controle fino sobre:

* validação
* banco de dados
* formulários
* experiência no admin

Elas são essenciais para criar **Models bem definidos e robustos**.
