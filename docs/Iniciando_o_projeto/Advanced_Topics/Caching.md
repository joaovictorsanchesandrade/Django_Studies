O **caching** é uma técnica avançada usada para **melhorar a performance e reduzir a carga no servidor**, armazenando resultados de operações caras ou dados frequentemente acessados para que possam ser reutilizados rapidamente.

O Django oferece suporte nativo a **vários tipos de cache**, que podem ser configurados para **views, templates, queries e objetos específicos**.

---

## 1. Tipos de Cache no Django

O Django suporta múltiplos **backends de cache**, cada um adequado a diferentes cenários:

| Backend          | Descrição                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------- |
| `LocMemCache`    | Cache em memória local do processo. Simples e rápido, mas não compartilhado entre processos. |
| `Memcached`      | Cache distribuído em memória, ótimo para múltiplos servidores.                               |
| `Redis`          | Cache distribuído e persistente, suporta tipos complexos e expiração avançada.               |
| `DatabaseCache`  | Armazena cache em uma tabela do banco de dados. Útil quando não há memória suficiente.       |
| `FileBasedCache` | Armazena cache em arquivos no disco. Mais lento que memória, mas persiste entre reinícios.   |

---

## 2. Configuração de Cache

No **settings.py**, você define o backend e parâmetros principais:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,  # segundos
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}
```

* `TIMEOUT` – tempo em segundos que o cache será válido.
* `MAX_ENTRIES` – número máximo de entradas no cache.
* `LOCATION` – identifica o cache (necessário para Memcached ou Redis).

---

## 3. Cache de Views

### 3.1 Cache de View inteiro

Use o decorator `cache_page` para armazenar **a resposta completa de uma view**:

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 15 minutos
def lista_produtos(request):
    # lógica da view
    ...
```

* A primeira requisição gera o conteúdo.
* As requisições subsequentes usam o cache, reduzindo consultas ao banco.

---

### 3.2 Cache de URL no urls.py

Também é possível aplicar cache diretamente nas rotas:

```python
from django.views.decorators.cache import cache_page
from django.urls import path
from myapp.views import lista_produtos

urlpatterns = [
    path('produtos/', cache_page(60 * 10)(lista_produtos)),
]
```

---

## 4. Cache de Template

O Django permite **cachear blocos específicos de templates** usando a tag `{% cache %}`:

```html
{% load cache %}
{% cache 600 lista_produtos %}
    <ul>
    {% for produto in produtos %}
        <li>{{ produto.nome }}</li>
    {% endfor %}
    </ul>
{% endcache %}
```

* O primeiro render grava o bloco em cache.
* Subsequentemente, o Django reutiliza o conteúdo armazenado.
* `600` é o tempo de expiração em segundos.

---

## 5. Cache de Querysets e Objetos

Você pode **armazenar resultados de consultas complexas** usando o cache manual:

```python
from django.core.cache import cache
from myapp.models import Produto

def produtos_caros():
    produtos = cache.get('produtos_caros')
    if not produtos:
        produtos = Produto.objects.filter(preco__gt=100)
        cache.set('produtos_caros', produtos, 300)  # 5 minutos
    return produtos
```

* Reduz consultas ao banco de dados para **resultados que mudam raramente**.

---

## 6. Estratégias Avançadas

1. **Cache de Fragmentos** – cache apenas partes do template ou view que consomem mais recursos.
2. **Cache seletivo por usuário** – usando **variáveis de chave** para diferenciar caches por sessão ou usuário.
3. **Invalidar cache** – limpar cache manualmente quando dados mudam:

```python
cache.delete('produtos_caros')
```

4. **Cache distribuído** – ideal para múltiplos servidores, usando Redis ou Memcached.
5. **Combinar com Django Signals** – invalidar cache automaticamente quando um objeto é atualizado:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Produto)
def limpar_cache_produtos(sender, instance, **kwargs):
    cache.delete('produtos_caros')
```

---

## 7. Boas Práticas

* Use **cache apenas quando os dados mudam raramente** ou têm alto custo de processamento.
* Sempre **defina tempo de expiração** para evitar dados desatualizados.
* Prefira **cache distribuído** em ambientes com múltiplos servidores.
* Combine **view cache + template cache + objeto cache** para máxima performance.
* Monitore a **taxa de acertos do cache** para garantir eficácia.

---

## 8. Referências

* [Django Caching Documentation](https://docs.djangoproject.com/en/stable/topics/cache/)
* [Memcached](https://memcached.org/)
* [Redis](https://redis.io/)

