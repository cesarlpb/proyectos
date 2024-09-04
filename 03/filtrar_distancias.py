def leer_distancias(file_path):
    distancias = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        ciudad = None
        for line in lines:
            if line.startswith('Ciudad:'):
                ciudad = line.split(':')[1].strip()
            elif line.startswith('  Duración en coche:'):
                duracion = int(line.split(':')[1].strip().split()[0])  # Extrae el tiempo en minutos
                distancias[ciudad] = duracion
    return distancias

def combinar_distancias(file_1, file_2):
    distancias_1 = leer_distancias(file_1)
    distancias_2 = leer_distancias(file_2)

    # Combinar los resultados en una lista de diccionarios
    ciudades = set(distancias_1.keys()).union(set(distancias_2.keys()))
    resultado = []
    for ciudad in ciudades:
        duracion_1 = distancias_1.get(ciudad, 'N/A')
        duracion_2 = distancias_2.get(ciudad, 'N/A')
        resultado.append({'ciudad': ciudad, 'distancia_1': duracion_1, 'distancia_2': duracion_2})

    return resultado

def imprimir_resultado_ordenado(resultado, key):
    # Ordenar la lista por la clave proporcionada (distancia_1 o distancia_2)
    resultado_ordenado = sorted(resultado, key=lambda x: x[key] if x[key] != 'N/A' else float('inf'))
    
    # Imprimir la lista ordenada
    for item in resultado_ordenado:
        print(f"Ciudad: {item['ciudad']}")
        print(f"  Duración 1 en coche: {item['distancia_1']} mins")
        print(f"  Duración 2 en coche: {item['distancia_2']} mins")
        print("-" * 40)

# Especifica las rutas a tus archivos
file_1 = 'distancias_oficina.txt'
file_2 = 'distancias_prat.txt'

# Combina las distancias de ambos archivos
resultado = combinar_distancias(file_1, file_2)

# Imprime el resultado ordenado por distancia_1
imprimir_resultado_ordenado(resultado, 'distancia_1')

# Si quieres ordenar por 'distancia_2', simplemente cambia la clave:
# imprimir_resultado_ordenado(resultado, 'distancia_2')