# Dictionary storing characters and their base stats.
# Each character is a key, and its value is another dictionary with its attributes.
personajes = {
    # --- DC Characters (Main) ---
    "Superman": {"poder": 100, "destreza": 85, "velocidad": 95, "inteligencia": 75},
    "Batman": {
        "poder": 70,
        "destreza": 90,
        "velocidad": 70,
        "inteligencia": 100,
    },  # High intelligence and dexterity, compensating for his lack of superhuman powers.
    "Flash": {
        "poder": 60,
        "destreza": 80,
        "velocidad": 98,
        "inteligencia": 80,
    },  # Extreme speed.
    "Wally West": {
        "poder": 65,
        "destreza": 85,
        "velocidad": 100,
        "inteligencia": 85,
    },  # Considered the fastest speedster.
    "Wonder Woman": {"poder": 95, "destreza": 90, "velocidad": 90, "inteligencia": 90},
    "Green Lantern": {"poder": 90, "destreza": 75, "velocidad": 85, "inteligencia": 80},
    "Aquaman": {
        "poder": 85,
        "destreza": 70,
        "velocidad": 75,
        "inteligencia": 70,
    },  # Increased strength and speed, especially in water.
    #  Marvel Characters
    "Hulk": {
        "poder": 100,
        "destreza": 60,
        "velocidad": 60,
        "inteligencia": 60,
    },  # Maximum brute strength, but lower agility and speed.
    "Iron Man": {
        "poder": 90,
        "destreza": 85,
        "velocidad": 80,
        "inteligencia": 100,
    },  # Technological genius with versatile armor.
    "Captain America": {
        "poder": 80,
        "destreza": 95,
        "velocidad": 65,
        "inteligencia": 75,
    },  # Maximum human potential and combat expert.
    "Thor": {
        "poder": 98,
        "destreza": 85,
        "velocidad": 85,
        "inteligencia": 70,
    },  # Divine power and great endurance.
    # --- The Boys Characters ---
    "Homelander": {
        "poder": 100,
        "destreza": 80,
        "velocidad": 95,
        "inteligencia": 40,
    },  # Very powerful but emotionally unstable and less tactical.
    "Butcher": {
        "poder": 75,
        "destreza": 70,
        "velocidad": 60,
        "inteligencia": 80,
    },  # Expert strategist with serum-enhanced strength.
    # --- Breaking Bad Characters ---
    "Walter White": {
        "poder": 30,
        "destreza": 40,
        "velocidad": 10,
        "inteligencia": 100,
    },  # Genius-level intellect, low physical capability.
    "Jesse Pinkman": {
        "poder": 20,
        "destreza": 60,
        "velocidad": 20,
        "inteligencia": 50,
    },  # Street smarts, no great physical power.
    "Gus Fring": {
        "poder": 40,
        "destreza": 70,
        "velocidad": 5,
        "inteligencia": 95,
    },  # Criminal mastermind and extremely methodical.
}


# Function to calculate the overall ranking based on specific weights for each stat.
def calcular_ranking(stats):
    # Weighted sum is calculated: power is worth more (40%) than the others (30% each).
    total = (
        (stats["poder"] * 0.4)
        + (stats["destreza"] * 0.3)
        + (stats["velocidad"] * 0.3)
        + (stats["inteligencia"] * 0.3)
    )
    # Normalized by dividing by 1.3 (the sum of weights) so the maximum is 100.
    normalized_total = total / 1.3
    # Returns the rounded value, ensuring the minimum is 1.
    return max(1, round(normalized_total))


# Function to display a list of characters sorted by a selected stat.
def mostrar_ranking_por_stat(stat_elegida):
    print(f"\n--- Ranking por {stat_elegida.capitalize()} ---")
    # The dictionary is sorted by converting it to a list of tuples and using the stat as the sort key.
    ranking_ordenado = sorted(
        personajes.items(), key=lambda item: item[1][stat_elegida], reverse=True
    )
    # The sorted list is iterated to print the results.
    for nombre, stats in ranking_ordenado:
        print(f"{nombre}: {stats[stat_elegida]}")


# Main function that handles the interactive menu for the user.
def main():
    while True:
        # Prints the available options in the menu.
        print("\n--- Menú de Ranking de Personajes ---")
        print("1. Ranking General")
        print("2. Ranking por Poder")
        print("3. Ranking por Destreza")
        print("4. Ranking por Velocidad")
        print("5. Ranking por Inteligencia")
        print("6. Salir")

        # Captures the user's choice.
        opcion = input("Elige una opción: ")

        # Logic to process the chosen option.
        if opcion == "1":
            print("\n--- Ranking General ---")
            # Calculates and displays the computed ranking for each character.
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
            # Farewell message and program exit.
            print("¡Hasta luego!")
            break
        else:
            # Handles invalid input.
            print("Opción no válida. Inténtalo de nuevo.")


# Script entry point: ensures main() only runs if the file is executed directly.
if __name__ == "__main__":
    main()
