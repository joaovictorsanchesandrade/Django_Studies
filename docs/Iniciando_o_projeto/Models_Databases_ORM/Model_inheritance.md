A **herança de Models** no Django permite **reutilizar campos e comportamentos** entre diferentes Models, evitando duplicação de código e facilitando a manutenção.

O Django oferece **três tipos principais de herança**, cada um com impactos diferentes no banco de dados.

---

## Por Que Usar Herança em Models?

Use herança quando:

* Existem **campos comuns** entre vários Models
* Há **comportamento compartilhado** (métodos)
* Você deseja **padronizar estruturas**
* Quer manter o código mais limpo e reutilizável

📌 Herança não é obrigatória, mas quando bem usada melhora bastante o design do sistema.

---

## Tipos de Herança no Django

1. **Abstract Base Classes**
2. **Multi-table Inheritance**
3. **Proxy Models**

---

## Abstract Base Classes (Classe Abstrata)

### O Que É?

Uma **classe abstrata** não cria tabela no banco.
Ela serve apenas para **fornecer campos e métodos** para os Models filhos.

### Exemplo

```python
from django.db import models

class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

Uso:

```python
class Post(BaseModel):
    titulo = models.CharField(max_length=100)

class Comentario(BaseModel):
    texto = models.TextField()
```

📌 Cada Model terá seus próprios campos no banco, mas **nenhuma tabela BaseModel será criada**.

---

### Quando Usar Abstract Base Classes

* Campos padrão (`created_at`, `updated_at`)
* Soft delete
* Auditoria
* Métodos comuns

---

## Multi-table Inheritance (Herança com Múltiplas Tabelas)

### O Que É?

Cada classe da hierarquia gera **sua própria tabela**.
O Django cria automaticamente um **OneToOneField** entre elas.

### Exemplo

```python
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

class Cliente(Pessoa):
    limite_credito = models.DecimalField(max_digits=8, decimal_places=2)
```

Banco de dados:

* Tabela `Pessoa`
* Tabela `Cliente` (ligada por OneToOne)

Acesso:

```python
cliente.nome
```

---

### Quando Usar Multi-table Inheritance

* Entidades realmente diferentes
* Hierarquia clara
* Necessidade de consultas separadas

⚠️ Pode impactar performance devido a joins.

---

## Proxy Models

### O Que É?

Permite **alterar comportamento** (métodos, admin, ordering) **sem alterar o banco de dados**.

📌 Não cria nova tabela.

### Exemplo

```python
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

class ProdutoAtivo(Produto):
    class Meta:
        proxy = True
        ordering = ['nome']

    def is_disponivel(self):
        return self.ativo
```

---

### Quando Usar Proxy Models

* Criar múltiplas visões do mesmo Model
* Admin customizado
* Ordenações diferentes
* Métodos específicos

---

## Comparação dos Tipos de Herança

| Tipo          | Cria tabela? | Uso principal           |
| ------------- | ------------ | ----------------------- |
| Abstract Base | ❌            | Reutilização de campos  |
| Multi-table   | ✅            | Hierarquia de entidades |
| Proxy         | ❌            | Alterar comportamento   |

---

## Herança e Métodos

Métodos definidos na classe base são herdados normalmente:

```python
class Base(models.Model):
    def ativo(self):
        return True

    class Meta:
        abstract = True
```

---

## Herança e Meta Options

As opções `Meta` **não são herdadas automaticamente** (exceto em Proxy Models).

```python
class Meta:
    ordering = ['-id']
```

📌 Reaplique quando necessário.

---

## Boas Práticas

* Prefira **Abstract Base Classes**
* Use Multi-table apenas quando necessário
* Evite heranças profundas
* Documente a hierarquia
* Pense no impacto no banco

---

## Conclusão

A **herança de Models** é uma ferramenta poderosa para estruturar aplicações Django de forma elegante e escalável.

Quando bem utilizada:

* reduz duplicação
* melhora legibilidade
* organiza o domínio da aplicação

