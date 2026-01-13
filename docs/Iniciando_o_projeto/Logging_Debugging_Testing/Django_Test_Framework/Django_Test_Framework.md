Testes são uma parte essencial do desenvolvimento de aplicações Django. Eles garantem que seu código funciona corretamente, evita regressões e ajuda a manter a **qualidade e confiabilidade** da aplicação.

O Django oferece suporte nativo ao **unittest** por meio da classe `TestCase` e pode ser integrado com frameworks externos como **Pytest** para maior flexibilidade e produtividade.

---

## 1. Principais Ferramentas de Teste

| Ferramenta                                  | Função Principal                                                                                                       |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [Pytest](pytest.md)                         | Framework externo, simples e flexível, com suporte a fixtures, parametrização e cobertura de testes.                   |
| [unittest & TestCase](unittest_TestCase.md) | Framework nativo do Django baseado no `unittest`, ideal para testes isolados de models, views, forms e outras camadas. |

---

## 2. Estrutura Recomendada de Testes

Um projeto Django organizado deve manter os testes em uma estrutura clara:

```
myapp/
    tests/
        __init__.py
        test_models.py
        test_views.py
        test_forms.py
```

* **Arquivos**: iniciam com `test_` ou terminam com `_tests.py`.
* **Classes de Teste**: herdam de `TestCase` ou utilizam Pytest com funções que começam com `test_`.
* **Isolamento**: cada teste deve rodar independentemente, garantindo confiabilidade.

---

## 3. Testando Diferentes Camadas

1. **Models** – validar criação, métodos e regras de negócio.
2. **Views** – testar requisições, códigos de status e templates renderizados.
3. **Forms** – validar entradas válidas e inválidas.
4. **Serializers (DRF)** – testar validação e conversão de dados.
5. **URLs e Rotas** – garantir que endpoints corretos respondam como esperado.

---

## 4. Boas Práticas

1. **Use fixtures ou `setUp`** para criar dados de teste consistentes.
2. **Mantenha testes independentes** para evitar efeitos colaterais.
3. **Teste cenários positivos e negativos**.
4. **Combine TestCase nativo e Pytest** se desejar:

   * TestCase → simplicidade e integração nativa.
   * Pytest → flexibilidade, parametrização e plugins.
5. **Integre com CI/CD** para execução automática de testes.
6. **Evite acessar dados reais** – use banco de teste (`TestCase` e Pytest cuidam disso automaticamente).

---

## 5. Executando Testes

* **Com TestCase (nativo)**:

```bash
python manage.py test
```

* **Com Pytest**:

```bash
pytest
pytest -v         # Verbose
pytest --cov=myapp # Relatório de cobertura
```

> O Django cria um banco de dados temporário para executar os testes, garantindo **isolamento** e **limpeza automática**.

---

## 6. Comparação entre Pytest e TestCase

| Recurso             | TestCase nativo  | Pytest-Django              |
| ------------------- | ---------------- | -------------------------- |
| Base                | unittest         | pytest                     |
| Fixtures            | setUp / tearDown | Fixtures reutilizáveis     |
| Parametrização      | Limitada         | `@pytest.mark.parametrize` |
| Sintaxe             | Verbosa          | Concisa e legível          |
| Plugins e Cobertura | Limitado         | Amplo suporte a plugins    |

---

## 7. Referências

* [Django Testing Documentation](https://docs.djangoproject.com/en/stable/topics/testing/)
* [unittest Documentation](https://docs.python.org/3/library/unittest.html)
* [Pytest Documentation](https://docs.pytest.org/en/stable/)
* [Pytest-Django Documentation](https://pytest-django.readthedocs.io/en/latest/)

