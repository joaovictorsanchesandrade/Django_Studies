No Django, um **Logger** é o objeto responsável por registrar mensagens de log dentro da aplicação. Ele permite que você capture informações sobre o fluxo do sistema, erros e eventos importantes de forma organizada e controlada.

O Django utiliza o **módulo `logging` do Python**, então toda a lógica de loggers segue a mesma estrutura do Python, mas integrada à configuração do Django.

---

## 1. Criando um Logger

Para usar um logger, basta importar o módulo `logging` e criar um logger com `getLogger(nome)`:

```python
import logging

# Cria um logger com o nome do módulo
logger = logging.getLogger(__name__)
```

> `__name__` é usado para nomear o logger de acordo com o módulo atual. Isso ajuda a identificar a origem da mensagem no log.

---

## 2. Registrando Mensagens

Os loggers possuem métodos para cada **nível de gravidade**:

```python
logger.debug("Mensagem de debug")
logger.info("Mensagem informativa")
logger.warning("Mensagem de aviso")
logger.error("Mensagem de erro")
logger.critical("Mensagem crítica")
```

### Níveis de gravidade:

| Nível      | Descrição                                     |
| ---------- | --------------------------------------------- |
| `DEBUG`    | Detalhes para depuração                       |
| `INFO`     | Informações gerais sobre o fluxo da aplicação |
| `WARNING`  | Avisos sobre situações inesperadas            |
| `ERROR`    | Erros que não interrompem a execução          |
| `CRITICAL` | Erros graves que podem quebrar a aplicação    |

---

## 3. Logger por App ou Módulo

É recomendável criar **loggers específicos para cada app ou módulo**. Isso ajuda a filtrar mensagens e identificar problemas rapidamente.

Exemplo dentro de um app chamado `usuarios`:

```python
# usuarios/views.py
import logging

logger = logging.getLogger('usuarios')

def listar_usuarios(request):
    logger.info("Listando usuários")
    return HttpResponse("Usuários listados")
```

---

## 4. Boas Práticas com Loggers

1. **Sempre use loggers**, não `print()`.
2. **Nomeie loggers por módulo ou app** para facilitar identificação.
3. **Escolha corretamente o nível de log** de acordo com a importância da mensagem.
4. **Evite logar informações sensíveis**, como senhas ou dados pessoais.
5. **Use loggers para rastrear eventos importantes**, não para cada linha de código.

---

## 5. Exemplo Prático

```python
import logging

logger = logging.getLogger(__name__)

def processar_pedido(pedido):
    logger.info(f"Iniciando processamento do pedido {pedido.id}")
    try:
        # lógica do processamento
        resultado = pedido.valor / pedido.quantidade
        logger.debug(f"Resultado do cálculo: {resultado}")
    except ZeroDivisionError:
        logger.error("Erro: divisão por zero no pedido", exc_info=True)
```

> Aqui, o logger permite rastrear o fluxo e registrar erros com detalhes, mantendo o código limpo e organizado.

