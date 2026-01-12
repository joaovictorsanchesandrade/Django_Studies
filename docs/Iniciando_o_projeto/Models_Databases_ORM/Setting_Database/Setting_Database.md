O Django possui um sistema de configuração de banco de dados **simples, flexível e poderoso**, permitindo trocar de banco com poucas alterações no código.

Toda a configuração de banco fica centralizada no arquivo:

```python
settings.py
```

---

## Onde o Banco de Dados é Configurado?

No Django, o banco de dados é definido pela variável `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

📌 O Django usa o conceito de **um banco padrão (`default`)**, mas suporta múltiplos bancos.

---

## Componentes da Configuração

Principais chaves usadas em `DATABASES`:

* `ENGINE` → tipo do banco de dados
* `NAME` → nome do banco ou caminho do arquivo
* `USER` → usuário do banco
* `PASSWORD` → senha
* `HOST` → endereço do servidor
* `PORT` → porta de conexão

Nem todos são necessários em todos os bancos.

---

## Banco Padrão: SQLite

Por padrão, o Django vem configurado com **SQLite**, ideal para:

* estudos
* protótipos
* projetos pequenos
* testes rápidos

Exemplo:

```python
ENGINE = 'django.db.backends.sqlite3'
```

✔️ Não exige servidor
✔️ Fácil de usar
❌ Não recomendado para produção em larga escala

---

## Estrutura Recomendada para Produção

Em produção, é comum usar variáveis de ambiente:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

📌 Boa prática de segurança.

---

## Múltiplos Bancos de Dados

O Django suporta **mais de um banco simultaneamente**:

```python
DATABASES = {
    'default': {...},
    'replica': {...}
}
```

Uso comum:

* leitura/escrita separadas
* microsserviços
* migração gradual de dados

---

## Migrations e Banco de Dados

Após configurar o banco, utilize:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esses comandos:

* criam tabelas
* aplicam alterações
* mantêm o schema sincronizado

---

## Boas Práticas

* Use SQLite apenas para desenvolvimento
* Prefira PostgreSQL em produção
* Nunca versione senhas no código
* Utilize variáveis de ambiente
* Teste migrations antes de subir para produção

---

## Conteúdos Relacionados

1. **[Supported DBs](Supported_DBs.md)**
   Lista de bancos de dados suportados pelo Django, com características, vantagens e quando usar cada um.

---

## Conclusão

A configuração de banco de dados no Django é:

* simples de iniciar
* poderosa para crescer
* flexível para diferentes cenários

Entender bem essa configuração é essencial para criar aplicações **seguras, escaláveis e bem estruturadas**.

