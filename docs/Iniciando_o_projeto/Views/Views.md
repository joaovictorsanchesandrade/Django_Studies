No Django, **as views são o coração do projeto**.
Elas são responsáveis por **receber a requisição do usuário**, **processar a lógica necessária** e **retornar uma resposta HTTP**.

Toda interação entre o usuário e o sistema **passa obrigatoriamente por uma view**.

---

## O que é uma View?

Uma **view** é uma **função ou classe Python** que segue um fluxo bem definido:

1. Recebe uma **request** (requisição HTTP)
2. Executa a **lógica de negócio**
3. Retorna uma **response** (resposta HTTP)

Independentemente do que aconteça durante o processamento, **uma view sempre deve retornar uma resposta HTTP**.

Por exemplo:

* Se o usuário não tem permissão → a view retorna **403 Forbidden**
* Se o recurso não existe → **404 Not Found**
* Se ocorrer um erro interno → **500 Internal Server Error**

A view **nunca pode “parar no meio”** sem retornar uma resposta.

---

## Tipos de Views no Django

O Django oferece diferentes formas de implementar views, cada uma adequada a um nível de complexidade diferente:

1. [Function-Based Views (FBV)](Function_based_views.md)
2. [Class-Based Views (CBV)](Class_based_views.md)
3. [Generic Views](Generic_views/Generic_views.md)

Cada abordagem existe para resolver **problemas diferentes**, e um bom desenvolvedor sabe **quando usar cada uma**.

