## 🧱 Project (Projeto)

O **Project** é o contêiner principal da aplicação Django.
Ele representa **o sistema inteiro**.

### Um projeto contém:

* Configurações globais
* Conexão com banco de dados
* URLs principais
* Configurações de segurança
* Lista de apps instalados

### Estrutura típica de um projeto:

```text
meuprojeto/
├── manage.py
├── meuprojeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

### Criando um projeto:

```bash
django-admin startproject meuprojeto
```

👉 **Regra mental:**

> Um projeto = uma aplicação web completa.

---

## 🧩 App (Aplicação)

Um **App** é um **módulo funcional** dentro do projeto.
Cada app resolve **um problema específico**.

### Exemplos de apps:

* autenticação
* usuários
* blog
* pagamentos
* dashboard
* API
* produtos

### Estrutura típica de um app:

```text
blog/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

### Criando um app:

```bash
python manage.py startapp blog
```

Depois, registre o app em `settings.py`:

```python
INSTALLED_APPS = [
    'blog',
]
```

👉 **Regra mental:**

> Um app = uma funcionalidade isolada e reutilizável.

---

## 🔗 Relação entre Project e Apps

* Um **project** pode ter **vários apps**
* Um **app** pode ser reutilizado em **outros projetos**
* O Django incentiva **modularização**

### Exemplo real:

```text
Sistema de E-commerce (Project)
│
├── users (App)
├── products (App)
├── orders (App)
├── payments (App)
└── reports (App)
```

---

## 🧠 Boas práticas importantes

✅ Separe funcionalidades em apps
✅ Apps devem ser independentes
✅ Não jogue tudo em um único app
❌ Evite criar apps gigantes
✅ Pense em reutilização

---

## 📌 Resumo rápido

| Conceito   | O que é                         |
| ---------- | ------------------------------- |
| Project    | Aplicação Django completa       |
| App        | Módulo funcional do projeto     |
| Um projeto | Pode ter vários apps            |
| Um app     | Pode existir em vários projetos |
