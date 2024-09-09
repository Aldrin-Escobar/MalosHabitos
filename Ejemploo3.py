def calcular_area_rectangulo(base, altura):

    return base * altura

def calcular_area_triangulo(base, altura):

    return 0.5 * base * altura

def obtener_entrada_numerica(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def main():

    print("Calcular el área de un rectángulo:")
    base_rect = obtener_entrada_numerica("Ingrese la base del rectángulo: ")
    altura_rect = obtener_entrada_numerica("Ingrese la altura del rectángulo: ")
    area_rectangulo = calcular_area_rectangulo(base_rect, altura_rect)
    print(f"Área del rectángulo: {area_rectangulo:.2f}")

    print("\nCalcular el área de un triángulo:")
    base_tri = obtener_entrada_numerica("Ingrese la base del triángulo: ")
    altura_tri = obtener_entrada_numerica("Ingrese la altura del triángulo: ")
    area_triangulo = calcular_area_triangulo(base_tri, altura_tri)
    print(f"Área del triángulo: {area_triangulo:.2f}")

if __name__ == "__main__":
    main()
