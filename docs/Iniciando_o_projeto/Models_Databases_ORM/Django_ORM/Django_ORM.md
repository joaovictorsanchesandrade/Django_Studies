O **Django ORM (Object-Relational Mapping)** é uma das partes mais poderosas do framework.
Ele permite interagir com o banco de dados usando **Python puro**, sem escrever SQL na maioria dos casos, mantendo segurança, legibilidade e produtividade.

Nesta seção, você aprenderá desde as operações básicas até técnicas avançadas de consulta, otimização e uso de SQL puro quando necessário.

---

## Conteúdos

1. **[Querying Data](Querying_data.md)**
   Introdução às consultas no Django ORM.
   Aprenda a recuperar dados usando `QuerySets`, filtros simples, encadeamento de consultas e avaliação preguiçosa (*lazy evaluation*).

2. **[Create, Update, Delete](Create_Update_Delete.md)**
   Operações de escrita no banco de dados.
   Aborda criação de registros, atualizações individuais e em massa, exclusões seguras e boas práticas com `save()`, `update()` e `delete()`.

3. **[Aggregations](Aggregations.md)**
   Uso de funções de agregação como `Count`, `Sum`, `Avg`, `Min` e `Max`.
   Essencial para gerar relatórios, métricas e estatísticas diretamente no banco de dados.

4. **[Filtering & Lookups](Filtering_lookups.md)**
   Filtros avançados e operadores de consulta.
   Inclui lookups de texto, números, datas, relacionamentos, `Q objects`, `F expressions` e consultas complexas.

5. **[Raw SQL](Raw_SQL.md)**
   Execução de SQL puro no Django de forma segura.
   Ideal para casos avançados onde o ORM não é suficiente, mantendo controle e performance sem abrir mão da segurança.

6. **[Query Optimization](Query_Optimization.md)**
   Técnicas de otimização de consultas para aplicações reais.
   Cobre N+1 queries, `select_related`, `prefetch_related`, índices, cache, `explain()` e estratégias de alta performance.

---

## Objetivos desta Seção

Ao concluir este módulo, você será capaz de:

* Consultar dados de forma eficiente
* Manipular grandes volumes de dados com segurança
* Criar queries complexas e performáticas
* Entender quando usar ORM ou SQL puro
* Escrever código limpo, escalável e profissional

---

📌 **Observação:**
Dominar o Django ORM é um diferencial enorme para aplicações em produção, APIs REST, sistemas de alto tráfego e projetos escaláveis.
