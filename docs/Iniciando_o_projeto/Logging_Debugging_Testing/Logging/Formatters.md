No Django, um **Formatter** é o componente do sistema de logging responsável por **definir como as mensagens de log serão exibidas**. Ele determina o **formato final da mensagem** que será enviada por um Handler para a saída (console, arquivo, e-mail, etc.).

Enquanto **Loggers** geram mensagens, **Handlers** definem onde elas vão, e **Filters** selecionam quais passam, o **Formatter** define **como elas aparecem**.

---

## 1. Função de um Formatter

O Formatter permite:

* Adicionar informações como **timestamp**, **nível do log**, **nome do logger** e **mensagem**.
* Padronizar a aparência dos logs em toda a aplicação.
* Facilitar leitura e análise, especialmente quando se usam arquivos ou sistemas de monitoramento.

Exemplo de fluxo:

```
Logger -> Filter -> Handler -> Formatter -> Saída
```

---

## 2. Criando um Formatter no Django

No Django, os formatters são configurados no dicionário `LOGGING` dentro de `settings.py`.

Exemplo básico:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simples': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'detalhado': {
            'format': '{asctime} {levelname} {name} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detalhado',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### Explicando:

* **`simples`**: formato enxuto, mostrando apenas o nível e a mensagem.
* **`detalhado`**: inclui **timestamp**, **nível**, **nome do logger**, **módulo** e a mensagem completa.
* **`style`**: define a sintaxe usada (`'{'` para `.format()`, `'%'` para `%` e `'$'` para `string.Template`).

---

## 3. Campos Comuns em Formatters

Você pode usar vários campos predefinidos no Python Logging:

| Campo       | Descrição                        |
| ----------- | -------------------------------- |
| `asctime`   | Timestamp do log                 |
| `levelname` | Nível do log (DEBUG, INFO, etc.) |
| `name`      | Nome do logger                   |
| `module`    | Módulo de origem da mensagem     |
| `filename`  | Nome do arquivo de origem        |
| `funcName`  | Nome da função que chamou o log  |
| `lineno`    | Número da linha                  |
| `message`   | Mensagem do log                  |

Exemplo:

```python
'format': '{asctime} | {levelname} | {name} | {funcName}:{lineno} | {message}'
```

> Resultado típico:
> `2026-01-12 22:15:00 | INFO | usuarios | listar_usuarios:15 | Usuário logado com sucesso`

---

## 4. Boas Práticas com Formatters

1. **Use formatos claros e consistentes** em toda a aplicação.
2. **Inclua timestamps** para facilitar rastreamento de eventos.
3. **Inclua nome do logger ou módulo** para identificar a origem do log.
4. **Evite mensagens excessivamente longas** em logs críticos.
5. **Crie diferentes formatters** para desenvolvimento e produção:

   * Desenvolvimento → mais detalhado para depuração.
   * Produção → mais resumido e fácil de ler.

---

## 5. Exemplo Prático

```python
import logging

logger = logging.getLogger('usuarios')

logger.info("Usuário realizou login")
logger.warning("Usuário tentou acessar página restrita")
```

Se o formatter detalhado estiver configurado, o console pode exibir:

```
2026-01-12 22:20:00 INFO usuarios views 42 Usuário realizou login
2026-01-12 22:20:05 WARNING usuarios views 45 Usuário tentou acessar página restrita
```

> Assim, cada log contém **informações completas** para análise rápida e depuração.

