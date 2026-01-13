As **signals** no Django são um mecanismo que permite **disparar ações automaticamente** em resposta a eventos específicos do framework, sem acoplar diretamente o código. Elas são amplamente usadas para **manter a separação de responsabilidades** e criar funcionalidades reativas.

---

## 1. Conceito de Signals

* Uma **signal** é um **evento disparado pelo Django** ou pelo próprio código do desenvolvedor.
* Um **receiver** (ou handler) é uma função que **escuta** essa signal e executa uma ação quando ela ocorre.
* Exemplo: criar automaticamente um perfil de usuário quando um `User` é criado.

---

## 2. Signals Integradas do Django

O Django fornece várias **signals nativas**, como:

| Signal             | Descrição                                                   |
| ------------------ | ----------------------------------------------------------- |
| `pre_save`         | Disparada antes de um objeto ser salvo.                     |
| `post_save`        | Disparada depois que um objeto é salvo.                     |
| `pre_delete`       | Disparada antes de um objeto ser deletado.                  |
| `post_delete`      | Disparada depois que um objeto é deletado.                  |
| `m2m_changed`      | Disparada quando um relacionamento many-to-many é alterado. |
| `request_started`  | Disparada quando uma requisição HTTP começa.                |
| `request_finished` | Disparada quando uma requisição HTTP termina.               |

---

## 3. Criando um Receiver

Para criar um **receiver**, utilize o decorator `@receiver` ou conecte manualmente a função à signal.

### 3.1 Usando `@receiver`

```python
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from myapp.models import Perfil

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
```

* `sender` define o modelo que dispara a signal.
* `created` indica se o objeto foi criado (True) ou atualizado (False).
* `**kwargs` captura informações adicionais da signal.

---

### 3.2 Conectando manualmente

```python
from django.db.models.signals import post_save
from myapp.signals import criar_perfil_usuario
from django.contrib.auth.models import User

post_save.connect(criar_perfil_usuario, sender=User)
```

* Útil quando não se deseja usar decorators ou precisa conectar dinamicamente.

---

## 4. Signals e Aplicações Reais

Alguns exemplos de uso:

1. **Criação automática de perfil de usuário** – cria objetos relacionados quando o usuário é registrado.
2. **Atualização de cache** – limpa ou atualiza cache quando um objeto é modificado.
3. **Logs automáticos** – registra alterações no banco de dados sem alterar o fluxo principal.
4. **Envio de notificações** – envia e-mails ou push notifications após ações do usuário.
5. **Controle de integridade de dados** – validações ou ajustes adicionais após save/delete.

---

## 5. Boas Práticas com Signals

1. **Evite lógica pesada em signals** – prefira delegar para tasks assíncronas (ex: Celery).
2. **Documente bem** – signals podem dificultar o rastreio de fluxo de execução.
3. **Use `post_save` para ações dependentes de IDs gerados** (o `pre_save` ainda não possui o ID do objeto).
4. **Desconecte receivers se necessário** – útil em testes para evitar efeitos colaterais.
5. **Combine com logging** para monitorar quando signals são disparadas.

---

## 6. Testando Signals

```python
from django.test import TestCase
from django.contrib.auth.models import User
from myapp.models import Perfil

class SignalTest(TestCase):
    def test_criar_perfil(self):
        user = User.objects.create_user(username='joao', password='123')
        perfil = Perfil.objects.get(usuario=user)
        self.assertIsNotNone(perfil)
```

* Garantir que a **ação da signal ocorreu corretamente** é essencial para confiabilidade do sistema.

---

## 7. Referências

* [Django Signals Documentation](https://docs.djangoproject.com/en/stable/topics/signals/)
* [Best Practices for Django Signals](https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-use-django-signals.html)
* [Signals e Testes no Django](https://docs.djangoproject.com/en/stable/topics/testing/tools/)

