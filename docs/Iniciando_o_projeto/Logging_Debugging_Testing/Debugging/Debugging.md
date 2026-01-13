Depuração (debugging) é uma etapa fundamental no desenvolvimento de aplicações Django. Ela permite **identificar, analisar e corrigir erros**, além de **otimizar performance** e entender o fluxo interno do sistema.

O Django oferece ferramentas nativas e externas para depuração, desde **páginas de erro personalizadas** até **profilers e depuradores interativos**.

---

## 1. Principais Ferramentas e Conceitos

O fluxo de depuração e análise pode ser dividido em quatro grandes áreas:

| Ferramenta / Recurso              | Função Principal                                                                                |
| --------------------------------- | ----------------------------------------------------------------------------------------------- |
| [Error Pages](Error_Pages.md)     | Tratar e personalizar páginas de erro HTTP (404, 500, etc.)                                     |
| [debug_toolbar](debug_toolbar.md) | Analisar requisições, queries SQL, templates e tempo de execução em desenvolvimento             |
| [PDB IPDB](PDB_IPDB.md)           | Depuração interativa do código Python, inspecionando variáveis e fluxo em tempo real            |
| [django_silk](django_silk.md)     | Profiling detalhado de requisições, queries SQL, cache e funções para otimização de performance |

---

## 2. Error Pages

As **páginas de erro** permitem exibir mensagens amigáveis ao usuário quando ocorre algum problema:

* 404 – Página não encontrada
* 500 – Erro interno do servidor
* 403 – Acesso negado
* 400 – Requisição inválida

Você pode criar **templates personalizados** (`404.html`, `500.html`) e **views de erro** para adicionar lógica extra, como **logs de erros ou sugestões de navegação**.

Mais detalhes: [Error Pages](Error_Pages.md)

---

## 3. Django Debug Toolbar

O **Debug Toolbar** adiciona uma **barra lateral interativa** no navegador que exibe:

* SQL queries executadas
* Tempo de renderização de templates
* Cache hits/misses
* Informações de headers, sessões e logs
* Signals disparados

É uma ferramenta essencial para **identificar gargalos em desenvolvimento**.

Mais detalhes: [debug_toolbar](debug_toolbar.md)

---

## 4. PDB / IPDB

O **PDB** e o **IPDB** permitem **pausar a execução do código** em qualquer ponto e **interagir com o estado da aplicação**:

* Inspecionar variáveis e objetos do Django
* Executar código linha a linha
* Navegar pelo stack trace

O **IPDB** oferece uma interface mais amigável, com **cores e autocompletar**.

Mais detalhes: [PDB IPDB](PDB_IPDB.md)

---

## 5. Django Silk

O **Django Silk** é um **profiler avançado** para monitoramento de performance:

* Tempo total de requisições HTTP
* SQL queries e tempo de execução
* Profiling de funções específicas com decorators
* Monitoramento de cache

Permite identificar **gargalos e otimizar performance**, sendo complementar à Debug Toolbar.

Mais detalhes: [django_silk](django_silk.md)

---

## 6. Boas Práticas de Debugging

1. **Use ferramentas de depuração apenas em desenvolvimento** (`DEBUG = True`).
2. **Não exiba informações sensíveis em produção**.
3. **Combine logging e debugging interativo** para rastrear erros e fluxo do sistema.
4. **Perfis e análises de performance** ajudam a detectar problemas antes que afetem usuários finais.
5. **Personalize páginas de erro** para manter uma boa experiência ao usuário mesmo em situações inesperadas.

---

Este arquivo funciona como **guia central de debugging no Django**, organizando os recursos essenciais para:

* Detecção de erros
* Depuração interativa
* Monitoramento e profiling de performance

Links detalhados fornecem instruções completas para cada ferramenta.

