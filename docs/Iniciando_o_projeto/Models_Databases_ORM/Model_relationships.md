Os **relacionamentos entre Models** permitem conectar dados de forma estruturada e eficiente.
No Django, eles são implementados diretamente nos Models por meio de **campos de relacionamento**, e o ORM cuida automaticamente das consultas, joins e integridade referencial.

---

## Tipos de Relacionamentos no Django

O Django suporta três tipos principais de relacionamentos:

1. **One-to-One (Um para Um)**
2. **One-to-Many (Um para Muitos)**
3. **Many-to-Many (Muitos para Muitos)**

---

## One-to-One Relationship (Um para Um)

### `OneToOneField`

Usado quando **cada instância de um Model se relaciona com exatamente uma instância de outro Model**.

Exemplo clássico: `User` e `Perfil`

```python
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
```

Uso:

* extensão do `User`
* configurações específicas
* dados complementares

Acesso:

```python
perfil.user
user.perfil
```

---

## One-to-Many Relationship (Um para Muitos)

### `ForeignKey`

Usado quando **um objeto pode estar associado a vários outros**, mas cada objeto pertence a apenas um.

Exemplo: `Autor` e `Post`

```python
class Autor(models.Model):
    nome = models.CharField(max_length=100)

class Post(models.Model):
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE
    )
```

Acesso:

```python
post.autor
autor.post_set.all()
```

📌 O Django cria automaticamente o relacionamento reverso com o sufixo `_set`.

---

## Many-to-Many Relationship (Muitos para Muitos)

### `ManyToManyField`

Usado quando **múltiplos objetos se relacionam entre si**.

Exemplo: `Post` e `Tag`

```python
class Tag(models.Model):
    nome = models.CharField(max_length=50)

class Post(models.Model):
    tags = models.ManyToManyField(Tag)
```

Acesso:

```python
post.tags.all()
tag.post_set.all()
```

📌 O Django cria automaticamente uma **tabela intermediária**.

---

## Personalizando Relacionamentos

### `related_name`

Define o nome do relacionamento reverso:

```python
autor = models.ForeignKey(
    Autor,
    related_name="posts",
    on_delete=models.CASCADE
)
```

```python
autor.posts.all()
```

---

### `related_query_name`

Define o nome usado em filtros:

```python
related_query_name="post"
```

```python
Autor.objects.filter(post__titulo="Django")
```

---

## Controle de Exclusão: `on_delete`

Define o comportamento quando o objeto relacionado é removido.

Principais opções:

* `CASCADE` → apaga os dependentes
* `PROTECT` → impede a exclusão
* `SET_NULL` → define como `NULL`
* `SET_DEFAULT` → define valor padrão
* `DO_NOTHING` → nenhuma ação

Exemplo:

```python
models.ForeignKey(
    Categoria,
    on_delete=models.PROTECT
)
```

---

## Relacionamentos Opcionais

Para permitir que um relacionamento seja opcional:

```python
models.ForeignKey(
    Categoria,
    null=True,
    blank=True,
    on_delete=models.SET_NULL
)
```

---

## Tabela Intermediária (Through)

Em relacionamentos `ManyToMany`, é possível definir uma tabela intermediária personalizada.

Exemplo: `Aluno` e `Curso` com data de matrícula

```python
class Matricula(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    data = models.DateField()

class Aluno(models.Model):
    cursos = models.ManyToManyField(
        'Curso',
        through='Matricula'
    )
```

---

## Consultas com Relacionamentos

### `select_related`

* Usado para **ForeignKey e OneToOne**
* Evita múltiplas queries

```python
Post.objects.select_related('autor')
```

---

### `prefetch_related`

* Usado para **ManyToMany**
* Executa consultas separadas e faz cache

```python
Post.objects.prefetch_related('tags')
```

---

## Relacionamentos e Admin

O Django Admin entende relacionamentos automaticamente:

* `ForeignKey` → dropdown
* `ManyToManyField` → seleção múltipla
* `OneToOneField` → inline comum

Exemplo de inline:

```python
class PerfilInline(admin.StackedInline):
    model = Perfil
```

---

## Boas Práticas

* Use `related_name` sempre que possível
* Evite nomes genéricos como `data`, `status`
* Use `PROTECT` para dados críticos
* Utilize `select_related` e `prefetch_related` para performance
* Pense no relacionamento antes de modelar tabelas

---

## Conclusão

Os **relacionamentos entre Models** são um dos maiores diferenciais do Django ORM.
Eles permitem criar estruturas de dados complexas de forma simples, segura e performática.

Dominar relacionamentos significa:

* escrever menos SQL
* evitar bugs de integridade
* criar aplicações escaláveis

