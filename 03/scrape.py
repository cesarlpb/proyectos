from requests_html import HTMLSession

session = HTMLSession()
# URL de la página a analizar
url = 'https://www.guinotprunera.com/es/alquiler-pisos-pisos/en-barcelona-barcelona/<params>'
response = session.get(url)

response.html.render(wait=2)  # Renderiza la página, ejecutando JavaScript

# Ahora puedes procesar la página como necesites
container = response.html.find('.listadoInmueblesContainer', first=True)
if container:
    print("Contenido cargado correctamente.")
    for item in container.find('div'):
        print(item.text)  # O haz lo que necesites con los divs
else:
    print("No se encontró el contenedor de listado de inmuebles.")


