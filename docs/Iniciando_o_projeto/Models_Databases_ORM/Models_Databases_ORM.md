Esta seção aborda o **coração do Django**: a modelagem de dados, o relacionamento com o banco de dados e o uso do ORM para manipular informações de forma segura, eficiente e escalável.

O objetivo é fornecer uma base sólida que vai desde a definição de models até consultas avançadas e otimização de performance em ambientes reais.

---

## Estrutura do Conteúdo

1. **[Models](Models/Models.md)**
   Introdução à criação de Models no Django.
   Aborda tipos de campos, opções de campos, campos personalizados e boas práticas para modelagem de dados.

2. **[Model Relationships](Model_relationships.md)**
   Relacionamentos entre Models.
   Inclui `ForeignKey`, `OneToOneField`, `ManyToManyField`, relações reversas, `related_name` e estratégias de modelagem.

3. **[Model Methods](Model_methods.md)**
   Métodos personalizados nos Models.
   Demonstra como encapsular regras de negócio, criar métodos utilitários, sobrescrever `save()` e manter código limpo.

4. **[Model Inheritance](Model_inheritance.md)**
   Herança de Models no Django.
   Cobre herança abstrata, multi-table inheritance e proxy models, além de quando usar cada abordagem.

5. **[Setting Up the Database](Setting_Database/Setting_Database.md)**
   Configuração do banco de dados.
   Inclui bancos suportados, configuração do `settings.py`, variáveis de ambiente e boas práticas para desenvolvimento e produção.

6. **[Migrations](Migrations.md)**
   Controle de versão do banco de dados.
   Aborda criação, aplicação, rollback de migrations, migrations customizadas e uso seguro em produção.

7. **[Django ORM](Django_ORM/Django_ORM.md)**
   Manipulação de dados com o Django ORM.
   Vai desde consultas básicas até SQL puro e otimização avançada de queries.

---

## Objetivos deste Módulo

Ao concluir esta seção, você será capaz de:

* Modelar bancos de dados corretamente
* Criar relações eficientes entre tabelas
* Encapsular regras de negócio nos Models
* Gerenciar bancos de dados com segurança
* Escrever queries performáticas e escaláveis

---

📌 **Importante:**
Uma boa modelagem e domínio do ORM impactam diretamente:

* performance
* escalabilidade
* manutenção do projeto
* qualidade do código

Este módulo é essencial para quem deseja trabalhar com Django em **nível profissional**.
