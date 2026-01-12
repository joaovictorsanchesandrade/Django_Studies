As **Aggregations** permitem executar **operações matemáticas e estatísticas diretamente no banco de dados**, como contagem, soma, média, mínimo e máximo.

Usar agregações corretamente:

* reduz uso de memória
* melhora performance
* evita processamento desnecessário em Python

---

## O Que São Aggregations?

Aggregations são funções que **resumem um conjunto de registros** em um único valor.

Exemplos comuns:

* total de registros
* soma de valores
* média
* maior ou menor valor

No Django, elas são acessadas por meio do módulo:

```python
from django.db.models import Count, Sum, Avg, Max, Min
```

---

## Aggregate vs Annotate

### `aggregate()`

* Retorna **um único resultado**
* Aplica a agregação sobre todo o QuerySet

### `annotate()`

* Retorna **um valor agregado por objeto**
* Adiciona um campo calculado a cada registro

---

## Usando `aggregate()`

### Contando Registros

```python
Usuario.objects.aggregate(total=Count('id'))
```

Resultado:

```python
{'total': 150}
```

---

### Soma de Valores

```python
Pedido.objects.aggregate(total=Sum('valor'))
```

---

### Média

```python
Produto.objects.aggregate(preco_medio=Avg('preco'))
```

---

### Máximo e Mínimo

```python
Produto.objects.aggregate(
    maior=Max('preco'),
    menor=Min('preco')
)
```

---

## Usando `annotate()`

### Contagem por Relacionamento

```python
from django.db.models import Count

Autor.objects.annotate(
    total_posts=Count('posts')
)
```

Uso:

```python
autor.total_posts
```

---

### Soma por Grupo

```python
Cliente.objects.annotate(
    total_gasto=Sum('pedidos__valor')
)
```

---

## Agrupamento de Dados

Agrupamentos são feitos automaticamente com `annotate()`.

Exemplo:

```python
Post.objects.values('status').annotate(
    total=Count('id')
)
```

---

## Filtrando Aggregations

```python
Autor.objects.annotate(
    total_posts=Count('posts')
).filter(total_posts__gt=5)
```

---

## Aggregations com `distinct`

```python
Count('posts', distinct=True)
```

---

## Aggregations com Condições

### Usando `filter` (Django moderno)

```python
from django.db.models import Q

Count('posts', filter=Q(posts__publicado=True))
```

---

## Expressões com Aggregations

```python
from django.db.models import F

Produto.objects.annotate(
    valor_total=F('preco') * F('quantidade')
)
```

---

## Aggregations em Relacionamentos

```python
Categoria.objects.annotate(
    total_produtos=Count('produtos')
)
```

---

## Performance e Boas Práticas

* Prefira agregações no banco
* Evite loops em Python para cálculos
* Use `select_related` e `prefetch_related` quando necessário
* Cuidado com `distinct`, pode impactar performance
* Sempre avalie o SQL gerado

---

## Debugando Aggregations

```python
print(queryset.query)
```

---

## Casos Comuns de Uso

* Dashboards
* Relatórios
* Estatísticas
* Rankings
* KPIs

---

## Erros Comuns

* Usar `aggregate()` esperando múltiplos resultados
* Esquecer relacionamentos corretos
* Agrupar dados sem `values()`
* Fazer cálculos em Python desnecessariamente

---

## Conclusão

As **Aggregations** são essenciais para trabalhar com dados de forma eficiente no Django ORM.

Dominar agregações permite:

* criar relatórios performáticos
* reduzir carga da aplicação
* aproveitar o poder do banco de dados

