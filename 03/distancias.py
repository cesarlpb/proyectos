import googlemaps

# Reemplaza con tu clave API de Google Maps
API_KEY = 'api_key'

# Inicializa el cliente de Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Dirección de origen
origen = "<dirección, provincia, país>"

# Lista de ciudades
ciudades = [
    "Badalona",
    "Barcelona",
    "Bigues I Riells",
    "Canovelles",
    "Canoves",
    "Cardedeu",
    "Castellar del Vallès",
    "Cervello",
    "Corbera De Llobregat",
    "Cornella De Llobregat",
    "Dosrius",
    "El Papiol",
    "El Pont De Vilomara i Rocafort",
    "Esparreguera",
    "Granollers",
    "Les Franqueses Del Valles",
    "L'Hospitalet de Llobregat",
    "Llagosta, La",
    "Llinars del Valles",
    "Manresa",
    "Matadepera",
    "Molins De Rei",
    "Montcada I Reixac",
    "Palleja",
    "Parets del Valles",
    "Pineda De Mar",
    "Rellinars",
    "Ripollet",
    "Rubí",
    "Sabadell",
    "Sant Adrià de Besòs",
    "Sant Antoni de Vilamajor",
    "Sant Boi de Llobregat",
    "Sant Feliu de Llobregat",
    "Sant Fost de Campsentelles",
    "Sant Joan Despi",
    "Sant Pere de Vilamajor",
    "Sant Vicenç Dels Horts",
    "Talamanca",
    "Terrassa",
    "Ullastrell",
    "Vacarisses",
    "Vallirana",
    "Vallromanes",
    "Viladecavalls"
]

# Calcular las distancias
distancias = {}
for ciudad in ciudades:
    distancia_result = gmaps.distance_matrix(origen, ciudad + ", Barcelona, Spain", mode="driving")
    distancia = distancia_result['rows'][0]['elements'][0]['distance']['text']
    duracion = distancia_result['rows'][0]['elements'][0]['duration']['text']
    distancias[ciudad] = {'distancia': distancia, 'duracion': duracion}

# Mostrar resultados
for ciudad, info in distancias.items():
    print(f"Ciudad: {ciudad}")
    print(f"  Distancia: {info['distancia']}")
    print(f"  Duración en coche: {info['duracion']}")
    print("-" * 40)
