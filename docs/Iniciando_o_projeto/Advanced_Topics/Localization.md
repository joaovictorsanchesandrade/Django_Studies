A **localização** é o processo de adaptar sua aplicação para diferentes **idiomas, regiões e formatos de dados**, garantindo que usuários de diferentes culturas tenham uma experiência consistente e compreensível.

O Django oferece suporte nativo para **i18n (internationalization)** e **l10n (localization)**, facilitando traduções e formatação de dados.

---

## 1. Conceitos Principais

* **i18n (Internationalization)** – preparar a aplicação para suportar múltiplos idiomas e regiões.
* **l10n (Localization)** – adaptar conteúdos e formatos específicos de cada local (datas, moedas, números, fuso horário).

> No Django, i18n e l10n trabalham juntos para criar aplicações multilíngues e culturalmente adequadas.

---

## 2. Configuração Inicial

No **settings.py**, habilite suporte a i18n e l10n:

```python
# Ativar internacionalização e localização
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Idioma padrão
LANGUAGE_CODE = 'pt-br'

# Fuso horário
TIME_ZONE = 'America/Sao_Paulo'

# Idiomas suportados
LANGUAGES = [
    ('en', 'English'),
    ('pt-br', 'Português (Brasil)'),
    ('es', 'Español'),
]

# Localização de arquivos de tradução
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
```

---

## 3. Marcação de Strings para Tradução

No código Python, use **`gettext`** para marcar strings:

```python
from django.utils.translation import gettext as _

def minha_view(request):
    mensagem = _("Bem-vindo ao nosso site!")
    return HttpResponse(mensagem)
```

No template, use a tag `{% trans %}`:

```html
{% load i18n %}
<h1>{% trans "Bem-vindo ao nosso site!" %}</h1>
```

* Para traduções plurais, use `ngettext` no Python e `{% blocktrans count %}` nos templates.

---

## 4. Criando Arquivos de Tradução

1. Gere arquivos `.po` com o comando:

```bash
django-admin makemessages -l pt_BR
```

* O comando busca todas as strings marcadas com `_()` ou `{% trans %}`.
* Cria o arquivo `locale/pt_BR/LC_MESSAGES/django.po`.

2. Traduza as mensagens no arquivo `.po`:

```po
msgid "Bem-vindo ao nosso site!"
msgstr "Welcome to our site!"
```

3. Compile os arquivos `.po` para `.mo`:

```bash
django-admin compilemessages
```

* Os arquivos `.mo` são utilizados em tempo de execução para exibir a tradução correta.

---

## 5. Mudando Idioma Dinamicamente

É possível alterar o idioma do usuário dinamicamente usando middleware e funções utilitárias:

```python
from django.utils import translation

def mudar_idioma(request, lang_code):
    translation.activate(lang_code)
    response = HttpResponse("Idioma alterado")
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response
```

* O Django verifica o cookie `django_language` ou o cabeçalho `Accept-Language` do navegador.

---

## 6. Localização de Formatos

Com `USE_L10N = True`, o Django adapta automaticamente **datas, horários, números e moedas** de acordo com o idioma ativo:

```python
from django.utils import formats
from datetime import date

data = date.today()
print(formats.date_format(data))  # '12/01/2026' para pt-BR
```

* Em templates, use filtros como `{{ data|date:"SHORT_DATE_FORMAT" }}`.

---

## 7. Boas Práticas

1. Marque **todas as strings visíveis para o usuário** para tradução.
2. Use **variáveis dentro de traduções** com placeholders para evitar concatenação.
3. Mantenha **arquivos `.po` organizados por idioma** e compile sempre que alterar traduções.
4. Teste a aplicação em diferentes idiomas para garantir **coerência de layout e conteúdo**.
5. Combine com **timezone-aware datetime** para fuso horário correto.

---

## 8. Referências

* [Django Internationalization and Localization](https://docs.djangoproject.com/en/stable/topics/i18n/)
* [Django Translation Framework](https://docs.djangoproject.com/en/stable/topics/i18n/translation/)
* [Unicode and Time Zone Support](https://docs.djangoproject.com/en/stable/topics/i18n/timezones/)

