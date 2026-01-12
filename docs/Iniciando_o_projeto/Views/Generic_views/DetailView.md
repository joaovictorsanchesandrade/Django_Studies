# DetailView

A **DetailView** é usada para **exibir os detalhes de um único objeto** do model.

Ela busca automaticamente o objeto com base no identificador presente na URL.

## Quando usar
- Página de detalhes
- Visualização individual de registros
- Perfis
- Artigos ou posts

## Funcionamento básico
A DetailView:
1. Recebe o identificador do objeto
2. Busca o objeto no banco
3. Envia o objeto para o template

## Principais atributos
- `model`
- `template_name`
- `context_object_name`

## Exemplo
```python
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/detail.html'
```





