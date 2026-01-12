# CreateView

A **CreateView** é responsável por **criar novos registros** no banco de dados.

Ela lida automaticamente com formulários, validação e salvamento.

## Quando usar
- Formulários de cadastro
- Criação de usuários
- Inserção de dados

## Funcionamento básico
A CreateView:
1. Exibe o formulário
2. Valida os dados enviados
3. Salva o objeto no banco
4. Redireciona após sucesso

## Principais atributos
- `model`
- `fields`
- `template_name`
- `success_url`

## Exemplo
```python
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'preco']
    success_url = '/produtos/'
```

