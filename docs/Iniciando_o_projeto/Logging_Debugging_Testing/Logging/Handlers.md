No Django, um **Handler** é o componente responsável por **decidir para onde as mensagens registradas por um Logger serão enviadas**. Enquanto o Logger apenas registra uma mensagem, o Handler define se ela vai para o **console**, um **arquivo**, um **e-mail** ou outro destino.

O Django integra o sistema de logging do Python, então todos os handlers seguem a mesma lógica do módulo `logging`.

---

## 1. Função de um Handler

Um **Handler** atua como um canal entre o Logger e a saída final da mensagem de log. Ele permite:

* Enviar logs para múltiplos destinos ao mesmo tempo.
* Filtrar logs por nível ou condição.
* Transformar a mensagem antes de enviá-la usando um Formatter.

Exemplo de fluxo:

```
Logger -> Handler -> Saída (Console, Arquivo, Email, etc.)
```

---

## 2. Tipos Comuns de Handlers

O Django oferece suporte a diversos tipos de handlers nativos do Python:

| Handler                    | Descrição                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| `StreamHandler`            | Envia logs para o console ou qualquer stream (ex.: `sys.stdout`).                               |
| `FileHandler`              | Escreve logs em arquivos.                                                                       |
| `RotatingFileHandler`      | Arquivos de log que rodam automaticamente quando atingem tamanho limite.                        |
| `TimedRotatingFileHandler` | Roda arquivos de log com base em tempo (diário, semanal etc.).                                  |
| `AdminEmailHandler`        | Envia logs de nível `ERROR` ou superior para os administradores definidos no Django (`ADMINS`). |
| `NullHandler`              | Descartar logs sem gerar saída (útil para bibliotecas).                                         |

---

## 3. Exemplo de Handlers no Django

No arquivo `settings.py`, os handlers são configurados dentro do dicionário `LOGGING`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'arquivo': {
            'class': 'logging.FileHandler',
            'filename': 'meu_log.log',
        },
        'email_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'arquivo'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### Explicando:

* `'console'`: envia logs para o terminal.
* `'arquivo'`: escreve logs em `meu_log.log`.
* `'email_admins'`: envia logs de nível `ERROR` ou superior para os administradores cadastrados no `settings.ADMINS`.

---

## 4. Boas Práticas com Handlers

1. **Use múltiplos handlers quando necessário**: é comum enviar logs para console em desenvolvimento e para arquivos em produção.
2. **Combine com formatters** para definir o formato da mensagem de saída.
3. **Escolha o handler certo para cada situação**:

   * Console → depuração local.
   * Arquivo → histórico de logs.
   * Email → alertas críticos.
4. **Não use FileHandler em produção sozinho** para grandes sistemas; prefira RotatingFileHandler ou serviços externos de logging.
5. **Handlers podem ser compartilhados entre loggers**, permitindo centralização e consistência na saída de logs.

---

## 5. Exemplo Prático com Múltiplos Handlers

```python
import logging

logger = logging.getLogger('meu_app')

logger.info("Mensagem enviada para console e arquivo")
logger.error("Mensagem enviada para console, arquivo e email (se configurado)")
```

> Nesse exemplo, dependendo da configuração, a mesma mensagem pode ir para **vários destinos** simultaneamente.

