Durante o desenvolvimento de aplicações Django, é comum precisar **investigar o fluxo do código**, valores de variáveis e identificar **erros complexos**. Para isso, Python oferece **PDB (Python Debugger)** e **IPDB (IPython Debugger)**, ferramentas de depuração interativa que permitem **pausar a execução do código** e inspecionar seu estado.

---

## 1. PDB – Python Debugger

O **PDB** é o depurador nativo do Python. Ele permite:

* Pausar a execução do código.
* Inspecionar variáveis e objetos.
* Executar comandos linha a linha.
* Navegar pelo stack trace.

### 1.1 Usando PDB

Para iniciar uma sessão de depuração, importe `pdb` e insira um **ponto de interrupção** no código:

```python
import pdb

def minha_view(request):
    usuario = request.user
    pdb.set_trace()  # Pausa a execução aqui
    return HttpResponse(f"Olá, {usuario.username}")
```

### 1.2 Comandos Básicos do PDB

| Comando | Função                                        |
| ------- | --------------------------------------------- |
| `n`     | Próxima linha                                 |
| `s`     | Entrar em uma função chamada                  |
| `c`     | Continuar a execução até o próximo breakpoint |
| `l`     | Listar linhas do código ao redor              |
| `p var` | Imprimir valor da variável `var`              |
| `q`     | Sair do depurador                             |

> Quando a execução atingir `pdb.set_trace()`, o terminal ficará interativo, permitindo digitar esses comandos.

---

## 2. IPDB – IPython Debugger

O **IPDB** é uma versão mais amigável do PDB, com **auto-complete, cores e histórico de comandos**. Ele funciona da mesma forma, mas é mais eficiente para depuração interativa.

### 2.1 Instalando IPDB

```bash
pip install ipdb
```

### 2.2 Usando IPDB

```python
import ipdb

def processar_pedido(pedido):
    total = pedido.quantidade * pedido.preco
    ipdb.set_trace()  # Pausa a execução aqui
    return total
```

* Quando o código atingir `ipdb.set_trace()`, o terminal abrirá um prompt interativo.
* Todos os comandos do PDB funcionam, além de **auto-complete e histórico de variáveis**.

---

## 3. Dicas para Depuração no Django

1. **Use breakpoints somente em desenvolvimento** (`DEBUG = True`).
2. **Evite deixar `set_trace()` em produção**, pode travar o servidor.
3. Combine **PDB/IPDB com logging** para rastrear erros e fluxo de execução.
4. Em **views**, inserir breakpoints permite inspecionar `request`, `user` e qualquer objeto do Django.
5. Em **models ou scripts**, permite depurar lógica complexa e consultas SQL.

---

## 4. Exemplo Prático no Django

```python
# views.py
import ipdb
from django.shortcuts import render
from myapp.models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    ipdb.set_trace()  # Pausa aqui para inspecionar 'produtos'
    return render(request, 'produtos.html', {'produtos': produtos})
```

* Ao acessar a view, o servidor entrará em modo interativo no terminal.
* Você pode inspecionar `produtos`, testar métodos e até alterar valores temporariamente para testes.

---

## 5. Vantagens do PDB/IPDB

* Depuração **em tempo real**, sem necessidade de print().
* Permite **exploração detalhada de objetos Django**.
* Mais seguro que alterar código para debugging.
* Funciona em **views, models, forms e scripts**.

---

## 6. Referências

* [Python Debugger (PDB) Documentation](https://docs.python.org/3/library/pdb.html)
* [IPDB GitHub Repository](https://github.com/gotcha/ipdb)
* [Django Debugging Tips](https://docs.djangoproject.com/en/stable/topics/debugging/)

