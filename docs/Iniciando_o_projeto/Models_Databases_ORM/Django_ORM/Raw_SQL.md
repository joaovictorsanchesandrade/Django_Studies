Embora o **Django ORM** cubra a grande maioria dos casos de uso, existem situações em que escrever **SQL puro (Raw SQL)** é necessário ou mais eficiente.

O Django oferece formas **seguras e integradas** de executar SQL diretamente, sem abrir mão da proteção contra SQL Injection.

---

## Quando Usar Raw SQL?

Use SQL puro quando:

* A consulta é **muito complexa** para o ORM
* Você precisa de **features específicas do banco**
* Performance crítica exige SQL otimizado
* Queries legadas já existem
* Uso de **CTEs**, **window functions**, hints, etc.

📌 Regra geral: **prefira o ORM**, use Raw SQL apenas quando necessário.

---

## Executando Consultas com `raw()`

### Método `Model.objects.raw()`

Permite executar uma query SQL e mapear os resultados para um Model.

```python
usuarios = Usuario.objects.raw(
    "SELECT * FROM usuario WHERE ativo = %s",
    [True]
)
```

Características:

* Retorna objetos do Model
* Campos devem corresponder aos do Model
* Deve incluir a chave primária

---

## Usando Cursor Manualmente

### `connection.cursor()`

Usado para total controle da query.

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT COUNT(*) FROM usuario WHERE ativo = %s",
        [True]
    )
    row = cursor.fetchone()
```

📌 Retorna tuplas, não objetos.

---

## Evitando SQL Injection

❌ **Nunca** concatene strings:

```python
# ERRADO
cursor.execute(f"SELECT * FROM usuario WHERE nome = '{nome}'")
```

✔️ **Use parâmetros**:

```python
cursor.execute(
    "SELECT * FROM usuario WHERE nome = %s",
    [nome]
)
```

---

## Raw SQL para INSERT, UPDATE e DELETE

```python
with connection.cursor() as cursor:
    cursor.execute(
        "UPDATE produto SET preco = preco * 1.1"
    )
```

📌 Não dispara signals nem validações.

---

## Transações com Raw SQL

```python
from django.db import transaction

with transaction.atomic():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM logs")
```

---

## Executando SQL Específico do Banco

Exemplo (PostgreSQL):

```python
cursor.execute(
    "SELECT to_char(created_at, 'YYYY-MM') FROM pedidos"
)
```

📌 Cuidado com portabilidade.

---

## Integrando Raw SQL com QuerySets

Você pode misturar ORM e SQL:

```python
ids = [u.id for u in Usuario.objects.raw("SELECT id FROM usuario")]
Usuario.objects.filter(id__in=ids)
```

---

## Debugando Queries SQL do ORM

```python
print(queryset.query)
```

📌 Ajuda a decidir quando usar Raw SQL.

---

## Migrations com SQL Puro

```python
from django.db import migrations

class Migration(migrations.Migration):

    operations = [
        migrations.RunSQL(
            "CREATE INDEX idx_nome ON usuario(nome);"
        )
    ]
```

---

## Performance e Boas Práticas

* Use Raw SQL apenas quando necessário
* Sempre use parâmetros
* Documente queries complexas
* Prefira `raw()` quando quiser Models
* Teste em staging antes de produção

---

## Erros Comuns

* SQL Injection
* Ignorar transações
* Escrever SQL dependente do banco sem necessidade
* Usar Raw SQL onde o ORM resolveria

---

## Conclusão

O **Raw SQL** é uma ferramenta poderosa que complementa o Django ORM.

Quando bem utilizado:

* melhora performance
* resolve casos complexos
* mantém controle total sobre a query

Mas deve ser usado com **cuidado e responsabilidade**.

