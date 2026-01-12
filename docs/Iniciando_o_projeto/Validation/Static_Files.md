Os **arquivos estáticos** são todos os recursos que **não mudam dinamicamente** durante a execução da aplicação, como:

* CSS
* JavaScript
* Imagens
* Fontes
* Ícones

O Django possui um sistema próprio para **organizar, coletar e servir arquivos estáticos**, tanto em desenvolvimento quanto em produção.

---

## Estrutura de Arquivos Estáticos

### Estrutura comum de um app

```text
app/
 └── static/
     └── app/
         ├── css/
         ├── js/
         └── img/
```

📌 O namespace do app evita conflitos entre arquivos.

---

## Configuração Básica

No `settings.py`:

```python
STATIC_URL = '/static/'
```

---

## Servindo Estáticos em Desenvolvimento

Durante o desenvolvimento:

```bash
python manage.py runserver
```

O Django:

* encontra arquivos em `static/`
* serve automaticamente

📌 **Apenas em DEBUG=True**.

---

## Coleta de Arquivos Estáticos

Em produção, os arquivos precisam ser **coletados** em um único diretório.

```bash
python manage.py collectstatic
```

Gera:

```text
staticfiles/
 ├── admin/
 ├── app/
 └── ...
```

---

## STATIC_ROOT

Define onde os arquivos coletados serão armazenados.

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

📌 Obrigatório em produção.

---

## STATICFILES_DIRS

Usado para arquivos estáticos **globais** (fora dos apps).

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

---

## Referenciando Estáticos nos Templates

Carregue a tag:

```django
{% load static %}
```

Uso:

```django
<link rel="stylesheet" href="{% static 'app/css/style.css' %}">
```

---

## Ordem de Busca dos Estáticos

1. `STATICFILES_DIRS`
2. `app/static/`
3. `STATIC_ROOT` (após collectstatic)

---

## Static Files em Produção

Em produção, o Django **não deve servir estáticos diretamente**.

Opções:

* WhiteNoise
* Nginx
* CDN (CloudFront, Cloudflare, etc.)

📎 Veja: `Whitenoise.md`

---

## Usando WhiteNoise

Configuração básica:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

📌 Ideal para deploy simples.

---

## Cache e Versionamento

Use arquivos com hash:

```python
STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)
```

Garante:

* cache infinito
* invalidação automática

---

## Admin e Static Files

O Django Admin depende fortemente de estáticos.

📌 Sempre execute `collectstatic` antes de produção.

---

## Erros Comuns

* Esquecer `{% load static %}`
* Caminho errado no template
* Não rodar `collectstatic`
* Conflito de nomes de arquivos
* Tentar servir estáticos com Django em produção

---

## Boas Práticas

* Sempre use namespace por app
* Use compressão
* Use hash nos arquivos
* Separe static e media
* Use CDN quando possível

---

## Static Files vs Media Files

| Tipo   | Exemplo | Armazenamento |
| ------ | ------- | ------------- |
| Static | CSS, JS | Versionado    |
| Media  | Uploads | Dinâmico      |

📌 Nunca misture os dois.

---

## Conclusão

O sistema de **Static Files do Django** é robusto e flexível.

Quando bem configurado:

* melhora performance
* evita bugs
* facilita deploy
* garante escalabilidade

