def main():
    nombre = input("¿Cómo te llamas? ").strip()

    try:
        edad_input = input("¿Cuántos años tienes? ")
        edad = int(edad_input)
    except ValueError:
        print("¡Error! Entrada no válida. Se asignará edad 0.")
        edad = 0

    if edad >= 18:
        print(f"Hola {nombre}, ya eres mayor de edad.")
    else:
        print(f"Hola {nombre}, aún eres menor de edad.")

    frutas = ["Manzana", "Banana", "Cereza", "Fresa"]
    print("\nLista de frutas disponibles:")
    for fruta in frutas:
        print(f" • {fruta}")


if __name__ == "__main__":
    main()
