Os **Models** são o núcleo do Django ORM. Eles representam a estrutura dos dados da aplicação, definem como as informações são armazenadas no banco de dados e como são manipuladas em Python.

Cada model é uma classe que herda de `django.db.models.Model`, e cada atributo da classe representa um campo da tabela no banco de dados.

Nesta seção, você aprenderá desde os tipos básicos de campos até a criação de campos personalizados.

## Conteúdos

1. **[Field Types](Fields_types.md)**
   Estudo dos principais **tipos de campos disponíveis no Django**, como campos de texto, números, datas, relacionamentos e campos especiais.
   Aqui você aprende **qual campo usar em cada situação**.

2. **[Field Options](Field_options.md)**
   Opções que controlam o **comportamento dos campos**, como validação, valores padrão, unicidade, índices e aparência no admin e formulários.
   Essencial para criar models **robustos e bem definidos**.

3. **[Custom Fields](Custom_fields.md)**
   Criação de **campos personalizados** para casos em que os campos nativos do Django não são suficientes.
   Aborda normalização de dados, validações avançadas, integração com forms e migrations.

