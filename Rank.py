personajes = {
    "Eliot Alderson": {"poder": 50, "destreza": 90, "velocidad": 60},
    "Superman": {"poder": 100, "destreza": 80, "velocidad": 95},
}


def calcular_ranking(stats):
    total = (
        (stats["poder"] * 0.4) + (stats["destreza"] * 0.3) + (stats["velocidad"] * 0.3)
    )
    return total


for nombre, stats in personajes.items():
    score = calcular_ranking(stats)
    print(f"{nombre} tiene un ranking de: {score}%")
