O **Django ORM** fornece uma API poderosa e expressiva para **consultar dados no banco de dados** usando Python, sem a necessidade de escrever SQL na maioria dos casos.

Consultar dados corretamente é essencial para:

* performance
* legibilidade
* segurança
* manutenibilidade do código

---

## O Que é um QuerySet?

Um **QuerySet** representa uma **coleção de objetos** recuperados do banco.

```python
usuarios = Usuario.objects.all()
```

Características importantes:

* Lazy evaluation (executa a query apenas quando necessário)
* Pode ser encadeado
* Retorna objetos do Model

---

## Consultas Básicas

### Buscar Todos os Registros

```python
Model.objects.all()
```

---

### Buscar um Único Objeto

```python
Model.objects.get(id=1)
```

⚠️ Lança exceção se não existir ou se retornar mais de um resultado.

---

### Filtrar Dados

```python
Model.objects.filter(ativo=True)
```

---

### Excluir Dados

```python
Model.objects.exclude(ativo=False)
```

---

## Lookup Expressions (Filtros Avançados)

Os **lookups** permitem consultas mais detalhadas.

```python
Model.objects.filter(nome__icontains="django")
```

Principais lookups:

| Lookup      | Descrição                 |
| ----------- | ------------------------- |
| `exact`     | Igual                     |
| `iexact`    | Igual (case insensitive)  |
| `contains`  | Contém                    |
| `icontains` | Contém (case insensitive) |
| `in`        | Está na lista             |
| `gt`        | Maior que                 |
| `gte`       | Maior ou igual            |
| `lt`        | Menor que                 |
| `lte`       | Menor ou igual            |
| `range`     | Intervalo                 |
| `isnull`    | É NULL                    |

---

## Ordenação de Resultados

```python
Model.objects.order_by('nome')
Model.objects.order_by('-criado_em')
```

---

## Limitar Resultados

```python
Model.objects.all()[:10]
```

📌 Usa `LIMIT` no SQL.

---

## Consultas com Relacionamentos

### ForeignKey

```python
Post.objects.filter(autor__nome="João")
```

---

### ManyToMany

```python
Post.objects.filter(tags__nome="Django")
```

---

## Consultas Complexas com Q Objects

```python
from django.db.models import Q

Model.objects.filter(
    Q(ativo=True) | Q(admin=True)
)
```

📌 Permite usar `OR`, `AND` e `NOT`.

---

## Evitando Consultas Desnecessárias

### `select_related`

Usado para `ForeignKey` e `OneToOne`.

```python
Post.objects.select_related('autor')
```

---

### `prefetch_related`

Usado para `ManyToMany`.

```python
Post.objects.prefetch_related('tags')
```

---

## Consultas de Agregação

```python
from django.db.models import Count, Sum, Avg

Produto.objects.aggregate(Count('id'))
```

---

## Anotações (`annotate`)

```python
Autor.objects.annotate(total_posts=Count('post'))
```

---

## Verificando Existência

```python
Model.objects.filter(ativo=True).exists()
```

---

## Contando Registros

```python
Model.objects.count()
```

---

## Atualizações em Massa

```python
Model.objects.filter(ativo=False).update(ativo=True)
```

📌 Não chama `save()`.

---

## Deleções em Massa

```python
Model.objects.filter(ativo=False).delete()
```

---

## Avaliação Preguiçosa (Lazy Evaluation)

```python
qs = Model.objects.filter(ativo=True)
```

A query só será executada quando:

* iterar
* converter para lista
* acessar um elemento

---

## Debugando Queries

```python
print(qs.query)
```

---

## Boas Práticas

* Use filtros específicos
* Evite loops com queries dentro
* Use `select_related` e `prefetch_related`
* Não use `.all()` sem necessidade
* Evite `.get()` sem garantia de unicidade

---

## Conclusão

O Django ORM permite escrever consultas:

* legíveis
* seguras
* eficientes

Dominar consultas é fundamental para criar aplicações Django performáticas e escaláveis.

