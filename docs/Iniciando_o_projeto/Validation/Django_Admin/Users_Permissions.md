O sistema de **Users & Permissions** do Django fornece uma base robusta para **autenticação, autorização e controle de acesso**.
Ele é amplamente integrado ao **Django Admin**, permitindo gerenciar quem pode acessar, visualizar, criar, alterar ou excluir dados.

Dominar este tema é essencial para construir aplicações **seguras e escaláveis**.

---

## Visão Geral do Sistema de Autenticação

O Django fornece nativamente:

* Usuários (`User`)
* Grupos (`Group`)
* Permissões (`Permission`)
* Autenticação
* Integração total com o Admin

Tudo isso está no app:

```python
django.contrib.auth
```

---

## O Model User

Por padrão, o Django usa o model:

```python
from django.contrib.auth.models import User
```

Campos comuns:

* `username`
* `email`
* `password`
* `is_active`
* `is_staff`
* `is_superuser`
* `last_login`

📌 **Nunca armazene senha manualmente**. O Django usa hash seguro automaticamente.

---

## Flags Importantes do Usuário

| Campo              | Descrição                      |
| ------------------ | ------------------------------ |
| `is_active`        | Usuário ativo no sistema       |
| `is_staff`         | Pode acessar o Django Admin    |
| `is_superuser`     | Possui todas as permissões     |
| `is_authenticated` | Usuário autenticado (dinâmico) |

---

## Criando Usuários

### Pelo terminal

```bash
python manage.py createsuperuser
```

### Pelo código

```python
User.objects.create_user(
    username='joao',
    email='joao@email.com',
    password='123456'
)
```

---

## Grupos (Groups)

Grupos permitem **organizar permissões por papel**.

Exemplos:

* Administrador
* Editor
* Moderador
* Suporte

Criar grupo:

```python
from django.contrib.auth.models import Group

Group.objects.create(name='Editores')
```

---

## Permissões (Permissions)

### Permissões padrão

Para cada model, o Django cria automaticamente:

* `add_model`
* `change_model`
* `delete_model`
* `view_model`

Exemplo:

```text
add_post
change_post
delete_post
view_post
```

---

## Atribuindo Permissões a Grupos

```python
from django.contrib.auth.models import Permission

group = Group.objects.get(name='Editores')
permission = Permission.objects.get(codename='change_post')

group.permissions.add(permission)
```

📌 Boa prática: **atribuir permissões a grupos, não diretamente a usuários**.

---

## Atribuindo Permissões a Usuários

```python
user.user_permissions.add(permission)
```

⚠️ Use apenas quando necessário.

---

## Verificando Permissões no Código

### Em Views

```python
if request.user.has_perm('blog.change_post'):
    ...
```

---

### Decorator

```python
from django.contrib.auth.decorators import permission_required

@permission_required('blog.delete_post')
def excluir_post(request):
    ...
```

---

### Em Templates

```django
{% if perms.blog.add_post %}
    <a href="#">Criar Post</a>
{% endif %}
```

---

## Permissões no Django Admin

O Admin respeita automaticamente:

* permissões de add, change, delete e view
* grupos e permissões do usuário

Exemplo:

* Usuário sem `change_post` não pode editar
* Usuário sem `add_post` não vê o botão "Adicionar"

---

## Customizando Permissões no Admin

```python
class PostAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('blog.delete_post')
```

Outros métodos:

* `has_add_permission`
* `has_change_permission`
* `has_view_permission`

---

## Permissões Customizadas no Model

```python
class Post(models.Model):
    titulo = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ('publish_post', 'Pode publicar posts'),
        ]
```

Após criar:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Controle de Acesso por Grupos no Admin

Boas práticas:

* Superusuários: tudo liberado
* Staff comum: permissões específicas
* Usuários comuns: sem acesso ao Admin

---

## Admin e Segurança

✔️ Use HTTPS
✔️ Use permissões granulares
✔️ Evite `is_superuser` desnecessário
✔️ Revogue acessos antigos
✔️ Use logs e auditoria

---

## Erros Comuns

* Dar permissões diretamente a usuários
* Usar `is_superuser` para tudo
* Não revisar permissões periodicamente
* Misturar regras de negócio no Admin

---

## Quando Usar Grupos vs Permissões Diretas?

| Situação             | Melhor Opção     |
| -------------------- | ---------------- |
| Muitos usuários      | Grupos           |
| Papéis bem definidos | Grupos           |
| Exceção pontual      | Permissão direta |
| MVP pequeno          | Ambos            |

---

## Integração com Sistemas Maiores

* RBAC (Role-Based Access Control)
* Multi-tenant
* Permissões por objeto
* Django Guardian (object permissions)

---

## Conclusão

O sistema de **Users & Permissions** do Django é poderoso, flexível e seguro.
Quando bem utilizado, ele garante:

* controle total de acesso
* escalabilidade
* manutenção simples
* segurança profissional

Dominar esse tema é obrigatório para projetos Django sérios.

