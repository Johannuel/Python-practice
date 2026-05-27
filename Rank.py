personajes = {
    # --- DC Characters (Main) ---
    "Superman": {"poder": 100, "destreza": 85, "velocidad": 95, "inteligencia": 75},
    "Batman": {
        "poder": 70,
        "destreza": 90,
        "velocidad": 70,
        "inteligencia": 100,
    },  # High intelligence, high dexterity, but not super powerful or fast
    "Flash": {
        "poder": 60,
        "destreza": 80,
        "velocidad": 98,
        "inteligencia": 80,
    },  # Very high speed
    "Wally West": {
        "poder": 65,
        "destreza": 85,
        "velocidad": 100,
        "inteligencia": 85,
    },  # Even faster than Flash
    "Wonder Woman": {"poder": 95, "destreza": 90, "velocidad": 90, "inteligencia": 90},
    "Green Lantern": {"poder": 90, "destreza": 75, "velocidad": 85, "inteligencia": 80},
    "Aquaman": {
        "poder": 85,
        "destreza": 70,
        "velocidad": 75,
        "inteligencia": 70,
    },  # Strong, decent speed in water
    # --- Marvel Characters ---
    "Hulk": {
        "poder": 100,
        "destreza": 60,
        "velocidad": 60,
        "inteligencia": 60,
    },  # Immovable object, but not agile or intellectual
    "Iron Man": {
        "poder": 90,
        "destreza": 85,
        "velocidad": 80,
        "inteligencia": 100,
    },  # Genius, powerful suit
    "Captain America": {
        "poder": 80,
        "destreza": 95,
        "velocidad": 80,
        "inteligencia": 75,
    },  # Peak human, exceptional combatant
    "Thor": {
        "poder": 98,
        "destreza": 85,
        "velocidad": 80,
        "inteligencia": 70,
    },  # God-like power, strong but not a speedster
    # --- The Boys Characters ---
    "Homelander": {
        "poder": 100,
        "destreza": 80,
        "velocidad": 95,
        "inteligencia": 40,
    },  # Powerful, fast, but arrogant and not very smart
    "Butcher": {
        "poder": 75,
        "destreza": 70,
        "velocidad": 60,
        "inteligencia": 80,
    },  # Vought-serum power, but more strategic
    # --- Breaking Bad Characters ---
    "Walter White": {
        "poder": 30,
        "destreza": 40,
        "velocidad": 30,
        "inteligencia": 100,
    },  # Pure intellect
    "Jesse Pinkman": {
        "poder": 20,
        "destreza": 60,
        "velocidad": 60,
        "inteligencia": 50,
    },  # More street-smart, less powerful
    "Gus Fring": {
        "poder": 40,
        "destreza": 70,
        "velocidad": 70,
        "inteligencia": 95,
    },  # Strategic, composed, but no inherent physical power
}


def calcular_ranking(stats):
    total = (
        (stats["poder"] * 0.4)
        + (stats["destreza"] * 0.3)
        + (stats["velocidad"] * 0.3)
        + (stats["inteligencia"] * 0.3)
    )
    # Normalize the score to a 1-100 scale
    normalized_total = total / 1.3
    return max(1, round(normalized_total))


def mostrar_ranking_por_stat(stat_elegida):
    print(f"\n--- Ranking por {stat_elegida.capitalize()} ---")
    # Sort characters by the chosen stat in descending order
    ranking_ordenado = sorted(
        personajes.items(), key=lambda item: item[1][stat_elegida], reverse=True
    )
    for nombre, stats in ranking_ordenado:
        print(f"{nombre}: {stats[stat_elegida]}")


def main():
    while True:
        print("\n--- Menú de Ranking de Personajes ---")
        print("1. Ranking General")
        print("2. Ranking por Poder")
        print("3. Ranking por Destreza")
        print("4. Ranking por Velocidad")
        print("5. Ranking por Inteligencia")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- Ranking General ---")
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
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
