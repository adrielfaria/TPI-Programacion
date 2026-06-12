from validaciones import pedir_numero   # Se importa la función pedir_numero desde el módulo validaciones
from operaciones import agregar_pais, actualizar_pais, buscar_pais
from filtros import filtrar_paises_por
from ordenar import ordenar_paises
from estadisticas import mostrar_estadisticas
from archivo import leer_filas

def salir():
    print('Terminando la ejecuccion del programa')
    return False

def mostrar_menu():
    opciones = {
        '1': lambda: agregar_pais(leer_filas()),
        '2': lambda: actualizar_pais(leer_filas()),
        '3': lambda: buscar_pais(leer_filas()),
        '4': filtrar_paises_por,
        '5': ordenar_paises,
        '6': lambda: mostrar_estadisticas(leer_filas()),
        '7': salir
    }
    while True:
        print("\n===== GESTIÓN DE PAÍSES =====")
        print("1) Agregar país")
        print("2) Actualizar país")
        print("3) Buscar país")
        print("4) Filtrar países")
        print("5) Ordenar países")
        print("6) Mostrar estadísticas")
        print("7) Salir")

        opcion = pedir_numero("\nSeleccione una opción: ")

        funcion = opciones.get(opcion)

        if funcion:
            resultado = funcion()
            if resultado is False:
                break

        else: print('Opcion Invalida')


mostrar_menu()