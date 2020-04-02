import re
import requests

def encontrarEmailsDaPagina(url):

    request = requests.get(url)
    pagina = str(request.text)

    # Tem esse r antes das aspas para transformar em um string 'crua'
    ex = r'[\w\.]+@[\w]+\.[a-z]+(\.[a-z]+)?'

    res2 = re.finditer(ex, pagina)
    for i in res2:
        print(i.group())

url = 'http://www.jucepi.pi.gov.br/index.php'
encontrarEmailsDaPagina(url)