# Tratamento de dados em Python

## Sobre o projeto

Este projeto foi desenvolvido como exercício prático de Python, com foco no tratamento de dados textuais e na transformação de informações brutas em uma saída organizada no formato de tabela.

A proposta do programa é simular uma pequena base de dados em texto, onde cada registro contém nome, idade e cidade. A partir dessa lista inicial, o código separa os campos, remove espaços desnecessários, trata a idade, converte valores numéricos e exibe os dados de forma padronizada no terminal.

## Objetivo do exercício

O objetivo principal é praticar conceitos fundamentais de Python aplicados ao tratamento de dados, como manipulação de strings, listas, laços de repetição, conversão de tipos e formatação de saída.

Neste exercício, cada linha da lista representa um registro textual no formato `nome, idade, cidade`. O programa utiliza `split()` para separar os campos, `strip()` para limpar espaços extras, `replace()` para remover a palavra “anos” da idade e `int()` para converter a idade em número inteiro.

## Funcionalidades

* Recebe uma lista com dados textuais no formato nome, idade e cidade
* Percorre todos os registros utilizando estrutura de repetição
* Separa os dados de cada linha com `split()`
* Remove espaços desnecessários com `strip()`
* Remove a palavra “anos” do campo de idade com `replace()`
* Converte a idade para número inteiro com `int()`
* Exibe os dados tratados em formato de tabela no terminal
* Organiza a saída com alinhamento de colunas usando f-strings

## Tecnologias utilizadas

* Python 3

## Como executar o projeto

1. Certifique-se de que o Python esteja instalado no computador.
2. Baixe ou copie o arquivo do projeto.
3. Execute o arquivo pelo terminal ou por uma IDE de sua preferência, como:
   * PyCharm
   * Visual Studio Code
   * IDLE

## Exemplo de Uso

Entrada
```python
lista = [
    "João, 14 anos, Pereira Barreto",
    "Pedro, 20 anos, Ilha Solteira",
    "Airton, 47 anos, Santa Fé do Sul",
    "Pablo, 34 anos, Três Lagoas"
]
```

Saída
```txt
Nome       | Idade      | Cidade              
----------------------------------------------
João       | 14         | Pereira Barreto     
Pedro      | 20         | Ilha Solteira       
Airton     | 47         | Santa Fé do Sul     
Pablo      | 34         | Três Lagoas         
```


