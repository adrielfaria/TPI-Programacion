import csv
ARCHIVO = 'paises_prueba.csv'

def leer_filas() -> list:
    """
    Lee el archivo csv de países y retorna sus filas como lista de diccionarios.

    Saltea las filas vacias y normaliza los datos: convierte población y superficie a enteros y elimina espacios en el nombre del continente.
    """
    filas = []
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Saltear fila si todos los campos estan vacios
                if not any(fila.values()):
                    continue
                filas.append({
                'nombre': fila['nombre'],
                'poblacion': int(fila['poblacion']),
                'superficie': int(fila['superficie']),
                'continente': fila['continente'].strip()
            })
    except FileNotFoundError:
        print(f'El archivo {ARCHIVO} no existe.')
    except ValueError:
        print('Error: el archivo tiene un formato incorrecto.')
    except Exception as e:
        print(f'Error inesperado: {e}')
    return filas   
