# Aprendendo-RegEX
Projeto que apresenta as sintaxe básica das Expressões Regulares e também a classe Regex.

## Site para testar

[regexr.com](https://regexr.com/)

## O que é RegEX (regular expressions)
Expressões Regulares são usadas para identificar um padrão em uma string. É uma forma matemática usada para calcular e identificar certos caracteres usados para definir padrões numa cadeira de caracteres (strings).

Uma expressão regular pode definir um padrão de busca em um documento

## Aplicações RegEX
* Lista telefônica
* Código genético

## Apresentação dos Metacaracteres
### * Exemplo 01: Busca Literal

Ex: /Ian Luccas/g

Esse exemplo pode ser traduzido parar: /[I][a][n]\s[L][u][c][c][a][s]/g Repare que o caractere vazio é representado por \s

Esse mesmo exemplo só que desconsiderando letras maiúsculas e minúsculas: /[Ii][aA][nN]\s[Ll][uU][cC][cC][aA][sS]/g

Ou seja, a expressão regular procura a string 'IAN' no texto

Detalhe: Há caracteres que já são especiais para as expressões regulares. A expressão /./g significa qualquer caractere. Caso o caractere '.' faça parte da sua busca, então temos que usar uma barra invertida antes do caractere especial, assim '/\\\./g'

### * Exemplo 02: 

Buscar todos os telefones que terminan em 99

/-\d\d99/g: O '\d' significa qualquer dígito de 0 a 9

### * Exemplo 03: 

Encontrar, dentro da sequência de nucleotídios (DNA), uma sequência em que tenha 'G' seguindo de 2 nucleotídos qualquer e depois seguido de um 'A'

/G..A/g

### * Exemplo 04:
O meta caractere ^ represneta o INÍCIO da linha, ou seja, o início de cada parágrafo. O exemplo /^Eu/gm encontra todos os parágrafos que começam com 'Eu'. Detalhe que o 'm' do 'gm' vem de multilines, isso são as FLAGS da nossa busca, a flag multilines precisa ser ativada quando a sua aplicação está trabalhando com múltiplos parágrafos. O 'g' vem de global.

O \w representa qualquer caractere alfanumérico

### * Exemplo 05:

Expressão regular para verificar se você digitou o ponto final em todos os parágrafos:

/\w$/gm

### * Exemplo 06: 

Buscar todos os caracteres de 'a' até 'f'. Para isso vamos usar os denotadores (criadores de classe), ou seja, vamos definir nosso próprio cojunto de caracteres para a bucsa.

/[abcdef]/gm ou melhor ainda /[a-f]/gm

Isso funciona também com dígitos: /[1-3]/gm
    
## Quantificadores
