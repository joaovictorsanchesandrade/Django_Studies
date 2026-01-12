# Instalando o Django

> Pré-requisito:
> 
> 
> Presume-se que você já saiba o que são **Ambientes Virtuais** e esteja com o ambiente do projeto **ativado**.
> 
> Caso contrário, volte às anotações anteriores antes de continuar.
> 

---

## Instalando o Django

Com o ambiente virtual ativado, execute o comando:

```bash
pip install django

```

> Isso instalará o Django somente dentro do ambiente virtual, mantendo o sistema organizado.
> 

Para verificar se a instalação foi concluída corretamente:

```bash
django-admin --version

```

---

## Criando um novo projeto Django

Após a instalação, inicie seu projeto com o comando:

```bash
django-admin startproject nome_do_seu_projeto

```

Exemplo:

```bash
django-admin startproject meu_projeto

```

Isso criará a estrutura inicial do Django, incluindo arquivos de configuração, URLs e servidor.

---

## Iniciando o desenvolvimento

Entre na pasta do projeto:

```bash
cd nome_do_seu_projeto

```

E inicie o servidor de desenvolvimento:

```bash
python manage.py runserver

```

Acesse no navegador:

```
http://127.0.0.1:8000/

```

Se a página padrão do Django aparecer, seu ambiente está pronto para o desenvolvimento 🚀