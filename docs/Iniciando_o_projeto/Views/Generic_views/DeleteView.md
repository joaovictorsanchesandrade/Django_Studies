# DeleteView

A **DeleteView** é usada para **remover registros** do banco de dados de forma controlada.

Normalmente inclui uma tela de confirmação antes da exclusão.

## Quando usar
- Exclusão de dados
- Painéis administrativos
- Gestão de registros

## Funcionamento básico
A DeleteView:
1. Busca o objeto
2. Exibe confirmação
3. Remove o registro
4. Redireciona após exclusão

## Principais atributos
- `model`
- `template_name`
- `success_url`

## Exemplo
```python
class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = '/produtos/'
```

