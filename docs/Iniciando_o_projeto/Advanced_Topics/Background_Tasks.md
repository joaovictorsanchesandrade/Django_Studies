Tarefas em background são operações que **não precisam ser executadas imediatamente durante a requisição HTTP**, permitindo que a aplicação continue respondendo rapidamente ao usuário enquanto processos pesados são realizados em paralelo.

No Django, é comum utilizar **Celery** ou **Django Q** para gerenciar essas tarefas de forma eficiente e escalável.

---

## 1. Por que usar Background Tasks?

* **Melhora a performance da aplicação**: evita que requisições fiquem bloqueadas por processos longos.
* **Processa operações demoradas**: envio de e-mails, geração de relatórios, processamento de imagens, integração com APIs externas.
* **Permite escalabilidade**: tasks podem ser executadas em múltiplos workers, distribuídas entre servidores.

---

## 2. Celery – Gerenciador de Tarefas Assíncronas

O **Celery** é o gerenciador de tasks mais utilizado com Django. Ele permite executar tarefas de forma **assíncrona, agendada ou periódica**.

### 2.1 Instalação

```bash
pip install celery redis
```

> Redis é usado como broker de mensagens, mas RabbitMQ também é compatível.

---

### 2.2 Configuração Básica

```python
# projeto/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

app = Celery('projeto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

```python
# projeto/__init__.py
from .celery import app as celery_app

__all__ = ['celery_app']
```

---

### 2.3 Criando Tasks

```python
# myapp/tasks.py
from celery import shared_task
import time

@shared_task
def enviar_email(destinatario):
    time.sleep(5)  # simula envio de e-mail
    print(f"E-mail enviado para {destinatario}")
```

* `@shared_task` transforma a função em uma **task executável pelo Celery**.
* Pode ser chamada **de forma assíncrona** usando `enviar_email.delay('user@example.com')`.

---

### 2.4 Executando o Worker

```bash
celery -A projeto worker --loglevel=info
```

* O **worker** processa todas as tasks enfileiradas.
* O log mostra quando a task começa e termina.

---

### 2.5 Chamando Tasks Assíncronas

```python
from myapp.tasks import enviar_email

# Chamando de forma assíncrona
enviar_email.delay('user@example.com')
```

* `.delay()` envia a task para o **broker**, sem bloquear a requisição HTTP.

---

### 2.6 Tarefas Periódicas

Com Celery Beat, você pode executar tarefas periodicamente:

```python
# projeto/celery.py
from celery.schedules import crontab

app.conf.beat_schedule = {
    'limpar-cache-diariamente': {
        'task': 'myapp.tasks.limpar_cache',
        'schedule': crontab(hour=0, minute=0),
    },
}
```

* Executa `limpar_cache` todo dia à meia-noite.

---

## 3. Django Q – Alternativa Simples

O **Django Q** é outra opção para tasks assíncronas, mais fácil de configurar para projetos pequenos ou médios:

```bash
pip install django-q
```

* Configuração mínima no `settings.py`: define **broker e ORM**.
* Tasks podem ser chamadas com `async_task('myapp.tasks.minha_funcao', arg1, arg2)`.
* Suporta tasks agendadas, repetição e retries automáticos.

---

## 4. Boas Práticas

1. **Nunca execute tarefas pesadas diretamente na view** – use background tasks.
2. **Use brokers confiáveis** (Redis ou RabbitMQ) para produção.
3. **Defina tempo máximo de execução e retries** para tasks críticas.
4. **Monitore workers** e filas para evitar gargalos.
5. Combine com **caching e logging** para maior performance e rastreabilidade.

---

## 5. Exemplo Prático Integrado

```python
# views.py
from django.shortcuts import render
from myapp.tasks import enviar_email

def registrar_usuario(request):
    # lógica de registro...
    enviar_email.delay(request.user.email)  # envio de email em background
    return render(request, 'sucesso.html')
```

* O usuário recebe a resposta **imediatamente**, enquanto o e-mail é enviado em background.

---

## 6. Referências

* [Celery Documentation](https://docs.celeryq.dev/en/stable/)
* [Django Celery Integration](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)
* [Django Q Documentation](https://django-q.readthedocs.io/en/latest/)
* [Asynchronous Tasks in Django](https://docs.djangoproject.com/en/stable/topics/async/)

