from requests_html import HTMLSession

session = HTMLSession()
# URL de la página a analizar

with open('.env') as f:
    lines = f.read().splitlines()

ENV = {}
for line in lines:
    k, v = line.split('=')
    ENV[k] = v

PARAMS = ENV.get('PARAMS', 'si no hay params se busca con string vacío, sin filtros')
if not PARAMS or PARAMS.startwith('si no hay params'):
    PARAMS = ''

url = f'https://www.guinotprunera.com/es/alquiler-pisos-pisos/en-barcelona-barcelona/{PARAMS}'
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


