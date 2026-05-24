from posix import stat

personajes = {
    "Superman": {"poder": 100, "destreza": 80, "velocidad": 95, "inteligencia": 70},
    "Batman": {"poder": 70, "destreza": 60, "velocidad": 80, "inteligencia": 90},
    "Homelander": {"poder": 100, "destreza": 80, "velocidad": 95, "inteligencia": 40},
    "Butcher": {"poder": 90, "destreza": 70, "velocidad": 85, "inteligencia": 80},
    "Flash": {"poder": 80, "destreza": 70, "velocidad": 80, "inteligencia": 180},
    "Wally west": {"poder": 85, "destreza": 75, "velocidad": 85, "inteligencia": 200},
    "Wonder Woman": {"poder": 90, "destreza": 80, "velocidad": 90, "inteligencia": 100},
    "Hulk": {"poder": 100, "destreza": 90, "velocidad": 100, "inteligencia": 80},
}


def calcular_ranking(stats):
    total = (
        (stats["poder"] * 0.4)
        + (stats["destreza"] * 0.3)
        + (stats["velocidad"] * 0.3)
        + (stats["inteligencia"] * 0.3)
    )
    return total


for nombre, stats in personajes.items():
    score = calcular_ranking(stats)
    print(f"{nombre} tiene un ranking de: {score}%")
