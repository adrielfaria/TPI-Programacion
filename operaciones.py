from validaciones import pedir_texto, pedir_numero
from archivo import escribir_pais, reescribir_archivo


def buscar_pais(paises):
    # Pedir el nombre a buscar y guardar los resultados
    nombre_buscado = pedir_texto("Ingrese el nombre del país: ").strip().lower()
    encontrados = []

    for pais in paises:
        if nombre_buscado in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países.")
        return

    print("\nPaíses encontrados:")

    for pais in encontrados:
        print(
            f"{pais['nombre']} | "
            f"Población: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} | "
            f"Continente: {pais['continente']}"
        )


def agregar_pais(paises):
    # Solicitar datos del país y guardarlos en la lista
    nombre = pedir_texto("Nombre del país: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    poblacion = int(pedir_numero("Población: "))
    superficie = int(pedir_numero("Superficie: "))
    continente = pedir_texto("Continente: ").strip()

    escribir_pais(nombre, poblacion, superficie, continente)
    print("País agregado correctamente.")


def actualizar_pais(paises):
    # Buscar el país por nombre y actualizar sus datos
    nombre = pedir_texto("Ingrese el país a actualizar: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = int(pedir_numero("Nueva población: "))
            pais["superficie"] = int(pedir_numero("Nueva superficie: "))
            reescribir_archivo(paises)
            print("País actualizado correctamente.")
            return

    print("País no encontrado.")