# Projeto Django-FlashCards-Solid

O projeto `django-flashcards-solid` é uma aplicação web construída utilizando o framework Django, com um foco especial em aderir a boas práticas de clean code, princípios SOLID e implementando os 12 fatores para garantir uma aplicação segura, eficiente e escalável.

O projeto inicialmente é um teste, pensando em uma aplicação minha para venda de cursos.


## Tecnologias e Conceitos Utilizados

- **Django**: Framework web de alto nível para desenvolvimento rápido e limpo.
- **Docker**: Containerização da aplicação, permitindo a entrada de novos colaboradores de maneira fácil, e isolamento das dependências do projeto.
- **Clean Code**: Adoção de boas práticas para garantir código claro, legível e de fácil manutenção.
- **SOLID Principles**: Aplicação dos princípios SOLID para promover a flexibilidade e extensibilidade do código.
- **12 Fatores**: Implementação dos 12 fatores para construir aplicações robustas, escaláveis e fáceis de gerenciar.


## Práticas Adotadas

1 - Primeira prática adotada (12 fatores) foi a construção utilizando docker com todas as dependências em suas versões declaradas, isoladas e autocontidas. Permitindo a introdução de novos colaboradores e migração de ambiente com facilidade.

2 - Segunda prática adotada (12 fatores) construção utilizando variavéis de ambientes ao inves de deixar no settings.py exposto.
