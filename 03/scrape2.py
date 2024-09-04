from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Crear una sesión HTML
session = HTMLSession()

# URL de la página a analizar
url = 'https://www.guinotprunera.com/es/alquiler-pisos-pisos/en-barcelona-barcelona/<params>'
response = session.get(url)

# Renderizar el contenido dinámico (si es necesario)
response.html.render(wait=2)

# Usar BeautifulSoup para analizar el HTML
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)
# Encontrar el contenedor principal
container = soup.find('div', class_='listadoInmueblesContainer')

if container:
    # Encontrar todos los elementos "ficha" dentro del contenedor, no importa cuán anidados estén
    fichas = container.find_all('div', class_='ficha')

    # Extraer la información de cada "ficha"
    for ficha in fichas:
        # Título y enlace
        title_tag = ficha.select_one('.DLFichaTituloDestacado a')
        title = title_tag.text.strip() if title_tag else "Sin título"
        link = title_tag['href'] if title_tag else "Sin enlace"
        
        # Características
        features_tag = ficha.select_one('.DLCaracteristicas')
        features = features_tag.text.strip().replace('\n', '').replace('|', '| ') if features_tag else "Sin características"

        # Precio
        price_tag = ficha.select_one('.DLFichaPrecioDestacada span')
        price = price_tag.text.strip() if price_tag else "Sin precio"
        
        # Imprimir los resultados
        print(f"Título: {title}")
        print(f"Link: {link}")
        print(f"Características: {features}")
        print(f"Precio: {price}")
        print("-" * 40)
else:
    print("No se encontró el contenedor de listado de inmuebles.")
