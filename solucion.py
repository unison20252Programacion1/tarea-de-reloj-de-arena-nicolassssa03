# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <=0:
        print("Error: La altura debe ser un entero positivo")
        return

    #Primera Parte: Decreciente
    for i in range(m):
        espacios = i
        caracteres = 2 * (m - i) - 1
        print(" " * espacios + s * caracteres)

    #Segunda Parte: Creciente
    for i in range(1,m):
        espacios = m - 1 - i
        caracteres = 2 * i + 1
        print(" " * espacios + s * caracteres)
