O **Pytest** é um framework de testes em Python **simples, poderoso e flexível**, muito utilizado em projetos Django. Ele permite escrever **testes legíveis, parametrizados e escaláveis**, facilitando a garantia de qualidade da aplicação.

No contexto do Django, o Pytest pode ser integrado usando o pacote **`pytest-django`**, que adiciona suporte completo a **settings do Django, database e fixtures**.

---

## 1. Instalando Pytest e Pytest-Django

Instale as dependências via pip:

```bash
pip install pytest pytest-django
```

> Opcionalmente, para relatórios detalhados e cobertura de testes:

```bash
pip install pytest-cov
```

---

## 2. Configuração Básica

1. **Criar arquivo pytest.ini** na raiz do projeto:

```ini
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = projeto.settings
python_files = tests.py test_*.py *_tests.py
```

* `DJANGO_SETTINGS_MODULE`: aponta para as configurações do Django.
* `python_files`: define quais arquivos serão reconhecidos como testes.

2. **Estrutura recomendada de testes:**

```
myapp/
    tests/
        __init__.py
        test_models.py
        test_views.py
        test_forms.py
```

---

## 3. Escrevendo Testes com Pytest

### 3.1 Teste de Model

```python
# myapp/tests/test_models.py
import pytest
from myapp.models import Produto

@pytest.mark.django_db
def test_produto_criacao():
    produto = Produto.objects.create(nome="Caneta", preco=2.50)
    assert produto.nome == "Caneta"
    assert produto.preco == 2.50
```

> `@pytest.mark.django_db` habilita o acesso ao **banco de dados de teste** do Django.

---

### 3.2 Teste de View

```python
# myapp/tests/test_views.py
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_lista_produtos_view(client):
    url = reverse('lista_produtos')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Produtos" in response.content
```

> O **fixture `client`** do Pytest permite simular requisições HTTP sem iniciar o servidor.

---

### 3.3 Teste de Form

```python
# myapp/tests/test_forms.py
import pytest
from myapp.forms import ProdutoForm

def test_produto_form_valido():
    form_data = {'nome': 'Caneta', 'preco': 2.50}
    form = ProdutoForm(data=form_data)
    assert form.is_valid()

def test_produto_form_invalido():
    form_data = {'nome': '', 'preco': -1}
    form = ProdutoForm(data=form_data)
    assert not form.is_valid()
```

---

## 4. Fixtures no Pytest

Fixtures permitem **criar objetos reutilizáveis para testes**:

```python
# myapp/tests/conftest.py
import pytest
from myapp.models import Produto

@pytest.fixture
def produto():
    return Produto.objects.create(nome="Caderno", preco=10.0)
```

Uso da fixture:

```python
def test_produto_fixture(produto):
    assert produto.nome == "Caderno"
    assert produto.preco == 10.0
```

> Fixtures podem ser **compartilhadas entre múltiplos testes**, tornando-os mais limpos e reutilizáveis.

---

## 5. Marcadores Úteis

* `@pytest.mark.django_db` – habilita acesso ao banco de dados de teste.
* `@pytest.mark.skip` – ignora um teste específico.
* `@pytest.mark.parametrize` – roda o mesmo teste com diferentes parâmetros.

Exemplo de parametrização:

```python
@pytest.mark.parametrize("nome,preco", [("Caneta", 2.5), ("Caderno", 10)])
def test_produto_param(nome, preco):
    produto = Produto(nome=nome, preco=preco)
    assert produto.nome == nome
    assert produto.preco == preco
```

---

## 6. Executando Testes

Na raiz do projeto, rode:

```bash
pytest
```

* Para **testes detalhados**:

```bash
pytest -v
```

* Para **relatórios de cobertura**:

```bash
pytest --cov=myapp
```

---

## 7. Boas Práticas com Pytest no Django

1. **Use fixtures para criar dados de teste reutilizáveis**.
2. **Separe testes por tipo**: models, views, forms, serializers etc.
3. **Evite depender de dados reais** – sempre use banco de dados de teste (`pytest-django` cuida disso).
4. **Use parametrização** para testar múltiplos cenários com menos código.
5. **Integre Pytest com CI/CD** para garantir qualidade contínua.

---

## 8. Referências

* [Pytest Documentation](https://docs.pytest.org/en/stable/)
* [Pytest-Django Documentation](https://pytest-django.readthedocs.io/en/latest/)
* [Testing in Django with Pytest](https://docs.djangoproject.com/en/stable/topics/testing/overview/)

