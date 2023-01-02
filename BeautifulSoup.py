'''
It WORK !!!
'''
'''
First we have to import on the console
 "pip intall "

'''



from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://listado.mercadolibre.com.co/targetas-video#D[A:targetas%20video]"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
resultados = soup.find_all('div', class_="ui-search-result__wrapper shops__result-wrapper")
    
    
with open('busqueda_targeta.csv', 'w', encoding='utf8', newline='') as archivo:  
    
    escritor = writer(archivo)
    encabezado = ['Articulo', 'Precio']
    escritor.writerow(encabezado)
    
    for i in resultados: 
        titulo = i.find('h2', class_="ui-search-item__title shops__item-title").text
        precio = i.find('span', class_="price-tag-fraction").text
        info = [titulo, precio]
        escritor.writerow(info)
