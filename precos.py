import requests
import bs4

#declarando url do site 
url = "https://www.kabum.com.br/produto/134176/cadeira-gamer-husky-gaming-tempest-700-preto-com-almofadas-descanso-para-pernas-retratil-reclinavel-hgma074"
#Entregando permissão de acesso como navegador
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
#Acessando site
req = requests.get(url, headers = headers)
html = bs4.BeautifulSoup(req.content, 'html.parser')
#Elementos de busca
    #Declarando titulo
title_element = html.find(class_="cMCMNo")
    #Convertendo para str
title_content = title_element.string
    #Declarando preço 
price_element = html.find(class_="finalPrice")
    #Convertendo para st
price_content = price_element.string

#Resultado
print(f':{title_content} preço é: {price_content}')

