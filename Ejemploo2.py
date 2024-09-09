def calcular(a, b, c):

    res = a * b + c
    return res


def obtener_entrada_numerica(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


def principal():

    print("Ingrese los valores para realizar el cálculo.")
    x = obtener_entrada_numerica("Ingrese el valor de a: ")
    y = obtener_entrada_numerica("Ingrese el valor de b: ")
    z = obtener_entrada_numerica("Ingrese el valor de c: ")

    resultado = calcular(x, y, z)
    print(f"El resultado de {x} * {y} + {z} es: {resultado}")


if __name__ == "__main__":
    principal()

