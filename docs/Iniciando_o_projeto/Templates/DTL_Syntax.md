O **Django Template Language (DTL)** é a linguagem usada pelo Django para renderizar HTML de forma dinâmica.
Ele funciona como uma **ponte entre os dados da view e a interface**, permitindo exibir informações sem misturar lógica de negócio com apresentação.

---

## 1. Conceitos Fundamentais

Um template Django **não é Python**.
Ele é apenas um arquivo de texto (normalmente HTML) que contém **marcadores especiais** que o Django interpreta no momento da renderização.

Fluxo real:

1. O usuário faz uma requisição
2. A *view* processa os dados
3. A *view* envia um **contexto** para o template
4. O template renderiza o HTML final

📌 O template **nunca** deve decidir regras de negócio.

---

## 2. Variáveis

Variáveis são usadas para **exibir dados** que vêm da *view*.

```html
{{ titulo }}
```

### O que acontece aqui:

* `titulo` vem do dicionário de contexto
* O Django substitui `{{ titulo }}` pelo valor real
* Se não existir, nada é exibido (sem erro)

---

### Acesso a atributos

```html
{{ user.username }}
```

* `user` é um objeto
* `username` é um atributo
* O DTL tenta:

  1. Atributo
  2. Método sem argumentos
  3. Chave de dicionário

---

### Acesso a dicionários

```html
{{ dados.nome }}
{{ dados['nome'] }}
```

Ambas funcionam, mas a notação com ponto é a mais comum.

---

## 3. Tags de Controle

Tags controlam **fluxo, estrutura e comportamento** do template.
São escritas com `{% %}`.

---

## 3.1 `if / elif / else`

```html
{% if user.is_authenticated %}
```

### O que isso faz:

* Avalia uma condição booleana
* Se for verdadeira, renderiza o bloco

Operadores permitidos:

* Lógicos: `and`, `or`, `not`
* Comparação: `==`, `!=`, `<`, `>`
* Pertencimento: `in`, `not in`

📌 Não existe `try/except`, nem lógica complexa.

---

## 3.2 `for`

```html
{% for produto in produtos %}
```

### Funcionamento:

* `produtos` é uma lista enviada pela view
* `produto` representa cada item da lista
* O bloco roda uma vez por item

---

### Variáveis internas do loop

```html
{{ forloop.counter }}
```

Essas variáveis ajudam no controle visual:

* `counter`: começa em 1
* `counter0`: começa em 0
* `first`: primeiro item
* `last`: último item

---

### `empty`

```html
{% empty %}
```

Executa quando a lista está vazia — evita `if` desnecessário.

---

## 3.3 `with`

```html
{% with total=produtos|length %}
```

### Por que usar:

* Evita repetir expressões longas
* Melhora legibilidade
* Cria variáveis temporárias

📌 A variável só existe dentro do bloco.

---

## 4. Filtros

Filtros **modificam a saída** de uma variável antes de exibir.

```html
{{ nome|upper }}
```

### O que acontece:

* `nome` é passado para o filtro
* O filtro retorna um novo valor
* O template exibe o resultado

---

### Filtros com argumentos

```html
{{ texto|truncatewords:10 }}
```

* `10` é um argumento
* Controla o comportamento do filtro

---

### Encadeamento

```html
{{ nome|lower|capfirst }}
```

Cada filtro recebe o resultado do anterior.

---

## 5. Tags Estruturais

---

## 5.1 `extends`

```html
{% extends "base.html" %}
```

### O que faz:

* Diz que este template herda outro
* Tudo vem do `base.html`
* Apenas os blocos sobrescritos mudam

📌 Deve ser a primeira linha do arquivo.

---

## 5.2 `block`

```html
{% block content %}
```

### Função:

* Define áreas editáveis
* Permite reutilizar layouts
* Evita repetição de HTML

---

## 5.3 `include`

```html
{% include "components/navbar.html" %}
```

### Uso:

* Importa outro template
* Ideal para componentes reutilizáveis
* Mantém código organizado

---

## 5.4 `load`

```html
{% load static %}
```

### O que faz:

* Carrega bibliotecas de tags
* Necessário para usar `static`
* Também usado para filtros customizados

---

## 6. Arquivos Estáticos

```html
{% static 'css/style.css' %}
```

### Por que usar:

* Resolve caminho correto dos arquivos
* Funciona em produção e desenvolvimento
* Evita paths hardcoded

---

## 7. Comentários

```html
{# comentário #}
```

* Não aparece no HTML final
* Não é enviado ao navegador
* Ideal para documentação interna

---

## 8. Escape e Segurança

Por padrão:

```html
{{ conteudo }}
```

* HTML é escapado
* Evita XSS

---

### `safe`

```html
{{ conteudo|safe }}
```

* Renderiza HTML bruto
* **Perigoso se vier do usuário**

📌 Só use quando tiver certeza da origem.

---

## 9. Valores Padrão

```html
{{ variavel|default:"N/A" }}
```

Evita:

* Campos vazios
* Templates quebrados
* Condições extras

---

## 10. Limitações do DTL

O DTL **não permite**:

* Executar Python
* Criar funções
* Manipular banco
* Importar módulos

📌 Isso é uma decisão de design para manter segurança.

---

## 11. Boas Práticas

* Templates são para exibir, não decidir
* Views preparam os dados
* Use herança sempre
* Evite lógica dentro do HTML

---

## Conclusão

O **DTL** é simples por design, mas extremamente poderoso quando bem usado.
Entender **cada campo e cada tag** garante templates limpos, seguros e profissionais — exatamente como o Django espera.

