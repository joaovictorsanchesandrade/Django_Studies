Os **Middlewares** no Django são componentes que interceptam o fluxo **request → response** da aplicação.
Eles permitem executar lógica **global e transversal**, sem acoplar regras diretamente às views ou models.

Este módulo apresenta os conceitos fundamentais de middleware, seus usos reais e como customizá-los corretamente.

---

## O Que é um Middleware?

Um middleware é uma camada que envolve o processamento da requisição e da resposta:

```text
Request → Middleware → View → Middleware → Response
```

Ele pode:

* modificar a request
* interromper o fluxo
* alterar a response
* capturar exceções
* adicionar headers
* aplicar regras globais

---

## Quando Usar Middleware?

Use middleware quando a lógica:

* deve rodar em **todas ou várias requisições**
* não pertence a uma view específica
* é transversal à aplicação

Exemplos comuns:

* autenticação global
* autorização
* logs e auditoria
* segurança (headers, IP, rate limit)
* tracking de requisições
* manutenção do sistema

---

## Quando NÃO Usar Middleware?

* ❌ Regras específicas de uma view
* ❌ Validação de formulários
* ❌ Lógica de negócio
* ❌ Processamentos pesados

Nestes casos, use views, services, decorators ou signals.

---

## Ordem dos Middlewares

A ordem definida em `settings.py` é **crítica**:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'core.middleware.CustomMiddleware',
]
```

📌 Middlewares são executados:

* na request: de cima para baixo
* na response: de baixo para cima

---

## Middlewares Nativos do Django

Alguns exemplos importantes:

* `SecurityMiddleware`
* `AuthenticationMiddleware`
* `SessionMiddleware`
* `CsrfViewMiddleware`
* `CommonMiddleware`

Eles já cobrem muitos casos de uso comuns.

---

## Estrutura do Módulo

Este tópico está organizado de forma progressiva:

### Conteúdos

1. **[Customization](Customization.md)**
   Criação e customização de middlewares próprios.
   Aborda interceptação de request/response, hooks avançados, performance e boas práticas.

---

## Boas Práticas

* Crie middlewares pequenos e bem definidos
* Evite lógica pesada
* Documente o propósito
* Controle a ordem no `MIDDLEWARE`
* Teste cuidadosamente
* Monitore performance

---

## Erros Comuns

* Usar middleware para tudo
* Ordem incorreta no `MIDDLEWARE`
* Excesso de lógica global
* Queries no middleware
* Falta de tratamento de exceções

---

## Middleware em Projetos Reais

Em aplicações reais, middlewares são usados para:

* segurança
* observabilidade
* controle de acesso
* logging
* rate limiting
* feature flags

Quando bem utilizados, deixam o código **mais limpo e organizado**.

---

## Conclusão

Os middlewares são uma ferramenta poderosa para aplicar **comportamentos globais** no Django.
Usados com critério, eles aumentam a **segurança, organização e escalabilidade** da aplicação.

