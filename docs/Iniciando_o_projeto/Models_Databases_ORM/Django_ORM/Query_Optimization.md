A **otimização de queries** é um dos pontos mais críticos em aplicações Django.
Consultas mal planejadas causam lentidão, alto consumo de memória e sobrecarga no banco de dados.

O Django ORM fornece várias ferramentas para **reduzir queries**, **diminuir custo de execução** e **escalar a aplicação com segurança**.

---

## Princípios de Otimização

Antes de otimizar, entenda:

* Quantas queries estão sendo executadas
* Quanto tempo cada query leva
* Se o problema está no ORM ou no banco
* Se índices estão sendo utilizados

📌 **Otimização sem medição é adivinhação.**

---

## Evitando o Problema N+1

### O que é N+1?

```python
posts = Post.objects.all()
for post in posts:
    print(post.autor.nome)
```

🔴 Executa:

* 1 query para posts
* N queries para autores

---

## `select_related()`

Usado para **ForeignKey** e **OneToOne**.

```python
posts = Post.objects.select_related('autor')
```

✔️ Junta tabelas com `JOIN`

---

## `prefetch_related()`

Usado para **ManyToMany** e relações reversas.

```python
posts = Post.objects.prefetch_related('tags')
```

✔️ Executa queries separadas e faz cache em memória

---

## Escolhendo o Relacionamento Certo

| Relação                 | Use                |
| ----------------------- | ------------------ |
| ForeignKey / OneToOne   | `select_related`   |
| ManyToMany / reverse FK | `prefetch_related` |

---

## Limitando Campos Retornados

### `only()`

```python
usuarios = Usuario.objects.only('nome', 'email')
```

---

### `defer()`

```python
usuarios = Usuario.objects.defer('descricao_longa')
```

📌 Reduz tráfego de dados.

---

## Evitando Avaliações Desnecessárias

❌ Errado:

```python
if queryset:
    ...
```

✔️ Correto:

```python
if queryset.exists():
    ...
```

---

## `values()` e `values_list()`

Quando você não precisa de Models completos:

```python
Usuario.objects.values('id', 'email')
```

```python
Usuario.objects.values_list('email', flat=True)
```

✔️ Mais rápido e leve.

---

## Paginação Correta

❌ Errado:

```python
lista = list(Usuario.objects.all())[1000:1100]
```

✔️ Correto:

```python
Usuario.objects.all()[1000:1100]
```

📌 Usa `LIMIT` e `OFFSET`.

---

## Índices no Banco de Dados

### Criando índices

```python
class Produto(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
```

---

### Índices compostos

```python
class Meta:
    indexes = [
        models.Index(fields=['categoria', 'preco']),
    ]
```

---

## Usando `explain()`

```python
Usuario.objects.filter(ativo=True).explain()
```

📌 Mostra o plano de execução do banco.

---

## Cache de Queries

Use cache quando:

* Dados mudam pouco
* Queries são pesadas
* Alto volume de leitura

```python
from django.core.cache import cache

dados = cache.get('usuarios_ativos')
if not dados:
    dados = list(Usuario.objects.filter(ativo=True))
    cache.set('usuarios_ativos', dados, 300)
```

---

## Evitando Queries em Loops

❌ Errado:

```python
for id in ids:
    Usuario.objects.get(id=id)
```

✔️ Correto:

```python
Usuario.objects.filter(id__in=ids)
```

---

## Bulk Operations

### `bulk_create()`

```python
Usuario.objects.bulk_create(lista_usuarios)
```

---

### `update()`

```python
Usuario.objects.filter(ativo=False).update(ativo=True)
```

📌 Não chama `save()`.

---

## Quando Usar Raw SQL

Use Raw SQL se:

* ORM gerar queries ineficientes
* precisar de SQL avançado
* quiser controle total da execução

📎 Veja: `Raw_SQL.md`

---

## Monitoramento e Debug

### Django Debug Toolbar

* Número de queries
* Tempo de execução
* SQL gerado

📌 Essencial em desenvolvimento.

---

## Erros Comuns de Performance

* Ignorar índices
* N+1 queries
* `prefetch_related` em excesso
* Buscar mais dados do que o necessário
* Usar Python para filtrar dados do banco

---

## Checklist de Otimização

* [ ] Use `select_related` / `prefetch_related`
* [ ] Limite campos retornados
* [ ] Use índices
* [ ] Evite loops com queries
* [ ] Use cache quando necessário
* [ ] Analise queries com `explain()`

---

## Conclusão

A otimização de queries no Django é um **equilíbrio entre ORM, banco de dados e arquitetura**.

Dominar essas técnicas permite:

* aplicações rápidas
* menor custo de infraestrutura
* escalabilidade real

