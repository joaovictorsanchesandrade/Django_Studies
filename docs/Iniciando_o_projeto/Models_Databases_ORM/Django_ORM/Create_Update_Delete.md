O Django ORM fornece uma API clara e segura para **criar, atualizar e remover registros** no banco de dados, sem a necessidade de escrever SQL manualmente.

Essas operações formam o núcleo do **CRUD**:

* **Create** → criar dados
* **Read** → consultar dados
* **Update** → atualizar dados
* **Delete** → remover dados

(Este arquivo foca em **Create, Update e Delete**.)

---

## Create (Criar Registros)

### Criando com `.create()`

Cria e salva o objeto em uma única operação:

```python
Usuario.objects.create(
    nome="João",
    email="joao@email.com"
)
```

📌 Simples e direto.

---

### Criando com `.save()`

Mais controle sobre o processo:

```python
usuario = Usuario(
    nome="João",
    email="joao@email.com"
)
usuario.save()
```

📌 Útil quando você precisa executar lógica antes de salvar.

---

### Criando Relacionamentos

#### ForeignKey

```python
post = Post.objects.create(
    titulo="Meu Post",
    autor=autor
)
```

---

#### ManyToMany

```python
post.tags.add(tag1, tag2)
```

⚠️ O objeto precisa existir antes.

---

## Update (Atualizar Registros)

### Atualizando um Objeto

```python
usuario = Usuario.objects.get(id=1)
usuario.nome = "Novo Nome"
usuario.save()
```

---

### Atualização em Massa (`update()`)

```python
Usuario.objects.filter(ativo=False).update(ativo=True)
```

📌 Mais rápido
⚠️ Não chama `save()` nem signals

---

### Atualizando Campos Específicos

```python
usuario.save(update_fields=['nome'])
```

---

## Delete (Excluir Registros)

### Excluindo um Objeto

```python
usuario.delete()
```

---

### Excluindo em Massa

```python
Usuario.objects.filter(ativo=False).delete()
```

📌 Pode apagar muitos registros de uma vez.

---

## Soft Delete (Exclusão Lógica)

Em vez de remover o registro, marca como inativo:

```python
class Usuario(models.Model):
    ativo = models.BooleanField(default=True)

    def delete(self):
        self.ativo = False
        self.save()
```

📌 Boa prática para dados importantes.

---

## Métodos Úteis

### `get_or_create()`

```python
obj, criado = Categoria.objects.get_or_create(
    nome="Django"
)
```

✔️ Evita duplicação
✔️ Retorna se foi criado ou não

---

### `update_or_create()`

```python
obj, criado = Produto.objects.update_or_create(
    codigo="123",
    defaults={"preco": 10}
)
```

---

## Operações Atômicas (Transactions)

```python
from django.db import transaction

with transaction.atomic():
    pedido.save()
    pagamento.save()
```

📌 Garante consistência dos dados.

---

## Validação Antes de Salvar

```python
usuario.full_clean()
usuario.save()
```

📌 Força validações do Model.

---

## Erros Comuns

* Esquecer `save()`
* Usar `update()` esperando signals
* Deletar dados críticos sem backup
* Criar relacionamentos antes de salvar o objeto principal

---

## Boas Práticas

* Prefira `.create()` para simplicidade
* Use `.update()` apenas quando souber o impacto
* Implemente soft delete quando necessário
* Use transactions em operações críticas
* Centralize regras de negócio nos Models

---

## Conclusão

O Django ORM torna as operações de **Create, Update e Delete**:

* simples
* seguras
* eficientes

Dominar essas operações é essencial para qualquer aplicação Django profissional.


