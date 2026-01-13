O **Django Debug Toolbar** é uma ferramenta poderosa para desenvolvimento, permitindo **inspecionar requisições, queries, templates e muito mais** diretamente no navegador. Ela facilita a **depuração e otimização** de aplicações Django.

---

## 1. Instalando o Django Debug Toolbar

Para instalar, use pip:

```bash
pip install django-debug-toolbar
```

---

## 2. Configuração Básica

1. **Adicionar à lista de INSTALLED_APPS:**

```python
# settings.py
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

2. **Adicionar middleware:**

```python
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

3. **Configurar URLs do toolbar:**

```python
# projeto/urls.py
from django.conf import settings
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
```

---

## 3. Configuração de IPs Permitidos

Por padrão, a toolbar só aparece para **IP locais**:

```python
# settings.py
INTERNAL_IPS = [
    "127.0.0.1",
]
```

> Em containers ou ambientes complexos, talvez seja necessário adicionar o IP real do host.

---

## 4. Funcionalidades do Django Debug Toolbar

A toolbar adiciona **uma barra lateral flutuante** no navegador, mostrando informações detalhadas sobre cada requisição:

| Painel           | Descrição                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| **SQL Queries**  | Lista todas as queries executadas, tempo de execução e possibilidade de "explain" para otimização. |
| **Templates**    | Mostra templates renderizados e tempo de renderização.                                             |
| **Cache**        | Informações sobre hits/misses de cache.                                                            |
| **Headers**      | Visualiza headers HTTP da requisição e resposta.                                                   |
| **Signals**      | Mostra sinais do Django disparados na requisição.                                                  |
| **Logging**      | Mostra mensagens registradas via `logging`.                                                        |
| **Request Vars** | GET, POST, COOKIES, SESSION e META.                                                                |
| **Timer**        | Tempo total da requisição e tempo por painel.                                                      |

---

## 5. Boas Práticas

1. **Use somente em desenvolvimento** (`DEBUG = True`).
2. **Evite habilitar em produção** – pode vazar informações sensíveis.
3. **Combine com logging** para registrar erros ou consultas importantes.
4. **Analise queries SQL** para identificar possíveis gargalos.
5. **Desative painéis desnecessários** se houver excesso de informação:

```python
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
]
```

---

## 6. Exemplo Prático

1. Crie uma view:

```python
# myapp/views.py
from django.shortcuts import render
from myapp.models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})
```

2. Abra a página no navegador.
3. Observe na **Debug Toolbar**:

   * Quantas queries foram executadas.
   * Tempo total de renderização.
   * Templates utilizados.

> Isso permite **identificar problemas de performance** ou consultas desnecessárias.

---

## 7. Referências

* [Django Debug Toolbar Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)
* [Django Official Debugging Guide](https://docs.djangoproject.com/en/stable/topics/debugging/)

