import requests
from bs4 import BeautifulSoup

parada = input("Numero de la parada del bus: ")

response = requests.get('https://www.emtvalencia.es/QR.php?sec=est&p=' + parada)

soup = BeautifulSoup(response.content, 'html.parser')

span = soup.find('span', style="position: relative; top: -5px;")

time = span.get_text().strip().replace(u'\xa0', u' ')

img_tag = soup.find('img', src="http://www.emtvalencia.es/EmtEsquemas_graphics/line-icons/40bigW.gif")
num = img_tag.get("title")

print(num + " - " + time)