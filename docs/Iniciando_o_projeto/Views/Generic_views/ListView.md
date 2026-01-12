# ListView

A **ListView** é uma Generic View utilizada para **exibir uma lista de objetos** de um model.

Ela automatiza a consulta ao banco de dados e o envio desses dados para o template, evitando lógica repetitiva.

## Quando usar
- Listagem de registros
- Páginas iniciais
- Dashboards simples
- Tabelas de dados

## Funcionamento básico
A ListView:
1. Consulta todos os objetos do model
2. Envia os dados para o template
3. Renderiza a resposta HTTP

## Principais atributos
- `model`: model que será listado
- `template_name`: template utilizado
- `context_object_name`: nome da variável no template
- `paginate_by`: paginação dos resultados

## Exemplo
```python
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/list.html'
    context_object_name = 'produtos'
```

