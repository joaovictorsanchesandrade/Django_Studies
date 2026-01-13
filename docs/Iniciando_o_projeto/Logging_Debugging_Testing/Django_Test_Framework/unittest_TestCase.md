O Django possui um framework de testes integrado baseado no **unittest** do Python. Ele fornece a classe **`django.test.TestCase`**, que facilita **escrever testes isolados e confiáveis** para models, views, forms e outros componentes da aplicação.

---

## 1. Estrutura de Testes com TestCase

A estrutura básica de testes no Django é:

```
myapp/
    tests/
        __init__.py
        test_models.py
        test_views.py
        test_forms.py
```

* Cada arquivo de teste deve conter **classes que herdam de `TestCase`**.
* Cada método de teste deve começar com `test_`.

---

## 2. Teste de Model

```python
# myapp/tests/test_models.py
from django.test import TestCase
from myapp.models import Produto

class ProdutoModelTest(TestCase):

    def setUp(self):
        # Executado antes de cada teste
        self.produto = Produto.objects.create(nome="Caneta", preco=2.50)

    def test_produto_criacao(self):
        self.assertEqual(self.produto.nome, "Caneta")
        self.assertEqual(self.produto.preco, 2.50)

    def test_str_model(self):
        self.assertEqual(str(self.produto), "Caneta")
```

> `setUp` é executado antes de cada teste, garantindo **isolamento**.

---

## 3. Teste de View

```python
# myapp/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from myapp.models import Produto

class ProdutoViewTest(TestCase):

    def setUp(self):
        Produto.objects.create(nome="Caderno", preco=10.0)

    def test_lista_produtos_view(self):
        url = reverse('lista_produtos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Caderno")
```

> O **`self.client`** simula requisições HTTP, permitindo testar views sem iniciar o servidor.

---

## 4. Teste de Form

```python
# myapp/tests/test_forms.py
from django.test import TestCase
from myapp.forms import ProdutoForm

class ProdutoFormTest(TestCase):

    def test_produto_form_valido(self):
        form_data = {'nome': 'Caneta', 'preco': 2.50}
        form = ProdutoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_produto_form_invalido(self):
        form_data = {'nome': '', 'preco': -1}
        form = ProdutoForm(data=form_data)
        self.assertFalse(form.is_valid())
```

---

## 5. Boas Práticas com TestCase

1. **Use `setUp` e `tearDown`** para preparar e limpar dados de teste.
2. **Mantenha os testes independentes** – cada teste deve rodar isoladamente.
3. **Teste diferentes camadas**: models, views, forms, serializers.
4. **Use `self.client` para simular requisições HTTP**.
5. **Teste cenários válidos e inválidos**, garantindo cobertura completa.

---

## 6. Executando Testes

Na raiz do projeto Django, rode:

```bash
python manage.py test
```

* O Django cria **um banco de dados temporário** para rodar os testes.
* Ao final, o banco de teste é destruído automaticamente.

---

## 7. Comparação com Pytest

| Recurso        | TestCase nativo    | Pytest-Django                       |
| -------------- | ------------------ | ----------------------------------- |
| Base           | unittest           | pytest                              |
| Fixtures       | `setUp`/`tearDown` | Fixtures e `@pytest.mark.django_db` |
| Parametrização | Limitada           | `@pytest.mark.parametrize`          |
| Sintaxe        | Verbosa            | Mais concisa e legível              |

> O `TestCase` é ideal para quem deseja **usar apenas recursos nativos do Django**, enquanto Pytest oferece **mais flexibilidade e recursos avançados**.

---

## 8. Referências

* [Django Testing Documentation](https://docs.djangoproject.com/en/stable/topics/testing/)
* [unittest Documentation](https://docs.python.org/3/library/unittest.html)
* [Testing Django Models, Views, and Forms](https://docs.djangoproject.com/en/stable/topics/testing/overview/)

