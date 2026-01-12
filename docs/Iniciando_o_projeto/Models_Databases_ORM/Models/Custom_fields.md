Os **Custom Fields** permitem criar **novos tipos de campos** no Django quando os campos padrão não atendem totalmente às necessidades do projeto.

Eles são úteis para:

* validações específicas
* formatos de dados personalizados
* reutilização de lógica
* padronização de dados em múltiplos models

---

## Quando Criar um Custom Field?

Você deve considerar um campo personalizado quando:

* Um campo padrão exige **muita lógica repetida**
* O dado precisa ser **normalizado automaticamente**
* Existe uma **validação complexa e recorrente**
* O formato armazenado no banco é diferente do formato exibido

📌 Se for apenas validação simples, prefira `validators`.

---

## Estrutura Básica de um Custom Field

Todo campo personalizado deve herdar de `models.Field` ou de um campo existente.

Exemplo simples:

```python
from django.db import models

class UpperCaseCharField(models.CharField):
    def get_prep_value(self, value):
        return value.upper() if value else value
```

Uso:

```python
class Usuario(models.Model):
    nome = UpperCaseCharField(max_length=100)
```

---

## Métodos Importantes

### `get_prep_value(value)`

* Executado antes de salvar no banco
* Ideal para **normalização**

```python
def get_prep_value(self, value):
    return value.strip().lower()
```

---

### `from_db_value(value, expression, connection)`

* Executado ao ler do banco
* Permite transformar o valor retornado

```python
def from_db_value(self, value, expression, connection):
    return value
```

---

### `to_python(value)`

* Converte o valor para o tipo Python
* Chamado em formulários e queries

```python
def to_python(self, value):
    return value
```

---

## Criando um Campo Personalizado do Zero

Exemplo: Campo para armazenar **CPF** sem formatação

```python
from django.db import models
import re

class CPFField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value:
            return re.sub(r'\D', '', value)
        return value
```

Uso:

```python
class Cliente(models.Model):
    cpf = CPFField(unique=True)
```

---

## Custom Field + Validação

```python
from django.core.exceptions import ValidationError

class PositiveIntegerField(models.IntegerField):
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value < 0:
            raise ValidationError("O valor não pode ser negativo")
```

---

## Campos Personalizados com `deconstruct`

Para que o Django consiga gerar migrations corretamente, campos customizados devem implementar `deconstruct`.

```python
def deconstruct(self):
    name, path, args, kwargs = super().deconstruct()
    return name, path, args, kwargs
```

📌 Necessário quando:

* Você altera parâmetros no `__init__`
* Adiciona atributos extras ao campo

---

## Custom Fields e Formulários

Para controlar como o campo aparece em formulários:

```python
from django import forms

class CPFField(models.CharField):
    def formfield(self, **kwargs):
        defaults = {'form_class': forms.CharField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
```

---

## Custom Fields vs Validators

| Situação                | Melhor escolha |
| ----------------------- | -------------- |
| Validação simples       | Validators     |
| Normalização automática | Custom Field   |
| Lógica reutilizável     | Custom Field   |
| Regra pontual           | Validators     |

---

## Boas Práticas

* Prefira herdar de um campo existente
* Documente o comportamento do campo
* Evite lógica pesada
* Teste bem (save, query, forms, admin)
* Use `deconstruct` corretamente

---

## Conclusão

Os **Custom Fields** permitem estender o Django de forma elegante e poderosa, criando abstrações reutilizáveis e consistentes.

Eles devem ser usados com cuidado, mas quando bem aplicados:

* reduzem duplicação
* melhoram a qualidade do código
* deixam os Models mais expressivos

