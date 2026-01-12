O Django oferece suporte oficial a diversos **bancos de dados relacionais**, permitindo escolher a solução mais adequada para cada tipo de projeto — desde estudos até aplicações de grande escala em produção.

O suporte é feito por meio de **backends de banco de dados**, responsáveis pela comunicação entre o Django ORM e o banco.

---

## Bancos de Dados com Suporte Oficial

### SQLite

**Backend**

```python
'django.db.backends.sqlite3'
```

**Características**

* Banco de dados baseado em arquivo
* Não requer servidor
* Configuração zero

**Quando usar**

* Estudos
* Prototipagem
* Testes automatizados
* Projetos pequenos

**Limitações**

* Baixa concorrência
* Pouco escalável
* Não indicado para produção pesada

---

### PostgreSQL (Recomendado)

**Backend**

```python
'django.db.backends.postgresql'
```

**Características**

* Banco de dados robusto e completo
* Excelente suporte a transações
* Tipos avançados (JSONB, Array, UUID)
* Ótima integração com Django

**Quando usar**

* Produção
* Projetos médios e grandes
* Aplicações críticas

**Vantagens**

* Performance
* Confiabilidade
* Comunidade ativa

📌 **Banco mais recomendado pela comunidade Django**.

---

### MySQL

**Backend**

```python
'django.db.backends.mysql'
```

**Características**

* Muito popular
* Boa performance
* Amplo suporte em provedores de hospedagem

**Quando usar**

* Sistemas legados
* Ambientes já baseados em MySQL

**Observações**

* Preferir **InnoDB**
* Cuidado com diferenças de charset e collation

---

### MariaDB

**Backend**

```python
'django.db.backends.mysql'
```

**Características**

* Fork do MySQL
* Melhor performance em alguns cenários
* Totalmente compatível

**Quando usar**

* Alternativa ao MySQL
* Ambientes modernos

---

### Oracle

**Backend**

```python
'django.db.backends.oracle'
```

**Características**

* Banco corporativo
* Altamente escalável
* Recursos avançados

**Quando usar**

* Grandes empresas
* Ambientes corporativos específicos

⚠️ Configuração mais complexa.

---

## Bancos de Dados com Suporte Não Oficial

Além dos bancos oficiais, o Django pode ser usado com outros bancos via backends de terceiros.

### Exemplos

* Microsoft SQL Server
* IBM DB2
* CockroachDB
* Amazon Aurora

📌 A qualidade e compatibilidade dependem do backend utilizado.

---

## Comparação Rápida

| Banco      | Uso recomendado      | Produção |
| ---------- | -------------------- | -------- |
| SQLite     | Estudos / testes     | ❌        |
| PostgreSQL | Geral                | ✅        |
| MySQL      | Sistemas existentes  | ✅        |
| MariaDB    | Alternativa ao MySQL | ✅        |
| Oracle     | Corporativo          | ✅        |

---

## Considerações Importantes

* O Django ORM abstrai a maior parte das diferenças entre bancos
* Alguns recursos são **específicos de certos bancos** (ex: JSONB no PostgreSQL)
* Sempre teste migrations ao trocar de banco
* Nem todos os bancos lidam igual com constraints e índices

---

## Qual Banco Escolher?

**Regra prática:**

* Estudo → SQLite
* Produção → PostgreSQL
* Infra legada → MySQL / MariaDB
* Ambiente corporativo → Oracle

---

## Conclusão

O Django oferece flexibilidade para trabalhar com diferentes bancos de dados sem alterar a lógica da aplicação.

Escolher o banco correto:

* melhora performance
* aumenta confiabilidade
* facilita a manutenção

