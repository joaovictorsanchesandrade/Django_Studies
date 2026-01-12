## O que são tags no Django Template?

Tags são **instruções especiais** no template que controlam **fluxo, lógica, inclusão de templates, loops e outras funcionalidades**.
Elas são delimitadas por `{% %}` e **não retornam valores**, diferentemente das variáveis (`{{ }}`).

Exemplo básico:

```html
{% if usuario.is_authenticated %}
<p>Olá, {{ usuario.nome }}!</p>
{% endif %}
```

---

## Tags embutidas do Django

### Controle de fluxo

| Tag         | Uso                          | Exemplo                                                    |
| ----------- | ---------------------------- | ---------------------------------------------------------- |
| `if`        | Condicional simples          | `{% if usuario.is_staff %}Admin{% endif %}`                |
| `elif`      | Condicional adicional        | `{% if x > 10 %}Maior{% elif x == 10 %}Igual{% endif %}`   |
| `else`      | Alternativa                  | `{% if ativo %}Ativo{% else %}Inativo{% endif %}`          |
| `ifchanged` | Executa bloco se valor mudou | `{% ifchanged usuario.nome %}Nome mudou{% endifchanged %}` |

---

### Loops

| Tag     | Uso                                        | Exemplo                                                               |
| ------- | ------------------------------------------ | --------------------------------------------------------------------- |
| `for`   | Iteração sobre listas, tuplas ou querysets | `{% for item in lista %}{{ item }}{% endfor %}`                       |
| `empty` | Bloco executado se lista vazia             | `{% for item in lista %}{{ item }}{% empty %}Nenhum item{% endfor %}` |

Variáveis especiais em loops:

* `forloop.counter` → contador iniciando em 1
* `forloop.counter0` → contador iniciando em 0
* `forloop.first` → True se for o primeiro item
* `forloop.last` → True se for o último item

---

### Inclusão e herança

| Tag       | Uso                        | Exemplo                                     |
| --------- | -------------------------- | ------------------------------------------- |
| `include` | Inclui outro template      | `{% include "navbar.html" %}`               |
| `extends` | Herda template pai         | `{% extends "base.html" %}`                 |
| `block`   | Define área sobrescrevível | `{% block content %}Conteúdo{% endblock %}` |

---

## Criando tags personalizadas (custom tags)

Tags personalizadas permitem **executar lógica no template**, indo além dos filtros.

### Estrutura

1. Crie uma pasta `templatetags` na sua app
2. Crie um arquivo Python para a tag, ex: `meutag.py`
3. Registre a tag usando `@register.simple_tag` ou `@register.tag`

---

### Tags simples

Tags simples **executam uma função e retornam valor**:

```python
from django import template

register = template.Library()

@register.simple_tag
def saudacao(nome):
    return f"Olá, {nome}!"
```

No template:

```html
{% load meutag %}
<p>{% saudacao "João" %}</p>  <!-- Saída: Olá, João! -->
```

---

### Tags com argumentos

Você pode passar **argumentos obrigatórios e opcionais**:

```python
@register.simple_tag
def multiplicar(a, b=2):
    return a * b
```

No template:

```html
{% multiplicar 5 3 %}  <!-- Saída: 15 -->
{% multiplicar 5 %}    <!-- Saída: 10 (usa b=2) -->
```

---

### Tags complexas

Para **blocos de template**, use `@register.tag` e crie uma classe parser:

```python
from django import template

register = template.Library()

class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return self.nodelist.render(context).upper()

@register.tag
def upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)
```

Uso no template:

```html
{% load meutag %}
{% upper %}
texto em minúsculas
{% endupper %}  <!-- Saída: TEXTO EM MINÚSCULAS -->
```

---

## Boas práticas

* Use tags **apenas quando necessário**
* Evite lógica complexa dentro do template
* Prefira filtros para **manipulação simples de valores**
* Documente tags personalizadas para manter a manutenção fácil

---

## Resumo

* Tags controlam fluxo, loops, herança e inclusão no template
* Tags embutidas: `if`, `for`, `include`, `block`, `extends`
* Tags personalizadas permitem funções e blocos customizados
* Tags simples retornam valores, tags complexas manipulam blocos

