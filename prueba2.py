def sumar(a, b):
    """Función simple que suma dos números."""
    return a + b


def es_par(numero):
    """Función que verifica si un número es par."""
    return numero % 2 == 0


# --- Pruebas rápidas en consola ---
if __name__ == "__main__":
    print("=== Probando funciones ===")

    resultado_suma = sumar(5, 3)
    print(f"5 + 3 = {resultado_suma}")

    numero_test = 4
    print(f"¿El {numero_test} es par?: {es_par(numero_test)}")
