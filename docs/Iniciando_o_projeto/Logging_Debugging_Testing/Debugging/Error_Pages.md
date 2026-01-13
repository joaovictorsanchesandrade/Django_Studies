No desenvolvimento web, é comum que usuários encontrem **erros HTTP**, como 404 ou 500. O Django oferece formas **nativas e configuráveis** de exibir essas páginas de erro, além de permitir a criação de **páginas personalizadas** para melhorar a experiência do usuário.

---

## 1. Principais Códigos de Erro

No Django, os erros HTTP mais comuns são:

| Código | Significado                                      |
| ------ | ------------------------------------------------ |
| 400    | Bad Request – Requisição inválida                |
| 403    | Forbidden – Acesso negado                        |
| 404    | Not Found – Página não encontrada                |
| 500    | Internal Server Error – Erro interno do servidor |

---

## 2. Páginas de Erro Padrão

Por padrão, o Django exibe:

* **Em `DEBUG = True`**: páginas de erro detalhadas com **traceback completo**, ideal para desenvolvimento.
* **Em `DEBUG = False`**: páginas genéricas sem informações técnicas, seguras para produção.

---

## 3. Criando Páginas de Erro Personalizadas

Você pode criar templates personalizados para cada tipo de erro, colocando arquivos na pasta `templates`:

```
templates/
    400.html
    403.html
    404.html
    500.html
```

Exemplo de template **404.html**:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Página Não Encontrada</title>
    <style>
        body { text-align: center; font-family: sans-serif; padding: 50px; }
        h1 { font-size: 50px; }
        p { font-size: 20px; }
        a { text-decoration: none; color: #3498db; }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>Página não encontrada.</p>
    <a href="/">Voltar para a página inicial</a>
</body>
</html>
```

> Esse template será exibido automaticamente sempre que o erro 404 ocorrer, quando `DEBUG = False`.

---

## 4. Configurando Views de Erro Personalizadas

Além dos templates, você pode criar **views personalizadas** para tratar erros de forma dinâmica:

```python
# myapp/views.py
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

def custom_500_view(request):
    return render(request, "500.html", status=500)
```

E registrar no **urls.py** principal:

```python
# projeto/urls.py
from django.conf.urls import handler404, handler500
from myapp import views

handler404 = views.custom_404_view
handler500 = views.custom_500_view
```

> Assim, você pode adicionar lógica extra, como sugestões de páginas, logs ou mensagens dinâmicas.

---

## 5. Boas Práticas

1. **Nunca exibir traceback em produção** (`DEBUG = False`) – evita vazamento de informações sensíveis.
2. **Manter consistência visual** entre páginas de erro e o layout do site.
3. **Incluir links úteis** para redirecionar o usuário.
4. **Registrar logs de erros** para monitoramento e depuração futura.
5. **Personalizar cada tipo de erro** (404, 403, 500) para melhor experiência do usuário.

---

## 6. Debugging e Logging de Erros

Mesmo com páginas personalizadas, é importante **registrar os erros no log** para análise:

```python
import logging

logger = logging.getLogger(__name__)

def custom_404_view(request, exception):
    logger.warning(f"404 - Página não encontrada: {request.path}")
    return render(request, "404.html", status=404)
```

> Combinar **Error Pages + Logging** ajuda a monitorar problemas sem comprometer a experiência do usuário.

---

## 7. Referências

* [Django Documentation – Custom error views](https://docs.djangoproject.com/en/stable/topics/http/views/#customizing-error-views)
* [Debugging Django Applications](https://docs.djangoproject.com/en/stable/topics/debugging/)

