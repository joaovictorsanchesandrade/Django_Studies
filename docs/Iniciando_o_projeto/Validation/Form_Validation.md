A **validação de formulários** no Django garante que os dados enviados pelo usuário sejam **seguros, consistentes e corretos** antes de qualquer processamento ou persistência no banco de dados.

No Django, a validação é **automática, em camadas e previsível**, seguindo um fluxo bem definido.

---

## Onde a Validação Acontece?

A validação pode ocorrer em três níveis:

1. **Campo do Form**
2. **Formulário (Form / ModelForm)**
3. **Model**

📌 A validação deve acontecer **antes de qualquer lógica na view**.

---

## Fluxo Interno de Validação

Quando `is_valid()` é chamado:

1. `to_python()` → conversão de tipo
2. `validate()` → validações internas
3. `run_validators()` → validators customizados
4. `clean_<campo>()`
5. `clean()`
6. Dados finais em `cleaned_data`

```python
form.is_valid()
```

---

## Validação Automática de Campos

Cada campo já possui validações internas:

```python
forms.EmailField()
forms.IntegerField()
forms.URLField()
forms.DateField()
```

Exemplo:

```python
forms.EmailField(required=True)
```

✔️ Valida formato
✔️ Valida presença
✔️ Converte para Python

---

## Validação de Campo (`clean_<campo>`)

Usada para validações **isoladas por campo**.

```python
class CadastroForm(forms.Form):

    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise forms.ValidationError(
                "O nome de usuário não pode conter espaços"
            )
        return username
```

---

## Validação Global (`clean()`)

Usada quando a validação depende de **mais de um campo**.

```python
class RegistroForm(forms.Form):
    senha = forms.CharField()
    confirmar_senha = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('senha') != cleaned_data.get('confirmar_senha'):
            raise forms.ValidationError(
                "As senhas não coincidem"
            )
```

---

## ValidationError

```python
from django.core.exceptions import ValidationError
```

Pode conter:

* string simples
* lista de mensagens
* dicionário por campo

```python
raise ValidationError({
    'email': 'E-mail inválido'
})
```

---

## Validators Reutilizáveis

```python
from django.core.validators import RegexValidator

cpf_validator = RegexValidator(
    regex=r'^\d{11}$',
    message='CPF inválido'
)
```

Uso:

```python
forms.CharField(validators=[cpf_validator])
```

---

## Validação em ModelForm

A ordem é:

1. Validação do Form
2. Validação do Model
3. `clean()` do Model

📌 Evita duplicação de regras.

---

## Mensagens de Erro Customizadas

```python
forms.CharField(
    error_messages={
        'required': 'Campo obrigatório',
        'invalid': 'Valor inválido'
    }
)
```

---

## Erros Não Relacionados a Campos

```python
raise forms.ValidationError(
    "Erro geral no formulário"
)
```

Exibição no template:

```django
{{ form.non_field_errors }}
```

---

## Exibindo Erros no Template

```django
{% for field in form %}
    {{ field.label }}
    {{ field }}
    {{ field.errors }}
{% endfor %}
```

---

## Validação Manual (Avançado)

```python
form = Form(request.POST)

if not form.is_valid():
    print(form.errors)
```

📌 Útil para APIs ou logs.

---

## Segurança e Validação

* Protege contra XSS
* Evita dados maliciosos
* Normaliza dados
* Impede inconsistência no banco

📌 Validação é uma camada de **segurança**, não só UX.

---

## Boas Práticas

* Nunca valide na view
* Centralize validações reutilizáveis
* Prefira validação no Model quando possível
* Use mensagens claras
* Teste formulários

---

## Erros Comuns

* Acessar `cleaned_data` antes de `is_valid()`
* Escrever validação na view
* Ignorar validações do Model
* Duplicar regras

---

## Form Validation vs Model Validation

| Tipo             | Quando usar            |
| ---------------- | ---------------------- |
| Form Validation  | UX, regras temporárias |
| Model Validation | Regras de negócio      |
| Validators       | Reutilização           |

---

## Conclusão

A **validação de formulários** no Django é robusta, previsível e segura.

Dominar esse fluxo garante:

* menos bugs
* dados consistentes
* aplicações profissionais

