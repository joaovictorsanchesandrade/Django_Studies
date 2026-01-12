Os **filters** e **lookups** permitem criar consultas precisas e expressivas no Django ORM, possibilitando filtrar dados com base em valores, intervalos, textos, datas e relacionamentos.

Eles são fundamentais para:

* construir buscas avançadas
* criar APIs eficientes
* evitar lógica desnecessária em Python

---

## O Que São Lookups?

Lookups são **operadores especiais** usados após o nome do campo, separados por `__` (double underscore).

Exemplo:

```python
Usuario.objects.filter(nome__icontains="django")
```

Estrutura:

```text
campo__lookup=valor
```

---

## Lookups Básicos

### `exact` (padrão)

```python
Usuario.objects.filter(nome__exact="João")
```

Pode ser simplificado:

```python
Usuario.objects.filter(nome="João")
```

---

### `iexact`

Igual, ignorando maiúsculas e minúsculas.

```python
Usuario.objects.filter(nome__iexact="joão")
```

---

## Lookups de Texto

### `contains` / `icontains`

```python
Post.objects.filter(titulo__contains="Django")
Post.objects.filter(titulo__icontains="django")
```

---

### `startswith` / `istartswith`

```python
Post.objects.filter(titulo__startswith="Intro")
```

---

### `endswith` / `iendswith`

```python
Post.objects.filter(titulo__endswith="ORM")
```

---

## Lookups Numéricos

### `gt`, `gte`, `lt`, `lte`

```python
Produto.objects.filter(preco__gt=100)
Produto.objects.filter(preco__lte=50)
```

---

### `range`

```python
Produto.objects.filter(preco__range=(50, 200))
```

---

## Lookups de Lista

### `in`

```python
Usuario.objects.filter(id__in=[1, 2, 3])
```

---

## Lookups de NULL

### `isnull`

```python
Usuario.objects.filter(email__isnull=True)
```

---

## Lookups de Data e Hora

### `date`, `year`, `month`, `day`

```python
Pedido.objects.filter(criado_em__year=2025)
Pedido.objects.filter(criado_em__month=1)
```

---

### `week_day`

```python
Pedido.objects.filter(criado_em__week_day=1)
```

---

## Lookups com Relacionamentos

### ForeignKey

```python
Post.objects.filter(autor__nome="João")
```

---

### ManyToMany

```python
Post.objects.filter(tags__nome="Python")
```

---

## Consultas Complexas com Q Objects

Permite combinar condições com `OR`, `AND` e `NOT`.

```python
from django.db.models import Q

Usuario.objects.filter(
    Q(ativo=True) | Q(is_admin=True)
)
```

Negação:

```python
Usuario.objects.filter(~Q(ativo=True))
```

---

## Filtros Encadeados

```python
Usuario.objects.filter(ativo=True).filter(is_admin=True)
```

📌 Equivalente a `AND`.

---

## Lookups com Expressões (`F`)

```python
from django.db.models import F

Produto.objects.filter(quantidade__gt=F('quantidade_minima'))
```

---

## Custom Lookups

É possível criar lookups personalizados:

```python
from django.db.models import Lookup

class Lowercase(Lookup):
    lookup_name = 'lower'

    def as_sql(self, compiler, connection):
        return 'LOWER(%s)' % compiler.compile(self.lhs)
```

📌 Uso avançado.

---

## Performance e Boas Práticas

* Seja específico nos filtros
* Use índices (`db_index=True`)
* Evite filtros em loops
* Combine filtros em uma única query
* Use `exists()` quando só precisa saber se existe

---

## Erros Comuns

* Esquecer `__` nos lookups
* Usar filtros de texto em campos numéricos
* Fazer múltiplas queries desnecessárias
* Ignorar impacto de performance

---

## Conclusão

Os **Filtering & Lookups** são a base das consultas no Django ORM.

Dominar esses operadores permite:

* criar buscas avançadas
* melhorar performance
* escrever código mais limpo e expressivo

