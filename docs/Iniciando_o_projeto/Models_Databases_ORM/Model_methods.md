Os **Model Methods** permitem adicionar **comportamento e regras de negócio** diretamente aos Models.
Eles tornam o código mais organizado, reutilizável e alinhado ao domínio da aplicação.

Em Django, um Model não deve apenas armazenar dados, mas também **saber operar sobre eles**.

---

## O Que São Model Methods?

São **métodos Python normais** definidos dentro de uma classe que herda de `models.Model`.

Exemplo simples:

```python
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def preco_com_desconto(self, percentual):
        return self.preco - (self.preco * percentual / 100)
```

Uso:

```python
produto.preco_com_desconto(10)
```

---

## Métodos Especiais (Magic Methods)

### `__str__`

Define a representação em string do objeto.
Muito importante para o **Django Admin**.

```python
def __str__(self):
    return self.nome
```

📌 Sempre implemente `__str__` em seus Models.

---

### `__repr__` (opcional)

Usado principalmente para debug.

```python
def __repr__(self):
    return f"<Produto {self.id} - {self.nome}>"
```

---

## Métodos de Negócio (Business Logic)

Os Models são um bom lugar para regras relacionadas diretamente à entidade.

Exemplo:

```python
class Pedido(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)

    def marcar_como_pago(self):
        self.pago = True
        self.save()
```

---

## Métodos de Estado

Usados para verificar condições do objeto.

```python
class Usuario(models.Model):
    ativo = models.BooleanField(default=True)

    def esta_ativo(self):
        return self.ativo
```

---

## Métodos que Retornam Dados Calculados

```python
class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def total_itens(self):
        return self.itens.count()
```

---

## Uso de `@property`

Permite acessar métodos como atributos.

```python
class Produto(models.Model):
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def preco_formatado(self):
        return f"R$ {self.preco}"
```

Uso:

```python
produto.preco_formatado
```

📌 Ideal para valores derivados que não precisam ser salvos.

---

## Métodos que Usam Relacionamentos

```python
class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def total_posts(self):
        return self.posts.count()
```

---

## Sobrescrevendo Métodos do Model

### `save()`

Pode ser sobrescrito para lógica antes ou depois de salvar.

```python
def save(self, *args, **kwargs):
    self.nome = self.nome.upper()
    super().save(*args, **kwargs)
```

⚠️ Sempre chame `super()`.

---

### `delete()`

```python
def delete(self, *args, **kwargs):
    super().delete(*args, **kwargs)
```

📌 Use com cautela.

---

## Métodos vs Signals

| Situação                | Melhor escolha |
| ----------------------- | -------------- |
| Regra ligada à entidade | Model Method   |
| Ação automática global  | Signal         |
| Código explícito        | Model Method   |
| Acoplamento fraco       | Signal         |

📌 Prefira **Model Methods** sempre que possível.

---

## Métodos para o Django Admin

```python
class Produto(models.Model):
    ativo = models.BooleanField(default=True)

    def status(self):
        return "Ativo" if self.ativo else "Inativo"

    status.short_description = "Status"
```

---

## Boas Práticas

* Mantenha métodos curtos e claros
* Não coloque lógica de view no model
* Use nomes semânticos
* Evite efeitos colaterais inesperados
* Centralize regras de negócio

---

## Conclusão

Os **Model Methods** tornam seus Models:

* mais expressivos
* mais reutilizáveis
* mais fáceis de manter

Eles ajudam a manter a **regra de negócio no lugar certo**, evitando código duplicado em views, serializers ou forms.

