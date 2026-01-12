O **Message Framework** do Django permite exibir **mensagens temporárias** para o usuário, como:

* mensagens de sucesso
* erros
* avisos
* informações

Essas mensagens são muito usadas após:

* formulários
* ações de CRUD
* autenticação
* redirecionamentos

---

## O Que é o Message Framework?

É um sistema que:

* armazena mensagens temporariamente
* persiste entre requisições
* é exibido apenas uma vez
* melhora a experiência do usuário

📌 Ideal para feedback pós-ação.

---

## Como Funciona

Fluxo básico:

1. View adiciona a mensagem
2. Usuário é redirecionado
3. Template exibe a mensagem
4. Mensagem é removida

---

## Configuração Básica

O Message Framework vem habilitado por padrão.

Verifique no `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.messages',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
```

---

## Usando Mensagens na View

```python
from django.contrib import messages

messages.success(request, "Cadastro realizado com sucesso!")
```

Outros tipos:

```python
messages.error(request, "Erro ao salvar dados")
messages.warning(request, "Atenção!")
messages.info(request, "Informação importante")
```

---

## Níveis de Mensagens

| Nível     | Uso                |
| --------- | ------------------ |
| `success` | Operação concluída |
| `error`   | Erro crítico       |
| `warning` | Atenção            |
| `info`    | Informação         |
| `debug`   | Desenvolvimento    |

---

## Exibindo Mensagens no Template

```django
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
```

📌 Compatível com Bootstrap, Tailwind, etc.

---

## Message Tags

Cada mensagem possui:

* conteúdo
* nível
* `tags` (para CSS)

```django
{{ message.tags }}
```

---

## Usando com Redirects

```python
messages.success(request, "Registro atualizado")
return redirect('home')
```

📌 Mensagem sobrevive ao redirect.

---

## Mensagens em Forms

Exemplo:

```python
if form.is_valid():
    form.save()
    messages.success(request, "Salvo com sucesso")
else:
    messages.error(request, "Erro no formulário")
```

---

## Customizando Níveis de Mensagem

```python
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
```

📌 Útil para frameworks CSS.

---

## Armazenamento das Mensagens

Backends disponíveis:

* Session (padrão)
* Cookie

Configuração:

```python
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
```

---

## Mensagens e Segurança

* Não exponha dados sensíveis
* Mensagens não são persistentes
* Evite lógica de negócio em mensagens

---

## Boas Práticas

* Use mensagens claras e objetivas
* Combine com redirects
* Padronize estilos
* Não abuse de mensagens
* Use para feedback real

---

## Erros Comuns

* Esquecer de renderizar mensagens no template
* Usar mensagens para lógica de controle
* Não configurar CSS corretamente
* Mensagens genéricas demais

---

## Message Framework vs Alerts Manuais

| Abordagem         | Indicado              |
| ----------------- | --------------------- |
| Message Framework | Feedback temporário   |
| Alerts fixos      | Mensagens permanentes |
| Logs              | Debug                 |

---

## Conclusão

O **Message Framework** é essencial para criar aplicações Django com **boa experiência do usuário**.

Quando bem utilizado:

* melhora UX
* comunica ações claramente
* reduz confusão
* profissionaliza a aplicação

