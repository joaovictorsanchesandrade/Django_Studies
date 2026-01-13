No Django, um **Filter** é um componente do sistema de logging que permite **controlar quais mensagens um Logger ou Handler deve processar**. Ele atua como um **filtro condicional**, decidindo se uma mensagem deve ser registrada ou descartada.

Enquanto **Loggers** registram mensagens e **Handlers** definem para onde elas vão, os **Filters** determinam **quais mensagens passam**.

---

## 1. Função de um Filter

Filters permitem:

* Selecionar logs com base em critérios específicos (nível, módulo, usuário etc.).
* Aplicar regras adicionais antes que a mensagem chegue ao Handler.
* Evitar que logs desnecessários poluam a saída.

Exemplo de fluxo:

```
Logger -> Filter -> Handler -> Saída
```

---

## 2. Usando Filters no Django

Filters podem ser definidos de duas maneiras:

1. **Filtros padrão do Python**
   O Python fornece uma classe base `logging.Filter` que pode ser estendida.

2. **Filtros inline na configuração do Django**
   Você pode usar filtros diretamente no dicionário `LOGGING` em `settings.py`.

---

### 2.1. Filtro Simples (por Nome)

```python
# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'somente_app_usuarios': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: record.name.startswith('usuarios'),
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['somente_app_usuarios'],
        },
    },
    'loggers': {
        'usuarios': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

> Nesse exemplo, apenas logs do logger `'usuarios'` passarão pelo handler `'console'`.

---

### 2.2. Criando um Filter Personalizado

Você pode criar filtros mais complexos definindo uma classe que estenda `logging.Filter`:

```python
import logging

class UsuarioAtivoFilter(logging.Filter):
    def filter(self, record):
        # Exemplo: registrar apenas logs se o usuário estiver ativo
        # (record.user precisa ser adicionado manualmente ao Logger)
        return getattr(record, 'user_is_active', False)
```

E usar no `settings.py`:

```python
'filters': {
    'usuario_ativo': {
        '()': 'meu_app.logging.UsuarioAtivoFilter',
    },
},
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
        'filters': ['usuario_ativo'],
    },
},
```

> Agora, apenas registros que passarem pelo filtro serão enviados para o console.

---

## 3. Boas Práticas com Filters

1. **Use filters para reduzir ruído** em grandes aplicações.
2. **Combine filters com handlers e loggers** para um controle mais refinado.
3. **Evite lógica pesada dentro do filter**, pois ele é chamado a cada log e pode impactar performance.
4. **Filtros podem ser reutilizados** em múltiplos handlers ou loggers.
5. **Filtros não substituem níveis de log**; eles apenas adicionam critérios extras para selecionar mensagens.

---

## 4. Exemplo Prático

```python
import logging

logger = logging.getLogger('usuarios')

# Simulando um registro com atributo customizado
extra = {'user_is_active': True}

logger.info("Usuário ativo fez login", extra=extra)
logger.info("Usuário inativo tentou login", extra={'user_is_active': False})
```

> Somente a primeira mensagem passará pelo filtro `UsuarioAtivoFilter` e será exibida no console.

