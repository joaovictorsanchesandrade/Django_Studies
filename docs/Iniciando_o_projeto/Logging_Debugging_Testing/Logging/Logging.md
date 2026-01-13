O **logging** é uma ferramenta essencial para qualquer aplicação Django. Ele permite **registrar eventos**, **erros**, **alertas** e **informações importantes** sobre o funcionamento do sistema, facilitando **depuração, monitoramento e manutenção**.

O Django utiliza o módulo **`logging` do Python**, oferecendo integração completa com **Loggers**, **Handlers**, **Filters** e **Formatters**. Cada um desses componentes possui uma função específica no fluxo de registro de logs.

---

## 1. Fluxo de Logging

O fluxo básico de logging no Django é:

```
Logger -> Filter -> Handler -> Formatter -> Saída (console, arquivo, email, etc.)
```

* **Logger**: cria e registra mensagens de log.
* **Filter**: filtra quais mensagens devem ser processadas.
* **Handler**: decide para onde a mensagem será enviada.
* **Formatter**: define o formato final da mensagem.

---

## 2. Componentes do Logging

### [Loggers](Loggers.md)

* Responsáveis por **gerar mensagens de log** dentro da aplicação.
* Podem ser **por módulo ou por app**, facilitando organização.
* Possuem **níveis de gravidade** como `DEBUG`, `INFO`, `WARNING`, `ERROR` e `CRITICAL`.
* Exemplo de uso:

```python
import logging
logger = logging.getLogger(__name__)
logger.info("Mensagem de informação")
```

---

### [Handlers](Handlers.md)

* Determinam **para onde as mensagens de log serão enviadas**.
* Exemplos: console, arquivos, e-mails ou serviços externos.
* Podem ser **compartilhados entre loggers** para diferentes saídas.
* Exemplo de configuração:

```python
'handlers': {
    'console': {'class': 'logging.StreamHandler'},
    'arquivo': {'class': 'logging.FileHandler', 'filename': 'meu_log.log'},
}
```

---

### [Filters](Filters.md)

* Aplicam **regras adicionais para selecionar quais logs passam**.
* Podem filtrar por módulo, app, nível ou condições personalizadas.
* Exemplo de uso:

```python
'filters': {
    'somente_app_usuarios': {
        '()': 'django.utils.log.CallbackFilter',
        'callback': lambda record: record.name.startswith('usuarios'),
    },
}
```

---

### [Formatters](Formatters.md)

* Definem **o formato final das mensagens de log**.
* Permitem incluir informações como **timestamp**, **nível**, **logger**, **módulo** e **mensagem**.
* Exemplo de configuração:

```python
'formatters': {
    'detalhado': {
        'format': '{asctime} {levelname} {name} {module} {message}',
        'style': '{',
    },
}
```

---

## 3. Boas Práticas de Logging no Django

1. **Use loggers em vez de `print()`** para depuração.
2. **Escolha nomes claros** para loggers, de preferência por app ou módulo.
3. **Combine Handlers, Filters e Formatters** para controle completo sobre os logs.
4. **Não registre informações sensíveis** (senhas, dados pessoais).
5. **Use diferentes níveis de log** para diferenciar mensagens críticas de informativas.
6. **Mantenha logs claros e legíveis**, especialmente em produção.

---

Este arquivo funciona como **guia central do sistema de logging no Django**, com links para arquivos detalhados de cada componente:

1. [Loggers](Loggers.md) – Criar e registrar mensagens.
2. [Handlers](Handlers.md) – Definir destinos das mensagens.
3. [Filters](Filters.md) – Selecionar quais mensagens passam.
4. [Formatters](Formatters.md) – Definir o formato final das mensagens.

