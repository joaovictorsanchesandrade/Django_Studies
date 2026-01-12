# UpdateView

A **UpdateView** é utilizada para **editar registros existentes**.

Ela funciona de forma semelhante à CreateView, mas carregando os dados já salvos.

## Quando usar
- Edição de dados
- Atualização de perfis
- Painéis administrativos

## Funcionamento básico
A UpdateView:
1. Busca o objeto existente
2. Preenche o formulário
3. Atualiza os dados após validação

## Principais atributos
- `model`
- `fields`
- `template_name`
- `success_url`

## Exemplo
```python
class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'preco']
    success_url = '/produtos/'
```
