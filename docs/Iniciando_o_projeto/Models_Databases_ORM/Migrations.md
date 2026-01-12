As **Migrations** são o mecanismo do Django para **versionar, criar e alterar a estrutura do banco de dados** de forma segura e controlada, a partir das mudanças feitas nos Models.

Elas permitem que o schema do banco evolua junto com o código, sem a necessidade de escrever SQL manualmente na maioria dos casos.

---

## O Que São Migrations?

Uma migration é um **arquivo Python** que descreve uma alteração no banco de dados, como:

* criação de tabelas
* adição ou remoção de campos
* alteração de tipos
* criação de índices e constraints
* relacionamento entre tabelas

📌 Cada app possui sua própria pasta `migrations/`.

---

## Fluxo Básico de Migrations

1. Alterar ou criar Models
2. Gerar migrations
3. Aplicar migrations no banco

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Estrutura de uma Migration

Exemplo de arquivo de migration:

```python
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
```

---

## Comandos Importantes

### `makemigrations`

Cria novas migrations com base nas alterações dos Models:

```bash
python manage.py makemigrations
```

Para um app específico:

```bash
python manage.py makemigrations app
```

---

### `migrate`

Aplica as migrations pendentes no banco:

```bash
python manage.py migrate
```

---

### `showmigrations`

Mostra o status das migrations:

```bash
python manage.py showmigrations
```

✔️ `[X]` aplicada
❌ `[ ]` pendente

---

### `sqlmigrate`

Exibe o SQL que será executado:

```bash
python manage.py sqlmigrate app 0002
```

📌 Útil para entender o impacto da migration.

---

## Migration Inicial

A primeira migration de um app geralmente se chama:

```text
0001_initial.py
```

Ela cria todas as tabelas definidas nos Models do app.

---

## Dependências entre Migrations

As migrations possuem dependências explícitas:

```python
dependencies = [
    ('auth', '0012_alter_user_first_name_max_length'),
]
```

Isso garante a ordem correta de aplicação.

---

## Alterações Comuns em Migrations

### Adicionar um Campo

```bash
makemigrations
migrate
```

---

### Remover um Campo

⚠️ Cuidado: dados serão perdidos.

---

### Alterar Tipo de Campo

Pode gerar:

* operações automáticas
* perguntas interativas (valores padrão)

---

## Migrations de Dados (Data Migrations)

Permitem **alterar dados existentes**, não apenas estrutura.

Exemplo:

```python
def forwards(apps, schema_editor):
    Usuario = apps.get_model('app', 'Usuario')
    Usuario.objects.update(ativo=True)
```

```python
operations = [
    migrations.RunPython(forwards),
]
```

---

## Migrations Irreversíveis

```python
migrations.RunPython(
    forwards,
    reverse_code=migrations.RunPython.noop
)
```

📌 Use apenas quando necessário.

---

## Migrations e Controle de Versão

* As migrations **devem ser versionadas** (Git)
* Nunca edite migrations já aplicadas em produção
* Em caso de erro, crie uma nova migration

---

## Conflitos de Migrations

Podem ocorrer quando duas branches criam migrations diferentes.

Solução comum:

```bash
python manage.py makemigrations --merge
```

---

## Resetando Migrations (Ambiente Local)

⚠️ **Apenas em desenvolvimento**

```bash
python manage.py migrate app zero
```

Depois:

```bash
rm app/migrations/00*.py
makemigrations
migrate
```

---

## Boas Práticas

* Gere migrations frequentemente
* Revise migrations antes de aplicar
* Teste em ambiente de staging
* Use `sqlmigrate` em mudanças críticas
* Evite lógica complexa em data migrations

---

## Conclusão

As **Migrations** são fundamentais para a estabilidade e evolução de aplicações Django.

Dominar migrations significa:

* menos erros em produção
* maior segurança em deploys
* controle total sobre o banco de dados

