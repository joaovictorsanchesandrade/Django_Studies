Os **Django Forms** são responsáveis por **receber, validar e processar dados de entrada do usuário**.
Eles atuam como a principal camada de **validação** entre o frontend e os Models, garantindo integridade, segurança e consistência dos dados.

No Django, validação **não pertence à view** — ela deve ficar nos **Forms** ou nos **Models**.

---

## O Que São Forms no Django?

Um Form é uma classe Python que:

* define campos
* valida dados
* converte dados para tipos Python
* lida com erros automaticamente

```python
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
```

---

## Fluxo de Validação dos Forms

1. Usuário envia dados (POST)
2. Form recebe os dados
3. `is_valid()` é chamado
4. Campos são validados
5. Validações customizadas são executadas
6. Dados limpos ficam em `cleaned_data`

```python
form = ContatoForm(request.POST)

if form.is_valid():
    dados = form.cleaned_data
```

---

## Tipos de Forms

### `forms.Form`

Usado quando não há ligação direta com Models.

```python
class LoginForm(forms.Form):
    usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)
```

---

### `forms.ModelForm`

Usado quando os dados pertencem a um Model.

```python
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']
```

📌 Reaproveita validações do Model automaticamente.

---

## Campos de Formulário

Exemplos comuns:

```python
forms.CharField()
forms.EmailField()
forms.IntegerField()
forms.BooleanField()
forms.DateField()
forms.ChoiceField()
forms.ModelChoiceField()
```

Cada campo:

* valida tipo
* valida formato
* converte para Python

---

## Widgets

Widgets controlam **como o campo aparece no HTML**.

```python
class LoginForm(forms.Form):
    senha = forms.CharField(widget=forms.PasswordInput)
```

Exemplo de widgets:

* `TextInput`
* `Textarea`
* `EmailInput`
* `Select`
* `CheckboxInput`

---

## Validação de Campo (`clean_<campo>`)

```python
class UsuarioForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@empresa.com'):
            raise forms.ValidationError(
                "Email deve ser corporativo"
            )
        return email
```

📌 Executado automaticamente durante `is_valid()`.

---

## Validação Global (`clean()`)

Usado para validar **múltiplos campos juntos**.

```python
class CadastroForm(forms.Form):
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

Pode ser lançada em:

* Forms
* Models
* Validators customizados

---

## Reutilizando Validators

```python
from django.core.validators import MinLengthValidator

class Usuario(models.Model):
    senha = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8)]
    )
```

📌 Validators no Model também funcionam nos Forms.

---

## Mensagens de Erro Customizadas

```python
forms.CharField(
    error_messages={
        'required': 'Campo obrigatório',
        'max_length': 'Texto muito longo'
    }
)
```

---

## Exibindo Erros no Template

```django
<form method="post">
    {{ form.non_field_errors }}
    {{ form.as_p }}
</form>
```

Ou campo a campo:

```django
{{ form.email.errors }}
```

---

## Segurança e Validação

* Protege contra SQL Injection
* Protege contra XSS
* Valida tipos automaticamente
* Normaliza dados

📌 Forms são uma camada crítica de segurança.

---

## Boas Práticas

* Nunca valide dados na view
* Prefira `ModelForm` quando possível
* Centralize validações reutilizáveis
* Mensagens claras para o usuário
* Combine validações de Form + Model

---

## Erros Comuns

* Escrever validação na view
* Ignorar `is_valid()`
* Manipular `request.POST` diretamente
* Duplicar validações

---

## Conclusão

Os **Django Forms** são o ponto central da **validação de dados** na aplicação.

Dominar Forms significa:

* código mais limpo
* menos bugs
* mais segurança
* aplicações mais profissionais

