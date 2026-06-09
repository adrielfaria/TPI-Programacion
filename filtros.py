import csv
from validaciones import pedir_texto, pedir_numero
 
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

def filtrar_por_continente() -> None:
    """
    Pide al usuario ingresar el nombre del continente por el que desea filtrar y devuelve información de los paises que pertenecen a dicho continente.
    """
    continente = pedir_texto('Ingrese el nombre del continente por el que desea filtrar: ')
    paises = leer_filas()
    resultados = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            resultados.append(pais)
    if not resultados:
        print('No se han encontrado países en ese continente.')
        return
    for pais in resultados:
        print(f'Pais: {pais["nombre"]}, Poblacóon: {pais["poblacion"]}, Superficie: {pais["superficie"]}')

def filtrar_por_poblacion() -> None:
    """
    Pide al usuario ingresar una población mínima y una máxima y devuelve los países que se encuentran dentro de ese rango.
    """
    minima = int(pedir_numero('Población mínima: '))
    maxima = int(pedir_numero('Población máxima: '))
    paises = leer_filas()
    resultados = []
    for pais in paises:
        if minima <= pais['poblacion'] <= maxima:
            resultados.append(pais)
    if not resultados:
        print('No se han encontrado países en ese rango de población.')
        return
    for pais in resultados:
        print(f'Pais: {pais["nombre"]}, Población: {pais["poblacion"]}, Superficie: {pais["superficie"]} Continente: {pais["continente"]}')

def filtrar_por_superficie() -> None:
    """
    Pide al usuario ingresar una superficie mínima y una máxima y devuelve los países que se encuentran dentro de ese rango.
    """
    minima = int(pedir_numero('Superficie mínima: '))
    maxima = int(pedir_numero('Superficie máxima: '))
    paises = leer_filas()
    resultados = []
    for pais in paises:
        if minima <= pais['superficie'] <= maxima:
            resultados.append(pais)
    if not resultados:
        print('No se han encontrado países en ese rango de superficie.')
        return
    for pais in resultados:
        print(f'Pais: {pais["nombre"]}, Población: {pais["poblacion"]}, Superficie: {pais["superficie"]} Continente: {pais["continente"]}')




