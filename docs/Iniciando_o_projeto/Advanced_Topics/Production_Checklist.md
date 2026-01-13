Antes de colocar sua aplicação Django em **produção**, é essencial garantir que ela esteja **segura, performática e confiável**. Este checklist cobre **configurações, segurança, performance e monitoramento**.

---

## 1. Configurações do Django

1. **DEBUG**

```python
DEBUG = False
```

* Nunca deixe `DEBUG=True` em produção.

2. **ALLOWED_HOSTS**

```python
ALLOWED_HOSTS = ['meusite.com', 'www.meusite.com']
```

* Liste todos os domínios e subdomínios válidos.

3. **SECRET_KEY**

* Use **uma chave secreta forte** via variável de ambiente.

```python
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
```

4. **TIME_ZONE**

* Configure fuso horário correto para registros e agendamentos:

```python
TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True
```

---

## 2. Segurança

1. **Cookies Seguros**

```python
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

2. **Cabeçalhos de Segurança**

```python
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

3. **HTTPS**

* Use SSL/TLS para todas as requisições.
* Redirecione HTTP para HTTPS.

4. **Senhas e Chaves**

* Nunca versionar senhas, chaves de API ou dados sensíveis.
* Use variáveis de ambiente ou **secret managers**.

---

## 3. Banco de Dados

1. **Banco de Produção**

* Use **PostgreSQL, MySQL ou outro robusto**, evite SQLite.

2. **Usuário com permissões mínimas**

* Não use o superuser do banco para a aplicação.

3. **Migrations**

```bash
python manage.py migrate --noinput
```

* Execute migrations antes do deploy.

4. **Backups**

* Configure backups automáticos e testados regularmente.

---

## 4. Arquivos Estáticos e Mídia

1. **Coleta de arquivos estáticos**

```bash
python manage.py collectstatic
```

2. **Serviço separado**

* Sirva arquivos estáticos/mídia via **Nginx, CDN ou storage S3**.

---

## 5. Servidores e Deploy

1. **Servidor WSGI/ASGI**

* WSGI: Gunicorn, uWSGI
* ASGI: Uvicorn, Daphne (para WebSockets e async)

2. **Reverse Proxy**

* Configure Nginx ou Apache para gerenciar HTTPS, cache e compressão.

3. **Workers**

* Defina número adequado de workers/proc para Gunicorn ou Celery.

4. **Variáveis de ambiente**

* Configure **DEBUG, SECRET_KEY, DATABASE_URL e outras variáveis críticas**.

---

## 6. Performance

1. **Caching**

* Configure **view cache, template cache ou cache de objetos**.
* Use **Redis ou Memcached** em produção.

2. **Compressão**

* Habilite gzip ou Brotli via Nginx.

3. **Banco de Dados**

* Otimize queries, crie índices e monitore desempenho.

---

## 7. Logging e Monitoramento

1. **Logging**

* Configure loggers, handlers e filtros para erros críticos.
* Envie logs importantes para **arquivos, Sentry ou sistemas centralizados**.

2. **Monitoramento**

* Use ferramentas como **Sentry, Prometheus, Grafana ou New Relic**.
* Monitore erros, desempenho e disponibilidade.

---

## 8. Tarefas e Background

1. **Background Tasks**

* Configure Celery, Django Q ou outro worker para tarefas demoradas.
* Monitore filas e retries.

2. **Agendamento**

* Verifique jobs periódicos (Celery Beat, Cron).

---

## 9. Testes Finais

1. **Testes de produção**

* Execute testes automatizados com Django Test Framework ou Pytest.

2. **Testes de carga**

* Teste o comportamento da aplicação sob alto volume de requisições.

3. **Testes de segurança**

* Realize varredura de vulnerabilidades e teste endpoints críticos.

---

## 10. Checklist Resumido

| Item                           | Status |
| ------------------------------ | ------ |
| DEBUG = False                  | ☐      |
| ALLOWED_HOSTS configurado      | ☐      |
| SECRET_KEY seguro              | ☐      |
| HTTPS/SSL habilitado           | ☐      |
| Banco de dados seguro          | ☐      |
| Migrations aplicadas           | ☐      |
| Arquivos estáticos coletados   | ☐      |
| Caching configurado            | ☐      |
| Logging e monitoramento ativos | ☐      |
| Background tasks funcionando   | ☐      |
| Testes executados              | ☐      |

---

## 11. Referências

* [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
* [Django Security Guide](https://docs.djangoproject.com/en/stable/topics/security/)
* [Deploy Django with Gunicorn and Nginx](https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/gunicorn/)

