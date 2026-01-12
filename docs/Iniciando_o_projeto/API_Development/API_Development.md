Este módulo aborda os principais conceitos e ferramentas para criar **APIs RESTful** profissionais utilizando **Django REST Framework (DRF)**.
Ele reúne os elementos essenciais: **serializers, views/viewsets e routers**, garantindo APIs consistentes, escaláveis e fáceis de manter.

---

## Visão Geral

O desenvolvimento de APIs envolve três pilares principais no DRF:

1. **Serializers** – Convertem dados entre Python/Models e JSON, validando entrada e saída.
2. **Views & ViewSets** – Processam requisições HTTP, aplicam lógica de negócio e retornam respostas.
3. **Routers** – Mapeiam URLs automaticamente para ViewSets, padronizando endpoints.

Estes componentes trabalham juntos para **reduzir código repetitivo** e manter uma **estrutura consistente** para APIs REST.

---

## Estrutura do Módulo

### Conteúdos

1. **[Routers](Routers.md)**

   * Mapeamento automático de URLs para ViewSets
   * Tipos de routers: `DefaultRouter` e `SimpleRouter`
   * Versionamento e namespaces
   * Custom Actions e rotas personalizadas

2. **[Views & ViewSets](Views_ViewSets.md)**

   * Criação de endpoints usando `APIView`, `GenericAPIView` ou `Function-based Views`
   * Agrupamento de operações CRUD em `ViewSets`
   * Uso de decorators `@action` para custom endpoints
   * Boas práticas e erros comuns

3. **[Serializers](Serializers.md)**

   * Conversão entre Models e JSON
   * Validação de dados
   * Campos customizados e nested serializers
   * Read-only / Write-only fields
   * Separação de serializers para leitura e escrita

---

## Fluxo de Requisição em APIs

```text
Request
 → Authentication
 → Permissions
 → Throttling / Rate Limit
 → Router (URL → ViewSet)
 → Serializer Validation
 → View / ViewSet Logic
 → Response
```

📌 Cada etapa pode ser customizada, garantindo segurança, consistência e performance.

---

## Boas Práticas no Desenvolvimento de APIs

* Sempre validar dados no **serializer**
* Usar `ModelViewSet` e `DefaultRouter` sempre que possível
* Versionar a API (`v1`, `v2`, etc.)
* Padronizar respostas e status HTTP
* Evitar lógica de negócio pesada em Views ou Serializers
* Criar endpoints claros e específicos
* Documentar endpoints (Swagger / OpenAPI)
* Escrever testes automatizados

---

## Erros Comuns

* Criar ViewSets sem Router
* Serializers grandes e complexos
* Misturar lógica de negócio e validação
* Não versionar endpoints
* Ignorar controle de permissões e autenticação

---

## APIs em Projetos Reais

Em projetos profissionais, uma API DRF bem estruturada permite:

* Integração com frontends modernos (React, Vue, Mobile)
* Escalabilidade de endpoints sem duplicação de código
* Facilidade de manutenção e evolução
* Segurança via autenticação, permissões e throttling
* Documentação automática para times de desenvolvimento

---

## Conclusão

Dominar **Serializers, Views/ViewSets e Routers** é essencial para construir APIs REST **limpas, consistentes e escaláveis** com Django.
Este módulo fornece a base necessária para **desenvolver APIs profissionais e prontas para produção**.

