Os **Middlewares** no Django permitem interceptar e modificar o fluxo **request → response** globalmente.
A customização de middlewares possibilita aplicar **regras transversais** à aplicação, como segurança, logging, autenticação, auditoria e tratamento de erros.

Este documento aborda como **criar, configurar e customizar middlewares** de forma correta e profissional.

---

## O Que é um Middleware?

Um middleware é uma **camada intermediária** entre:

* a requisição (`HttpRequest`)
* a view
* a resposta (`HttpResponse`)

Fluxo simplificado:

```text
Request → Middleware → View → Middleware → Response
```

---

## Quando Criar um Middleware Customizado?

Use um middleware quando a lógica:

* deve ser aplicada a **todas ou várias views**
* não pertence a um model ou view específica
* é transversal (cross-cutting concerns)

Exemplos:

* autenticação global
* logs de requisição
* controle de acesso
* headers de segurança
* rate limiting
* auditoria

---

## Criando um Middleware Customizado

Estrutura básica:

```python
class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
```

---

## Registrando o Middleware

Adicionar em `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'core.middleware.ExampleMiddleware',
]
```

📌 A ordem importa.

---

## Trabalhando com Request

```python
def __call__(self, request):
    request.start_time = time.time()
    return self.get_response(request)
```

---

## Trabalhando com Response

```python
response['X-App-Version'] = '1.0.0'
return response
```

---

## Interceptando Antes da View

```python
def __call__(self, request):
    if not request.user.is_authenticated:
        return redirect('login')
    return self.get_response(request)
```

---

## Hooks Avançados de Middleware

### `process_view`

Executa antes da view:

```python
def process_view(self, request, view_func, view_args, view_kwargs):
    pass
```

---

### `process_exception`

Captura exceções:

```python
def process_exception(self, request, exception):
    log_error(exception)
```

---

### `process_template_response`

Modifica template responses:

```python
def process_template_response(self, request, response):
    response.context_data['app_name'] = 'MyApp'
    return response
```

---

## Middleware Baseado em Função

```python
def simple_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        return response

    return middleware
```

---

## Middleware para Logging

```python
class RequestLogMiddleware:

    def __call__(self, request):
        print(request.path)
        return self.get_response(request)
```

---

## Middleware de Segurança

Exemplo: bloqueio por IP

```python
class IPBlockMiddleware:

    def __call__(self, request):
        if request.META['REMOTE_ADDR'] in BLACKLIST:
            return HttpResponseForbidden()
        return self.get_response(request)
```

---

## Middleware e Performance

⚠️ Cuidados:

* código executa em todas as requisições
* evite queries no middleware
* não faça lógica pesada
* use cache quando possível

---

## Boas Práticas

* Crie middlewares pequenos e específicos
* Nomeie claramente
* Documente o propósito
* Teste com cuidado
* Controle a ordem no `MIDDLEWARE`

---

## Erros Comuns

* Middleware muito genérico
* Lógica de negócio no middleware
* Ordem incorreta no `MIDDLEWARE`
* Exceções não tratadas

---

## Quando NÃO Usar Middleware?

❌ Lógica específica de uma view
❌ Regras de negócio complexas
❌ Processamento pesado
❌ Validação de formulário

Nestes casos, use views, services ou signals.

---

## Middleware vs Decorators

| Situação             | Melhor Opção |
| -------------------- | ------------ |
| Regra global         | Middleware   |
| Regra por view       | Decorator    |
| Autenticação global  | Middleware   |
| Permissão específica | Decorator    |

---

## Conclusão

A customização de middlewares permite implementar **comportamentos globais, seguros e reutilizáveis** no Django.

Quando usados corretamente, middlewares aumentam a **organização, segurança e manutenção** do projeto.

