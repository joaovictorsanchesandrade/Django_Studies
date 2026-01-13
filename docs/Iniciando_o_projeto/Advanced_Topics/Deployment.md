O **deploy** é o processo de disponibilizar uma aplicação Django para produção, tornando-a acessível a usuários finais. Envolve configurar **servidores, banco de dados, segurança e escalabilidade**.

---

## 1. Preparativos para Deploy

Antes de colocar a aplicação em produção, é importante:

1. **Configurações de produção no settings.py**

```python
DEBUG = False
ALLOWED_HOSTS = ['meusite.com', 'www.meusite.com']

# Segurança
SECRET_KEY = 'uma_chave_secreta_segura'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

2. **Instalação de dependências**

```bash
pip install gunicorn psycopg2-binary
```

* `gunicorn` – servidor WSGI de produção.
* `psycopg2-binary` – driver para PostgreSQL (recomendado em produção).

3. **Banco de dados de produção** – use PostgreSQL, MySQL ou outro robusto, evitando SQLite.

4. **Coletar arquivos estáticos**

```bash
python manage.py collectstatic
```

* Copia todos os arquivos estáticos para o diretório definido em `STATIC_ROOT`.
* Essencial para servir CSS, JS e imagens em produção.

---

## 2. Servidores Web

Para produção, Django precisa de um **servidor WSGI/ASGI**:

| Tipo | Ferramenta      | Descrição                                                               |
| ---- | --------------- | ----------------------------------------------------------------------- |
| WSGI | Gunicorn, uWSGI | Executa aplicações Django síncronas.                                    |
| ASGI | Daphne, Uvicorn | Necessário para aplicações assíncronas ou WebSockets (Django Channels). |

* Normalmente, um **reverse proxy Nginx ou Apache** é usado na frente do WSGI/ASGI.
* Serve arquivos estáticos, faz SSL/TLS e gerencia conexões simultâneas.

---

## 3. Configurando Gunicorn e Nginx

### 3.1 Gunicorn

```bash
gunicorn projeto.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

* `--workers` define o número de processos.
* Pode ser gerenciado com **systemd** ou **supervisor** para reinício automático.

### 3.2 Nginx

```nginx
server {
    listen 80;
    server_name meusite.com www.meusite.com;

    location /static/ {
        alias /path/para/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

* Nginx serve arquivos estáticos e encaminha requisições para Gunicorn.
* Também pode configurar SSL/TLS com Let’s Encrypt.

---

## 4. Variáveis de Ambiente

* Nunca deixe **SECRET_KEY, senhas ou chaves de API** hardcoded.
* Use variáveis de ambiente ou arquivos `.env`:

```bash
export DJANGO_SECRET_KEY='uma_chave_segura'
export DATABASE_URL='postgres://user:senha@localhost:5432/meubanco'
```

* No `settings.py`:

```python
import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
```

---

## 5. Segurança em Produção

1. `DEBUG = False`
2. Configurar `ALLOWED_HOSTS` corretamente
3. HTTPS obrigatório (SSL/TLS)
4. Cookies seguros (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`)
5. Cabeçalhos de segurança (`SECURE_HSTS_SECONDS`, `SECURE_CONTENT_TYPE_NOSNIFF`)

---

## 6. Deploy em Serviços Populares

| Serviço               | Observações                                                       |
| --------------------- | ----------------------------------------------------------------- |
| **Heroku**            | Fácil para apps pequenos, integração com PostgreSQL.              |
| **AWS EC2**           | Total controle do servidor, escalabilidade manual.                |
| **DigitalOcean**      | VPS simples, bom para deploy customizado.                         |
| **Docker/Kubernetes** | Deploy containerizado, ideal para microservices e escalabilidade. |

* Docker permite **isolamento completo da aplicação** e fácil replicação em diferentes ambientes.

---

## 7. Boas Práticas de Deploy

1. **Sempre usar banco de dados robusto em produção** (PostgreSQL recomendado).
2. **Servir arquivos estáticos e mídia separadamente** (Nginx ou CDN).
3. **Automatizar deploy** com scripts ou CI/CD (GitHub Actions, GitLab CI).
4. **Monitoramento e logs**: configure `logging` e ferramentas como Sentry ou Prometheus.
5. **Backups regulares** de banco de dados e arquivos importantes.
6. **Testes antes do deploy** – use o Django Test Framework para evitar regressões.

---

## 8. Referências

* [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
* [Deploy Django with Gunicorn and Nginx](https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/gunicorn/)
* [Django and HTTPS / Security Settings](https://docs.djangoproject.com/en/stable/topics/security/)
* [Dockerizing Django](https://docs.docker.com/samples/django/)

