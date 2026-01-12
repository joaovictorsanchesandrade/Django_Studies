## Fluxo de solicitação–resposta no Django

No Django, o **roteamento** é responsável por direcionar uma requisição HTTP para a *view* correta.

O fluxo básico funciona assim:

**Request → URL Router → View → Response**

1. O cliente faz uma requisição (request).
2. O Django analisa a URL solicitada.
3. O *URL Router* tenta encontrar um padrão correspondente.
4. A *view* associada é executada.
5. Uma resposta (response) é retornada ao cliente.

Esse processo acontece de forma automática e eficiente, sendo um dos pilares da arquitetura do Django.

---

## Fundamentos de Roteamento

Os principais conceitos que você precisa dominar sobre roteamento no Django são:

1. [URL Patterns](URL_patterns.md)
   Definição dos caminhos e associação com views.

2. [Path Converters](Path_converters.md)
   Conversão dinâmica de partes da URL (int, str, slug, etc.).

3. [Grouping URLs](Grouping_URLs.md)
   Organização de URLs usando `include()`.

4. [Regex Paths](Reguex_Paths.md)
   Uso de expressões regulares para padrões mais complexos.

5. [Named URLs](Named_URLs.md)
   Nomeação de URLs para desacoplamento e manutenção.

6. [Reverse URL](Reverse_URL.md)
   Geração de URLs dinamicamente a partir do nome.

7. [Routing Middleware](Ruouting_Middleware.md)
   Interferência no fluxo de roteamento via middleware.

---

> 📌 **Observação:** Dominar o sistema de roteamento é essencial para criar aplicações Django escaláveis, organizadas e fáceis de manter.
