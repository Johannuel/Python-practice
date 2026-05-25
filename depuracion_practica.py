# Archivo de práctica para depuración con Python

# Error 1: Falta el ':' después de la definición de la función.
def calcular_promedio_lista(numeros)
    suma_total = 0
    for numero in numeros:
        # Error 2: Intentar sumar un número y una cadena si la lista tiene tipos mixtos.
        suma_total += numero

    # Error 3: Si la lista está vacía, la división por cero causará un error.
    promedio = suma_total / len(numeros)
    return promedio

# Error 4: Falta el ':' después de la definición de la función.
def saludar_usuario(nombre, edad)
    # Error 5: Intento de concatenar un número (edad) con una cadena sin conversión explícita.
    mensaje = "Hola, " + nombre + "! Tienes " + edad + " años."
    print(mensaje)

# Error 6: Usar una variable antes de asignarle un valor (NameError).
# Descomentar para probar:
# print(variable_no_definida_aun)

# Error 7: Llamada a función con tipos incorrectos.
lista_ejemplo = [10, 20, 30, 'cuarenta', 50] # 'cuarenta' es una cadena, causará TypeError en suma_total += numero
edad_usuario = 25 # Esto es un entero

# Descomentar para probar:
# print(f"El promedio es: {calcular_promedio_lista(lista_ejemplo)}")
# print(saludar_usuario("Alice", edad_usuario))

# Error 8: Lógica incorrecta - Bucle infinito (falta incrementar el contador).
def bucle_infinito_ejemplo():
    contador = 0
    while contador < 5:
        print(f"Contando: {contador}")
        # contador += 1 # Línea comentada intencionadamente para crear un bucle infinito.

# Descomentar para probar:
# print("Iniciando bucle...")
# bucle_infinito_ejemplo()
# print("Bucle terminado (si no era infinito).")
