O **Django Admin** é uma das funcionalidades mais poderosas do framework.
Além de fornecer uma interface pronta para gerenciamento de dados, ele permite **alto nível de customização**, tornando-se uma ferramenta profissional para administração interna do sistema.

Este documento aborda as principais formas de **customizar o Django Admin**, desde ajustes visuais até regras de negócio avançadas.

---

## Por Que Customizar o Django Admin?

A customização do Admin permite:

* Melhor experiência para administradores
* Redução de erros operacionais
* Aumento de produtividade
* Aplicação de regras de negócio
* Controle de permissões e acessos
* Interface mais clara e organizada

---

## Registrando Models no Admin

Forma básica:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Forma recomendada (com customização):

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
```

---

## Exibindo Campos na Listagem (`list_display`)

Define quais campos aparecem na lista:

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'publicado', 'criado_em')
```

📌 Aceita métodos definidos no `ModelAdmin`.

---

## Filtros Laterais (`list_filter`)

```python
class PostAdmin(admin.ModelAdmin):
    list_filter = ('publicado', 'autor', 'criado_em')
```

Ideal para tabelas grandes.

---

## Busca no Admin (`search_fields`)

```python
class PostAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'conteudo', 'autor__username')
```

📌 Usa `LIKE` no banco de dados.

---

## Ordenação Padrão (`ordering`)

```python
class PostAdmin(admin.ModelAdmin):
    ordering = ('-criado_em',)
```

---

## Paginação (`list_per_page`)

```python
class PostAdmin(admin.ModelAdmin):
    list_per_page = 25
```

---

## Campos Editáveis na Lista (`list_editable`)

```python
class PostAdmin(admin.ModelAdmin):
    list_editable = ('publicado',)
```

⚠️ O campo não pode ser o primeiro da lista.

---

## Organização de Campos (`fields` e `fieldsets`)

### `fields`

```python
fields = ('titulo', 'conteudo', 'autor', 'publicado')
```

### `fieldsets`

```python
fieldsets = (
    ('Conteúdo', {
        'fields': ('titulo', 'conteudo')
    }),
    ('Publicação', {
        'fields': ('autor', 'publicado'),
        'classes': ('collapse',)
    }),
)
```

---

## Campos Somente Leitura (`readonly_fields`)

```python
readonly_fields = ('criado_em', 'atualizado_em')
```

---

## Inline Models (Relacionamentos)

Permite editar modelos relacionados na mesma página.

```python
class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline]
```

Tipos:

* `TabularInline`
* `StackedInline`

---

## Customizando Forms no Admin

```python
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
```

Útil para:

* validações extras
* widgets personalizados
* regras de negócio

---

## Actions Personalizadas

Permite executar ações em massa.

```python
def publicar_posts(modeladmin, request, queryset):
    queryset.update(publicado=True)

publicar_posts.short_description = "Publicar posts selecionados"

class PostAdmin(admin.ModelAdmin):
    actions = [publicar_posts]
```

---

## Permissões Customizadas

```python
class PostAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
```

Outros métodos:

* `has_add_permission`
* `has_change_permission`
* `has_view_permission`

---

## Customizando o Admin Site

```python
admin.site.site_header = "Painel Administrativo"
admin.site.site_title = "Admin Django"
admin.site.index_title = "Bem-vindo ao Admin"
```

---

## Sobrescrevendo Templates do Admin

Estrutura:

```text
templates/
└── admin/
    └── base_site.html
```

Permite:

* alterar layout
* incluir scripts
* mudar identidade visual

---

## Integração com CSS e JS

```python
class PostAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
        js = ('js/admin.js',)
```

---

## Boas Práticas

* Não usar Admin como frontend público
* Criar permissões bem definidas
* Evitar lógica complexa no Admin
* Usar `actions` com cuidado
* Testar com diferentes perfis de usuário

---

## Erros Comuns

* Expor dados sensíveis
* Falta de validação
* Admin lento por excesso de queries
* Não usar `select_related` / `prefetch_related`

---

## Quando o Django Admin é Suficiente?

✔️ Painéis internos
✔️ CRUD administrativo
✔️ Backoffice
✔️ MVPs
✔️ Ferramentas internas

❌ Sistemas públicos
❌ Dashboards complexos
❌ Interfaces finais para usuários

---

## Conclusão

A customização do Django Admin transforma uma ferramenta padrão em um **painel administrativo poderoso, seguro e produtivo**.

Dominar o Admin é um diferencial real para desenvolvedores Django.

