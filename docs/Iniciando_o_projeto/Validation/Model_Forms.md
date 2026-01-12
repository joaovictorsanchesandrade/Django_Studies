Os **Model Forms** são uma abstração poderosa do Django que conectam **Forms diretamente aos Models**.
Eles reduzem código repetitivo, garantem consistência entre a camada de dados e a validação e facilitam a manutenção da aplicação.

Sempre que um formulário estiver diretamente ligado a um Model, **prefira `ModelForm`**.

---

## O Que é um ModelForm?

Um **ModelForm** é um formulário gerado automaticamente a partir de um Model.

```python
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']
```

O Django:

* cria os campos
* aplica validações do Model
* converte dados
* integra com o banco de dados

---

## Fluxo Completo: Form → Validação → Model

1. Usuário envia dados
2. `ModelForm` recebe o POST
3. Valida campos do Form
4. Executa validações do Model
5. Salva no banco (`save()`)

```python
form = UsuarioForm(request.POST)

if form.is_valid():
    form.save()
```

---

## Meta Options

### `fields`

```python
fields = ['nome', 'email']
```

---

### `exclude`

```python
exclude = ['criado_em']
```

📌 Use **fields ou exclude**, nunca ambos.

---

### `labels`

```python
labels = {
    'email': 'E-mail'
}
```

---

### `help_texts`

```python
help_texts = {
    'email': 'Digite um e-mail válido'
}
```

---

### `widgets`

```python
widgets = {
    'senha': forms.PasswordInput()
}
```

---

## Validação em ModelForms

### Validação de Campo

```python
class UsuarioForm(ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@empresa.com'):
            raise forms.ValidationError(
                'E-mail deve ser corporativo'
            )
        return email
```

---

### Validação Global

```python
def clean(self):
    cleaned_data = super().clean()
    if cleaned_data.get('senha') != cleaned_data.get('confirmar_senha'):
        raise forms.ValidationError('As senhas não coincidem')
```

---

## Reaproveitando Validação do Model

Validações no Model:

* `validators=[]`
* `clean()`
* `clean_<campo>()`

São automaticamente aplicadas no `ModelForm`.

📌 Evite duplicar validações.

---

## Salvando com `commit=False`

Permite modificar o objeto antes de salvar.

```python
form = UsuarioForm(request.POST)

if form.is_valid():
    usuario = form.save(commit=False)
    usuario.criado_por = request.user
    usuario.save()
```

---

## Atualizando Registros com ModelForm

```python
usuario = Usuario.objects.get(id=1)
form = UsuarioForm(request.POST, instance=usuario)

if form.is_valid():
    form.save()
```

📌 O Django entende que é uma atualização.

---

## Campos Extras no ModelForm

```python
class UsuarioForm(ModelForm):
    confirmar_email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['email']

    def clean(self):
        if self.cleaned_data['email'] != self.cleaned_data['confirmar_email']:
            raise forms.ValidationError("E-mails não coincidem")
```

📌 Campo não é salvo no Model.

---

## Customizando Mensagens de Erro

```python
class Meta:
    error_messages = {
        'email': {
            'unique': 'Este e-mail já está cadastrado'
        }
    }
```

---

## Segurança e Boas Práticas

* Nunca confie em dados do usuário
* Use `ModelForm` sempre que possível
* Centralize regras de negócio no Model
* Valide novamente no backend
* Use `commit=False` com cuidado

---

## Erros Comuns

* Repetir validações do Model no Form
* Usar `forms.Form` quando deveria usar `ModelForm`
* Alterar dados direto em `request.POST`
* Esquecer `instance` ao atualizar

---

## ModelForm vs Form

| Situação                   | Use         |
| -------------------------- | ----------- |
| Dados pertencem a um Model | `ModelForm` |
| Formulário independente    | `Form`      |
| CRUD                       | `ModelForm` |
| Lógica complexa sem Model  | `Form`      |

---

## Conclusão

Os **ModelForms** unem:

* produtividade
* segurança
* validação consistente
* integração com banco de dados

Eles são essenciais para aplicações Django **bem estruturadas e profissionais**.

