# Diccionario que almacena los personajes y sus estadísticas base.
# Cada personaje es una clave, y su valor es otro diccionario con sus atributos.
personajes = {
    # --- Personajes de DC (Principales) ---
    "Superman": {"poder": 100, "destreza": 85, "velocidad": 95, "inteligencia": 75},
    "Batman": {
        "poder": 70,
        "destreza": 90,
        "velocidad": 70,
        "inteligencia": 100,
    },  # Alta inteligencia y destreza, compensando su falta de poderes sobrehumanos.
    "Flash": {
        "poder": 60,
        "destreza": 80,
        "velocidad": 98,
        "inteligencia": 80,
    },  # Velocidad extrema.
    "Wally West": {
        "poder": 65,
        "destreza": 85,
        "velocidad": 100,
        "inteligencia": 85,
    },  # Considerado el velocista más rápido.
    "Wonder Woman": {"poder": 95, "destreza": 90, "velocidad": 90, "inteligencia": 90},
    "Green Lantern": {"poder": 90, "destreza": 75, "velocidad": 85, "inteligencia": 80},
    "Aquaman": {
        "poder": 85,
        "destreza": 70,
        "velocidad": 75,
        "inteligencia": 70,
    },  # Fuerza y velocidad aumentadas, especialmente en el agua.
    #  Personajes de Marvel
    "Hulk": {
        "poder": 100,
        "destreza": 60,
        "velocidad": 60,
        "inteligencia": 60,
    },  # Fuerza bruta máxima, pero menor agilidad y velocidad.
    "Iron Man": {
        "poder": 90,
        "destreza": 85,
        "velocidad": 80,
        "inteligencia": 100,
    },  # Genio tecnológico con armadura versátil.
    "Captain America": {
        "poder": 80,
        "destreza": 95,
        "velocidad": 65,
        "inteligencia": 75,
    },  # Máximo potencial humano y experto en combate.
    "Thor": {
        "poder": 98,
        "destreza": 85,
        "velocidad": 85,
        "inteligencia": 70,
    },  # Poder divino y gran resistencia.
    # --- Personajes de The Boys ---
    "Homelander": {
        "poder": 100,
        "destreza": 80,
        "velocidad": 95,
        "inteligencia": 40,
    },  # Muy poderoso pero emocionalmente inestable y menos táctico.
    "Butcher": {
        "poder": 75,
        "destreza": 70,
        "velocidad": 60,
        "inteligencia": 80,
    },  # Estratega experto con fuerza aumentada por suero.
    # --- Personajes de Breaking Bad ---
    "Walter White": {
        "poder": 30,
        "destreza": 40,
        "velocidad": 10,
        "inteligencia": 100,
    },  # Intelecto nivel genio, baja capacidad física.
    "Jesse Pinkman": {
        "poder": 20,
        "destreza": 60,
        "velocidad": 20,
        "inteligencia": 50,
    },  # Astucia callejera, sin gran poder físico.
    "Gus Fring": {
        "poder": 40,
        "destreza": 70,
        "velocidad": 5,
        "inteligencia": 95,
    },  # Mente maestra criminal y extremadamente metódico.
}


# Función para calcular el ranking general basado en pesos específicos para cada estadística.
def calcular_ranking(stats):
    # Se calcula la suma ponderada: el poder vale más (40%) que los demás (30% cada uno).
    total = (
        (stats["poder"] * 0.4)
        + (stats["destreza"] * 0.3)
        + (stats["velocidad"] * 0.3)
        + (stats["inteligencia"] * 0.3)
    )
    # Se normaliza dividiendo por 1.3 (la suma de los pesos) para que el máximo sea 100.
    normalized_total = total / 1.3
    # Retorna el valor redondeado, asegurando que el mínimo sea 1.
    return max(1, round(normalized_total))


# Función para mostrar una lista de personajes ordenada por una estadística seleccionada.
def mostrar_ranking_por_stat(stat_elegida):
    print(f"\n--- Ranking por {stat_elegida.capitalize()} ---")
    # Se ordena el diccionario convirtiéndolo en lista de tuplas y usando la estadística como clave de orden.
    ranking_ordenado = sorted(
        personajes.items(), key=lambda item: item[1][stat_elegida], reverse=True
    )
    # Se recorre la lista ordenada para imprimir los resultados.
    for nombre, stats in ranking_ordenado:
        print(f"{nombre}: {stats[stat_elegida]}")


# Función principal que maneja el menú interactivo para el usuario.
def main():
    while True:
        # Imprime las opciones disponibles en el menú.
        print("\n--- Menú de Ranking de Personajes ---")
        print("1. Ranking General")
        print("2. Ranking por Poder")
        print("3. Ranking por Destreza")
        print("4. Ranking por Velocidad")
        print("5. Ranking por Inteligencia")
        print("6. Salir")

        # Captura la elección del usuario.
        opcion = input("Elige una opción: ")

        # Lógica para procesar la opción elegida.
        if opcion == "1":
            print("\n--- Ranking General ---")
            # Calcula y muestra el ranking calculado para cada personaje.
            for nombre, stats in personajes.items():
                score = calcular_ranking(stats)
                print(f"{nombre} tiene un ranking de: {score}%")
        elif opcion == "2":
            mostrar_ranking_por_stat("poder")
        elif opcion == "3":
            mostrar_ranking_por_stat("destreza")
        elif opcion == "4":
            mostrar_ranking_por_stat("velocidad")
        elif opcion == "5":
            mostrar_ranking_por_stat("inteligencia")
        elif opcion == "6":
            # Mensaje de despedida y cierre del programa.
            print("¡Hasta luego!")
            break
        else:
            # Manejo de entradas no válidas.
            print("Opción no válida. Inténtalo de nuevo.")


# Punto de entrada del script: asegura que main() se ejecute solo si el archivo se corre directamente.
if __name__ == "__main__":
    main()
