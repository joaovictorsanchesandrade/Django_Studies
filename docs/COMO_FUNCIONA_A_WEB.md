# Como funciona a web?

# Dicionário de siglas

- **WWW (World Wide Web)** – Conjunto de páginas e recursos interligados por links.
- **DNS (Domain Name System)** – Sistema responsável por traduzir nomes de domínio em endereços IP.

---

## O que é a Internet?

A **Internet** é uma rede global que interconecta milhões de dispositivos, como computadores, celulares e servidores, permitindo a troca de dados entre eles.

Já a **World Wide Web (WWW)** é uma **aplicação que roda sobre a Internet**, formada por páginas interligadas através de links. Ou seja:

- Internet → infraestrutura (cabos, roteadores, servidores)
- Web → serviço que usa essa infraestrutura para exibir páginas

---

## Endereço IP e Portas

Para acessar um site, seu computador precisa se conectar ao **endereço IP** e à **porta** do servidor onde o site está hospedado.

Fluxo básico de comunicação:

```
Cliente (seu computador) →Internet →IP:Porta (Servidor)

```

O servidor recebe a **requisição (request)** e responde com os dados solicitados (HTML, CSS, imagens, etc).

---

## Mas por que não usamos IP e porta diretamente?

Normalmente acessamos sites usando **nomes de domínio**, como `google.com`, e não números como `142.250.72.14:80`.

Isso acontece porque existe o **DNS (Domain Name System)**, que funciona como um tradutor.

Fluxo com DNS:

```
Cliente → DNS → Domínio
                 ↓
              IP:Porta

```

O DNS recebe o domínio, procura o IP e a porta correspondentes e devolve essa informação para o cliente. A partir daí, a conexão com o servidor acontece normalmente.

---

## Analogia

Pense no DNS como uma **agenda telefônica gigante**:

- Você procura um nome (domínio)
- Ele te devolve o número (IP e porta)

Exemplo:

```
google.com →IP:Porta

```

A diferença é que, em vez de contatos pessoais, o DNS armazena milhões de endereços de servidores ao redor do mundo.