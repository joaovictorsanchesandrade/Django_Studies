O Django, a partir da versão 3.0, passou a oferecer **suporte nativo a operações assíncronas**, permitindo construir aplicações mais **performáticas e escaláveis**, especialmente para tarefas que envolvem **I/O intensivo**, como requisições HTTP externas, WebSockets ou chamadas de banco de dados assíncronas.

---

## 1. Conceitos Básicos

* **Síncrono (Sync)** – execução bloqueante. Cada requisição espera a anterior terminar antes de ser processada.
* **Assíncrono (Async)** – execução não bloqueante. Requisições podem ser processadas simultaneamente, liberando recursos durante operações de I/O.
* Django agora suporta **views, middleware e ORM assíncronos**.

---

## 2. Views Assíncronas

Você pode definir uma **view assíncrona** usando `async def`:

```python
# myapp/views.py
from django.http import JsonResponse
import asyncio

async def async_hello(request):
    await asyncio.sleep(2)  # simula operação de I/O
    return JsonResponse({'message': 'Olá do Django assíncrono!'})
```

* Requisições **não bloqueiam** o servidor enquanto `asyncio.sleep` está ativo.
* Ideal para **chamadas externas ou tarefas demoradas**.

---

## 3. Middleware Assíncrono

Middleware também pode ser assíncrono:

```python
# myapp/middleware.py
class AsyncMiddleware:
    async def __call__(self, request, get_response):
        response = await get_response(request)
        response['X-Async'] = 'True'
        return response
```

* Middleware assíncrono permite **processamento paralelo de requisições**.
* Deve ser compatível com o **ASGI server** (como Daphne ou Uvicorn).

---

## 4. ORM Assíncrono (Experimental)

Django 4.x permite executar **consultas assíncronas ao banco de dados**:

```python
from myapp.models import Produto

async def lista_produtos_async(request):
    produtos = await Produto.objects.all().aget(id=1)
    return JsonResponse({'produto': produtos.nome})
```

* Ainda limitado: nem todos os métodos do ORM são assíncronos.
* Principal vantagem: **não bloquear o event loop** em operações de I/O pesado.

---

## 5. WebSockets com Django Channels

Para comunicação em tempo real, use **Django Channels**, que adiciona suporte ASGI:

```python
# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({'message': data['message']}))
```

* Permite criar **chat, notificações em tempo real ou streaming de dados**.
* Funciona em conjunto com **ASGI servers**.

---

## 6. Tasks Assíncronas com Celery

Embora Django suporte async, para **tarefas de background e processamento pesado**, recomenda-se usar **Celery**:

```python
# tasks.py
from celery import shared_task
import time

@shared_task
def tarefa_demorada(x, y):
    time.sleep(10)
    return x + y
```

* Celery permite **executar tarefas fora do request/response cycle**, melhorando performance.
* Ideal para **envio de e-mails, geração de relatórios ou integrações externas**.

---

## 7. Configuração do ASGI

Para rodar Django assíncrono, configure **ASGI** no projeto:

```python
# projeto/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

application = get_asgi_application()
```

* Para WebSockets ou Channels:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myapp.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
```

---

## 8. Boas Práticas

1. Use **async apenas onde necessário** – operações CPU-bound não ganham performance.
2. Combine **views assíncronas com I/O-bound tasks** (APIs externas, WebSockets).
3. Use **ASGI servers** como Daphne ou Uvicorn para tirar proveito do async.
4. Continue usando **middleware e ORM síncronos** quando compatível para simplicidade.
5. Para **tarefas demoradas ou batch**, prefira **Celery ou background workers**.

---

## 9. Referências

* [Django Async Views Documentation](https://docs.djangoproject.com/en/stable/topics/async/)
* [Django Channels Documentation](https://channels.readthedocs.io/en/stable/)
* [ASGI Reference](https://asgi.readthedocs.io/en/latest/)
* [Celery Documentation](https://docs.celeryq.dev/en/stable/)

