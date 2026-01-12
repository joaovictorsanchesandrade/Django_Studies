# Ambientes Virtuais

## O que são ambientes virtuais?

Ambientes virtuais são usados para **isolar as dependências de um projeto Python**.

Em outras palavras, eles permitem que cada projeto tenha suas próprias bibliotecas e versões, sem interferir em outros projetos ou no Python instalado no sistema.

## Para que servem?

- Evitam conflitos entre versões de bibliotecas
- Mantêm o sistema limpo (sem “poluir” o Python global)
- Facilitam a reprodução do projeto em outras máquinas
- São essenciais em projetos profissionais e colaborativos

Cada ambiente virtual funciona como um **Python independente**, exclusivo para aquele projeto.

---

## Criando um ambiente virtual

Execute o comando abaixo **na raiz do seu projeto**:

```bash
python -m venv nome_do_seu_ambiente

```

Exemplo:

```bash
python -m venv venv

```

---

## Ativando o ambiente virtual

### Windows

```bash
nome_do_seu_ambiente\Scripts\activate

```

### Linux ou macOS

```bash
source nome_do_seu_ambiente/bin/activate

```

Após ativar, o terminal indicará que o ambiente virtual está em uso (geralmente com o nome do ambiente no início da linha).

---

## Desativando o ambiente virtual

Para sair do ambiente virtual, utilize:

```bash
deactivate

```

> Use esse comando quando encerrar o desenvolvimento ou não for mais trabalhar naquele projeto no momento.
> 

---

## Instalação de dependências

Todo módulo instalado com `pip` **enquanto o ambiente estiver ativado** será instalado **somente nele**, sem afetar outros projetos ou o sistema.

Exemplo:

```bash
pip install requests

```