## O que são filtros?

Filtros permitem **modificar ou formatar valores de variáveis** diretamente nos templates.
Eles são aplicados com a sintaxe:

```html
{{ variável|filtro }}
```

Filtros podem ser **embutidos** no Django ou **criados por você** (custom filters).

---

## Filtros embutidos do Django

### Filtros de texto

| Filtro             | Exemplo   | Resultado            |                                          |
| ------------------ | --------- | -------------------- | ---------------------------------------- |
| `upper`            | `{{ texto | upper }}`            | Converte para maiúsculas                 |
| `lower`            | `{{ texto | lower }}`            | Converte para minúsculas                 |
| `title`            | `{{ texto | title }}`            | Primeira letra de cada palavra maiúscula |
| `truncatechars:10` | `{{ texto | truncatechars:10 }}` | Trunca texto para 10 caracteres          |

---

### Filtros de números

| Filtro        | Exemplo       | Resultado                           |                               |
| ------------- | ------------- | ----------------------------------- | ----------------------------- |
| `add`         | `{{ numero    | add:"10" }}`                        | Soma 10 ao número             |
| `floatformat` | `{{ numero    | floatformat:2 }}`                   | Formata para 2 casas decimais |
| `divisibleby` | `{% if numero | divisibleby:"3" %} ... {% endif %}` | Checa se número é divisível   |

---

### Filtros de listas e dicionários

| Filtro    | Exemplo   | Resultado            |                                            |
| --------- | --------- | -------------------- | ------------------------------------------ |
| `length`  | `{{ lista | length }}`           | Retorna o tamanho da lista                 |
| `first`   | `{{ lista | first }}`            | Retorna o primeiro item da lista           |
| `last`    | `{{ lista | last }}`             | Retorna o último item da lista             |
| `default` | `{{ valor | default:"Padrão" }}` | Retorna um valor padrão se `None` ou vazio |

---

### Filtros de datas

| Filtro         | Exemplo  | Resultado        |                           |
| -------------- | -------- | ---------------- | ------------------------- |
| `date:"d/m/Y"` | `{{ data | date:"d/m/Y" }}` | Formata datas             |
| `time:"H:i"`   | `{{ hora | time:"H:i" }}`   | Formata hora              |
| `timesince`    | `{{ data | timesince }}`    | Mostra tempo desde a data |

---

## Encadeamento de filtros

Filtros podem ser **encadeados**:

```html
{{ texto|truncatechars:20|upper }}
```

Isso trunca o texto para 20 caracteres e converte para maiúsculas.

---

## Filtros personalizados (custom filters)

Filtros personalizados permitem **criar suas próprias funções** para manipular variáveis no template.

---

### Criando um filtro personalizado

1. Crie um arquivo chamado `templatetags/meufiltro.py` na sua app:

```python
from django import template

register = template.Library()

@register.filter
def dobrar(valor):
    return valor * 2
```

2. No template, carregue o filtro:

```html
{% load meufiltro %}
<p>Dobro: {{ numero|dobrar }}</p>
```

---

### Registrando filtros

* Use `@register.filter` para registrar funções como filtros
* O nome do filtro será o nome da função por padrão
* Você pode passar argumentos opcionais:

```python
@register.filter
def multiplicar(valor, fator):
    return valor * fator
```

Uso no template:

```html
{{ 5|multiplicar:3 }}  <!-- Resultado: 15 -->
```

---

## Boas práticas

* Use filtros apenas para **apresentação de dados**, não lógica complexa
* Mantenha nomes **claros e curtos**
* Prefira filtros embutidos sempre que possível
* Documente filtros personalizados para fácil manutenção

---

## Resumo

* Filtros modificam ou formatam valores em templates
* Existem filtros embutidos de texto, números, listas, dicionários e datas
* Filtros podem ser encadeados
* É possível criar filtros personalizados para necessidades específicas
* Use filtros para **apresentação**, mantendo a lógica na view ou model

