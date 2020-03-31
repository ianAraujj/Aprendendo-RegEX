# Aprendendo-RegEX
Projeto que apresenta as sintaxe básica das Expressões Regulares e também a classe Regex.

## O que é RegEX (regular expressions)
Expressões Regulares são usadas para identificar um padrão em uma string. É uma forma matemática usada para calcular e identificar certos caracteres usados para definir padrões numa cadeira de caracteres (strings).

Uma expressão regular pode definir um padrão de busca em um documento

## Buscas
### * Exemplo 01: Busca Literal

Ex: /Ian Luccas/g

Esse exemplo pode ser traduzido parar: /[I][a][n]\s[L][u][c][c][a][s]/g Repare que o caractere vazio é representado por \s

Esse mesmo exemplo só que desconsiderando letras maiúsculas e minúsculas: /[Ii][aA][nN]\s[Ll][uU][cC][cC][aA][sS]/g

Ou seja, a expressão regular procura a string 'IAN' no texto

Detalhe: Há caracteres que já são especiais para as expressões regulares. A expressão /./g significa qualquer caractere. Caso o caractere '.' faça parte da sua busca, então temos que usar uma barra invertida antes do caractere especial, assim '/\\\./g'

### * Exemplo 02: Buscar todos os telefone que terminan em 99

/-\d\d99/g: O '\d' significa qualquer dígito de 0 a 9

### * Exemplo 03: Encontrar, dentro da sequência de nucleotídios (DNA), uma sequência em que tenha 'G' seguindo de 2 nucleotídos qualquer e depois seguido de um 'A'

/G..A/g

### * Exemplo 04:
O meta caractere ^ represneta o INÍCIO da linha, ou seja, o início de cada parágrafo. O exemplo /^Eu/gm encontra todos os parágrafos que começam com 'Eu'

O \w representa qualquer caractere alfanumérico

## Aplicações RegEX
* Lista telefônica
* Código genético
