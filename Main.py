mediciones = 0

while mediciones < 4:
    temperatura = int(input("Introduce la temperatura actual en °C: "))

    if temperatura > 35:
        print("ALERTA: Calentamiento crítico") 
        break

    elif temperatura < 10:
        print("ALERTA: Enfriamiento crítico. Encendiendo calefacción")
        mediciones += 1 
        print(f"Medición registrada con éxito. Llevas {mediciones} de 4.")

    else:
        mediciones += 1
        print("Temperatura normal")
        print(f"Medición  registrada con éxito. Llevas {mediciones} de 4.")

print("Monitoreo finalizado.")