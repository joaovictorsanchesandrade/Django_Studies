A **paginação** é usada para dividir grandes conjuntos de dados em **páginas menores**, melhorando:

* performance
* experiência do usuário
* consumo de memória
* tempo de resposta

O Django fornece um sistema de paginação **simples, flexível e reutilizável**.

---

## Por Que Usar Paginação?

Sem paginação:

* páginas lentas
* alto consumo de memória
* queries pesadas
* má experiência do usuário

Com paginação:

* respostas rápidas
* navegação clara
* menor carga no banco

---

## Django Paginator

O Django oferece a classe `Paginator`:

```python
from django.core.paginator import Paginator
```

---

## Paginação Básica

```python
from django.core.paginator import Paginator

usuarios = Usuario.objects.all()
paginator = Paginator(usuarios, 10)

page = paginator.get_page(1)
```

* `10` → itens por página
* `1` → número da página

---

## Usando Paginação com Views

```python
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    paginator = Paginator(usuarios, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'usuarios.html', {
        'page_obj': page_obj
    })
```

---

## Usando no Template

```django
{% for usuario in page_obj %}
    {{ usuario.nome }}
{% endfor %}
```

---

## Navegação de Páginas

```django
<div class="pagination">
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
    {% endif %}

    <span>
        Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}
    </span>

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Próxima</a>
    {% endif %}
</div>
```

---

## Métodos Úteis do Page Object

* `has_next()`
* `has_previous()`
* `next_page_number()`
* `previous_page_number()`
* `start_index()`
* `end_index()`

```django
Mostrando {{ page_obj.start_index }}–{{ page_obj.end_index }}
```

---

## Tratamento de Erros

### Página inválida

```python
page_obj = paginator.get_page(page_number)
```

📌 Retorna a página mais próxima válida, sem lançar exceção.

---

### Controle Manual (Avançado)

```python
from django.core.paginator import EmptyPage, PageNotAnInteger

try:
    page_obj = paginator.page(page_number)
except PageNotAnInteger:
    page_obj = paginator.page(1)
except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)
```

---

## Paginação e ORM (Performance)

```python
usuarios = Usuario.objects.all()
```

📌 O Django usa `LIMIT` e `OFFSET` automaticamente.

---

## Paginação com `select_related`

```python
usuarios = Usuario.objects.select_related('perfil')
```

📌 Evita N+1 queries.

---

## Paginação com Filtros

```python
usuarios = Usuario.objects.filter(ativo=True)
paginator = Paginator(usuarios, 20)
```

---

## Paginação em Class-Based Views

### `ListView`

```python
from django.views.generic import ListView

class UsuarioListView(ListView):
    model = Usuario
    paginate_by = 10
```

Template:

```django
{{ page_obj }}
```

---

## Paginação em APIs

📌 No Django REST Framework, a paginação é feita com classes específicas.

➡️ Veja: `DRF Pagination`

---

## Boas Práticas

* Sempre pagine listas grandes
* Use filtros antes da paginação
* Combine com índices no banco
* Evite paginação profunda (`OFFSET` muito alto)
* Considere cursor pagination em grandes volumes

---

## Paginação Profunda (Problema)

`OFFSET` muito alto pode ser lento.

Alternativas:

* paginação por cursor
* paginação por ID
* paginação baseada em datas

---

## Erros Comuns

* Paginar listas Python (`list()`)
* Esquecer parâmetros GET
* Não tratar página inválida
* Ignorar performance

---

## Conclusão

A **paginação no Django** é simples de implementar e extremamente eficaz.

Quando bem utilizada:

* melhora performance
* melhora UX
* reduz custo
* aumenta escalabilidade

