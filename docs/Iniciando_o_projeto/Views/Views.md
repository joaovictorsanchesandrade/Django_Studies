No Django s views são o coração do projeto ela recebe a requisição do usuário processa os dados e depois devolve uma resposta.

# O que é uma view?
Um view é uma função ou classe python que:
1. Recebe uma request (requisição HTTP)
2. Executa alguma logica
3. Retorna uma respose (Resposta http)

Indenpente do que ocorrer uma View sempre deve retorna uma resposta em HTTP, digamos que o usuario não tem permissão de fazer aquilo, a view deve retorna uma resposta informando isso, e isso para tudo.

---

1. [Function-based views](Function_based_views.md)
2. [Class-based views](Class_based_views.md)
3. [Generic views](Generic_views/Generic_views.md)