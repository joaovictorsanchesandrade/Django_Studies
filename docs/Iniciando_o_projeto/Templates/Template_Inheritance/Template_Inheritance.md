# Template Inheritance (Herança de Templates)

## Sumário

1. [O que é Template Inheritance?](#o-que-é-template-inheritance)
2. [Por que usar Template Inheritance?](#por-que-usar-template-inheritance)
3. [Estrutura básica](#estrutura-básica)
   3.1 [Template Base](#template-base)
   3.2 [Template Filho](#template-filho)
4. [Tags principais](#tags-principais)
   4.1 [`{% extends %}`](#extends)
   4.2 [`{% block %}`](#block)
   4.3 [`{{ block.super }}`](#blocksuper)
5. [Herança em múltiplos níveis](#herança-em-múltiplos-níveis)
6. [Template Inheritance + Includes](#template-inheritance--includes)
7. [Erros comuns](#erros-comuns)
8. [Resumo](#resumo)
9. [Próximos tópicos](#próximos-tópicos)

---

## O que é Template Inheritance?

**Template Inheritance** é um recurso do Django que permite criar **templates filhos** que reutilizam a estrutura de um **template base**, sobrescrevendo apenas as partes necessárias. Isso evita duplicação de código e mantém o projeto organizado.

---

## Por que usar Template Inheritance?

* Evita repetição de código (DRY — *Don’t Repeat Yourself*)
* Facilita manutenção do layout
* Garante consistência visual entre páginas
* Torna o projeto mais escalável

---

## Estrutura básica

A herança de templates envolve dois elementos principais:

1. **Template base** → Define a estrutura principal da página
2. **Template filho** → Herda o base e altera apenas blocos específicos

---

### Template Base

Exemplo: `base.html`

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Meu Site{% endblock %}</title>
</head>
<body>

<header>
    <h1>Meu Site</h1>
</header>

<main>
    {% block content %}
    <!-- Conteúdo padrão -->
    {% endblock %}
</main>

<footer>
    <p>© 2026</p>
</footer>

</body>
</html>
```

---

### Template Filho

Exemplo: `home.html`

```html
{% extends "base.html" %}

{% block title %}
Home
{% endblock %}

{% block content %}
<h2>Página Inicial</h2>
<p>Bem-vindo ao site!</p>
{% endblock %}
```

---

## Tags principais

### `{% extends %}` <a id="extends"></a>

* Define qual template será herdado
* Deve ser **a primeira linha do arquivo**
* Só pode existir uma vez por template

```html
{% extends "base.html" %}
```

---

### `{% block %}` <a id="block"></a>

* Define áreas substituíveis
* Sintaxe:

```html
{% block nome_do_bloco %}
conteúdo
{% endblock %}
```

* Use nomes claros (`title`, `content`, `scripts`)
* Mantenha blocos pequenos e objetivos

---

### `{{ block.super }}` <a id="blocksuper"></a>

Permite acessar o conteúdo do bloco no template pai, útil para estender em vez de substituir:

```html
{% block content %}
{{ block.super }}
<p>Conteúdo adicional do template filho</p>
{% endblock %}
```

---

## Herança em múltiplos níveis

É possível criar templates que herdam outros templates filhos.

Exemplo de hierarquia:

```text
base.html
 └── layout.html
     └── page.html
```

#### layout.html

```html
{% extends "base.html" %}

{% block content %}
<div class="container">
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

#### page.html

```html
{% extends "layout.html" %}

{% block page_content %}
<h2>Conteúdo específico</h2>
{% endblock %}
```

---

## Template Inheritance + Includes

* `{% include %}` reutiliza **componentes pequenos**, enquanto herança define **layout**

```html
{% include "partials/navbar.html" %}
```

| Situação             | Recurso              |
| -------------------- | -------------------- |
| Layout base          | Template Inheritance |
| Componentes pequenos | `{% include %}`      |

---

## Erros comuns

* Esquecer `{% extends %}`
* Criar blocos fora da hierarquia
* Usar muitos níveis de herança sem necessidade
* Misturar lógica complexa nos templates

---

## Resumo

* Template Inheritance ajuda a **reutilizar layouts**
* `{% extends %}` define o template pai
* `{% block %}` cria áreas substituíveis
* `block.super` estende conteúdo do pai
* Suporta herança em múltiplos níveis
* Funciona bem com `{% include %}`

---

## Próximos tópicos

1. [Variables](Variables.md)
2. [Filters & custom filters](Filters_custom_filters.md)
3. [Tags & custom tags](Tags_custom_tags.md)

