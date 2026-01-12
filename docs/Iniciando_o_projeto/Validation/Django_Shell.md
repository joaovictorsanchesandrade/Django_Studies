O **Django Shell** é uma ferramenta interativa que permite **executar código Python dentro do contexto do projeto Django**.
Ele é extremamente útil para testes rápidos, depuração, consultas ao banco de dados, validações e exploração do ORM.

Se você usa Django profissionalmente, o shell será uma das ferramentas mais utilizadas no dia a dia.

---

## O Que é o Django Shell?

O Django Shell é um **REPL (Read–Eval–Print Loop)** que:

* carrega automaticamente o `settings.py`
* inicializa o Django ORM
* permite acesso aos Models, configurações e apps

Ele elimina a necessidade de criar views ou scripts apenas para testar algo.

---

## Iniciando o Django Shell

```bash
python manage.py shell
```

📌 Certifique-se de estar no diretório do projeto e com o ambiente virtual ativo.

---

## Django Shell Plus (Recomendado)

Com **django-extensions**:

```bash
pip install django-extensions
```

Adicionar em `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django_extensions',
]
```

Iniciar:

```bash
python manage.py shell_plus
```

### Vantagens do `shell_plus`

* Importa **todos os Models automaticamente**
* Menos código repetitivo
* Mais produtividade

---

## Importando Models Manualmente

```python
from app.models import Usuario, Post
```

---

## Usos Comuns do Django Shell

### Criar Registros

```python
Usuario.objects.create(
    nome="João",
    email="joao@email.com"
)
```

---

### Consultar Dados

```python
Usuario.objects.all()
Usuario.objects.filter(ativo=True)
Usuario.objects.get(id=1)
```

---

### Atualizar Registros

```python
usuario = Usuario.objects.get(id=1)
usuario.nome = "Novo Nome"
usuario.save()
```

---

### Excluir Registros

```python
Usuario.objects.filter(ativo=False).delete()
```

---

## Testando Validações

```python
usuario = Usuario(nome="")
usuario.full_clean()
```

📌 Executa validações do Model sem salvar no banco.

---

## Testando Forms

```python
form = UsuarioForm(data={'email': 'invalido'})
form.is_valid()
form.errors
```

---

## Inspecionando Queries SQL

```python
queryset = Usuario.objects.filter(ativo=True)
print(queryset.query)
```

📌 Fundamental para otimização.

---

## Trabalhando com Transactions

```python
from django.db import transaction

with transaction.atomic():
    Usuario.objects.create(nome="Teste")
```

---

## Executando Código Temporário

Útil para:

* corrigir dados
* migrações manuais
* scripts rápidos

```python
for usuario in Usuario.objects.all():
    usuario.slug = usuario.nome.lower()
    usuario.save()
```

---

## Carregando Dados de Teste

```python
from django.core.management import call_command

call_command('loaddata', 'dados.json')
```

---

## Debugando Erros

```python
try:
    Usuario.objects.get(id=999)
except Usuario.DoesNotExist:
    print("Usuário não encontrado")
```

---

## Shell e Performance

⚠️ Atenção:

* Evite loops com queries
* Use `bulk_create`, `update`
* Prefira testar otimizações no shell

---

## Boas Práticas

* Use o shell para testes rápidos
* Não rode scripts destrutivos em produção
* Documente comandos importantes
* Prefira `shell_plus`
* Use para entender o ORM

---

## Erros Comuns

* Executar comandos sem entender o impacto
* Usar shell em produção sem cuidado
* Esquecer ambiente virtual
* Criar dados inconsistentes

---

## Django Shell vs Scripts

| Uso                 | Melhor Opção       |
| ------------------- | ------------------ |
| Teste rápido        | Django Shell       |
| Script reutilizável | Management Command |
| Debug ORM           | Django Shell       |
| Automação           | Command            |

---

## Conclusão

O **Django Shell** é uma ferramenta indispensável para:

* aprender Django
* dominar o ORM
* depurar problemas
* testar validações
* ganhar produtividade

Dominar o shell acelera drasticamente seu desenvolvimento.

