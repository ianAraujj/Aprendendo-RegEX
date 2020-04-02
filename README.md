# Aprendendo-RegEX
Projeto que apresenta as sintaxe básica das Expressões Regulares e também a classe Regex.

## Site para testar

[regexr.com](https://regexr.com/)

## Site para exercícios
[Regex Cross word](https://regexcrossword.com/)

## O que é RegEX (regular expressions)
Expressões Regulares são usadas para identificar um padrão em uma string. É uma forma matemática usada para calcular e identificar certos caracteres usados para definir padrões numa cadeira de caracteres (strings).

Uma expressão regular pode definir um padrão de busca em um documento.

## Aplicações RegEX
* Lista telefônica
* Código genético
* Corretor ortográfico

## Parte I: Apresentação dos Metacaracteres
### * Exemplo 01: Busca Literal

Ex: /Ian Luccas/g

Esse exemplo pode ser traduzido parar: /```[I][a][n]\s[L][u][c][c][a][s]```/g Repare que o caractere vazio é representado por \s

Esse mesmo exemplo só que considerando letras maiúsculas e minúsculas: /```[Ii][aA][nN]\s[Ll][uU][cC][cC][aA][sS]```/g

Detalhe: Há caracteres que já são especiais para as expressões regulares. A expressão /```.```/g significa qualquer caractere. Caso o caractere '.' faça parte da sua busca, então temos que usar uma barra invertida antes do caractere especial, assim '/```\.```/g'

### * Exemplo 02: 

Buscar todos os telefones que terminan em 99

/```-\d\d99```/g: O '\d' significa qualquer dígito de 0 a 9

### * Exemplo 03: 

Encontrar, dentro da sequência de nucleotídios (DNA), uma sequência em que tenha 'G' seguindo de 2 nucleotídos qualquer e depois seguido de um 'A'

/```G..A```/g

### * Exemplo 04:
O meta caractere ^ represneta o INÍCIO da linha, ou seja, o início de cada parágrafo. O exemplo /```^Eu```/gm encontra todos os parágrafos que começam com 'Eu'. Detalhe que o 'm' do 'gm' vem de multilines, isso são as FLAGS da nossa busca, a flag multilines precisa ser ativada quando a sua aplicação está trabalhando com múltiplos parágrafos. O 'g' vem de global.

O \w representa qualquer caractere alfanumérico

### * Exemplo 05:

Expressão regular para verificar se você digitou o ponto final em todos os parágrafos:

/```\w$```/gm

### * Exemplo 06: 

Buscar todos os caracteres de 'a' até 'f'. Para isso vamos usar os denotadores (criadores de classe), ou seja, vamos definir nosso próprio cojunto de caracteres para a bucsa.

/```[abcdef]```/gm ou melhor ainda /```[a-f]```/gm

Isso funciona também com dígitos: /```[1-3]```/gm
    
## Parte II: Quantificadores

### Refazendo o exemplo 02 usando quantificadores

/```-\d{2}99```/g

Além  de especificar a quantidade de caracteres, os quantificadores também servem quando você não sabe exatamente quantos caracteres são, mas tem o valor do mínimo e do máximo.

### * Exemplo 07

Encontrar as palavras que começam com a literal 'C' e terminam com a literal 'o'

/```C\w{1,}o```/gm

### * Exemplo 08

Seleciona as palavra 'você' no singular e no plural

/```vocês?```/gm

O '?' significa que o caractere antes dele pode ou não existir. O diferente aqui é que quando encontramos um '?' na expressão regular, devemos observar o caractere anterior e não o seguinte. O '?' pode ser usado para identicicar urls com http ou https, seria assim: /```https?```/gm

O * é uma forma prática de informar que naquela posição da expressão pode haver quantas vezes possíveis aquele caractere, mas também pode não haver a ocorrência de nenhum. O '?' pode definir apenas a existência e a não existência daquele caractere. Esse mesmo exemplo pode ser feito por outras formas: /```https{0,1}```/gm

A expressão regular usando o * ou o ? é indicada porque fica mais simples para ser compreendida.

### * Exemplo 09

Selecione os parágrafos de uma página html

Para isso, temos que usar uma expressão regular preguiçosa e não uma expressão regular fominha. A expressão regular preguiçosa seleciona o mínimo necessário, esse modo vai selecionar o texto assim que for encontrado algo que case com o que foi especificado na expressão. O símbolo para a expressão preguiçosa é o '?'

/```<p>.*?</p>```/gm

## Parte III: Operadores Lógicos

### * Exemplo 10

Selecione todos os títulos h2 e h3 da página html

/```<h(3|2)>.*</h(3|2)>```/gm

Foi usado os parenteses para definir um conjunto e o caractere '|' para definir o operador lógico OU

### * Exemplo 11

Selecione tudo que não for 'a', 'e' e 'i'

Para selecionar tudo o que tiver 'a', 'e' e 'i' fazemos: /```[aei]```/gm

A negação disso fica: /```[^aei]```/gm

Operador de Negação: 
selecionar tudo o que não é dígito ```\D``` 
selecionar tudo o que não é palavra ```\W```

### * Exemplo 12

Selecione na lista telefônica todas as Vitórias que tiverem o sobrenome Medeiros.

/```Vitória\s(?=Medeiros)``` /gm

A Negação disso, ou seja, todas as Vitórias que não tiverem o sobrenome Medeiros, seria: /```Vitória\s(?!Medeiros)``` /gm

### * Exemplo 13

Selecione no texto as palavras que estão duplicadas uma após a outra, por exemplo, "Estado ```da da``` arte com foco ...". Essa seleção pode ser usada como maneira de correção ortográfica.

/```\b(\w+)\s\1\b``` /gm

O \b é um delimitador de palavras, limitando o início e o fim da palavra. o \1 faz referência ao primeiro grupo definido '(\w+)', um grupo está sempre entre parenteses. Em outras palavras, no texto o que tem em '(\w+)' tem que ser IGUAL ao que tem em \1

### * Refazendo o Exemplo 10

No caso da solução dada pelo exemplo 10, se na página html tivesse algo do tipo: ```<h2> Parágrafo <\h3>``` A expressão iria selecionar. Para resolver esse problema, vamos usar o conceito de referência apresentado anteriormente:
  
/```<h(3|2)>.*</h\1>```/gm
