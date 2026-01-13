O Django oferece recursos avançados para **performance, escalabilidade, internacionalização e deploy seguro**. Este guia reúne os principais tópicos que todo desenvolvedor deve dominar para criar **aplicações profissionais e robustas**.

---

## 1. Caching

O **caching** melhora a performance ao armazenar resultados de operações caras, evitando consultas ou processamento repetitivo.

Principais tipos de cache:

* **View Cache** – cache da resposta inteira da view.
* **Template Cache** – cache de blocos de template com `{% cache %}`.
* **Object/Queryset Cache** – armazenar resultados de consultas ou objetos no Redis, Memcached ou LocMem.

Mais detalhes: [Caching](Caching.md)

---

## 2. Asynchronous Django

O Django moderno suporta **programação assíncrona**, permitindo lidar com **I/O intensivo** sem bloquear o servidor.

* **Async Views** – `async def view` para requisições não bloqueantes.
* **Middleware Assíncrono** – processa requisições simultaneamente.
* **ORM Assíncrono** – permite consultas async em certos métodos.
* **WebSockets** – usando Django Channels para comunicação em tempo real.

Mais detalhes: [Asynchronous Django](Asynchronous_Django.md)

---

## 3. Background Tasks

Tarefas em background executam operações **fora do request/response cycle**, melhorando a performance do usuário.

* **Celery** – tasks assíncronas, agendadas ou periódicas.
* **Django Q** – alternativa simples para pequenos projetos.
* Aplicações: envio de e-mails, geração de relatórios, limpeza de cache.

Mais detalhes: [Background Tasks](Background_Tasks.md)

---

## 4. Localization

Permite que a aplicação seja **adaptada para múltiplos idiomas e regiões**.

* **i18n (internationalization)** – preparação da aplicação para múltiplos idiomas.
* **l10n (localization)** – formatação de datas, números e moedas conforme a localidade.
* Uso de `gettext` no Python e `{% trans %}` nos templates.
* Alteração de idioma dinâmica via middleware ou cookies.

Mais detalhes: [Localization](Localization.md)

---

## 5. Signals

Signals permitem **executar ações automáticas** em resposta a eventos do Django, mantendo **baixo acoplamento**.

* **Signals integradas**: `post_save`, `pre_save`, `m2m_changed`, `post_delete`.
* **Receivers** podem criar perfis, atualizar cache ou enviar notificações.
* Evite lógica pesada dentro de signals; prefira delegar para tasks assíncronas.

Mais detalhes: [Signals](Signals.md)

---

## 6. Deployment

O deployment garante que sua aplicação Django seja **acessível em produção de forma segura e escalável**.

* Servidores: WSGI (Gunicorn, uWSGI) ou ASGI (Uvicorn, Daphne).
* Reverse proxy: Nginx ou Apache para SSL, cache e compressão.
* Configurações críticas: `DEBUG=False`, `ALLOWED_HOSTS`, `SECRET_KEY`.
* Coleta de arquivos estáticos e mídia, variáveis de ambiente, monitoramento.

Mais detalhes: [Deployment](Deployment.md)

---

## 7. Production Checklist

Checklist essencial antes de colocar a aplicação em produção:

* Configurações seguras: `DEBUG=False`, `ALLOWED_HOSTS`, `SECRET_KEY`.
* HTTPS habilitado e cookies seguros.
* Banco de dados robusto com backups.
* Arquivos estáticos e mídia servidos separadamente.
* Logging, monitoramento e background tasks configurados.
* Testes e validações finalizados.

Mais detalhes: [Production Checklist](Production_Checklist.md)

---

## 8. Boas Práticas Gerais de Tópicos Avançados

1. **Combine caching, async e background tasks** para performance máxima.
2. **Use signals com moderação**, evitando lógica pesada dentro delas.
3. **Garanta suporte a múltiplos idiomas e fusos horários** para aplicações globais.
4. **Sempre siga a checklist de produção** antes de deploy.
5. **Monitore logs e métricas** em produção para manter confiabilidade.
6. **Automatize deploy e tasks** usando CI/CD e Celery/Django Q.

---

## 9. Referências

* [Django Caching](https://docs.djangoproject.com/en/stable/topics/cache/)
* [Django Async Views](https://docs.djangoproject.com/en/stable/topics/async/)
* [Django Channels](https://channels.readthedocs.io/en/stable/)
* [Celery Documentation](https://docs.celeryq.dev/en/stable/)
* [Django Localization](https://docs.djangoproject.com/en/stable/topics/i18n/)
* [Django Signals](https://docs.djangoproject.com/en/stable/topics/signals/)
* [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

