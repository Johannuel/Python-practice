# Objetivo: Permitir hasta 3 intentos para poner la clave correcta (1234)
clave_correcta = "1234"
intentos_realizados = 0

while intentos_realizados < 3:
    clave_usuario = input("Introduce tu clave de 4 dígitos: ")
    
    if clave_usuario == clave_correcta:
        print("Acceso concedido. Bienvenido.")
        break
        # ERROR 1: Si adivina a la primera, el bucle sigue pidiendo la clave
    else:
        print("Clave incorrecta.")
        intentos_realizados += 1
        quedan = 3 - intentos_realizados
        print(f"Te quedan {quedan} intentos.")  #ERROR 2: Falta controlar que el contador de intentos suba

if intentos_realizados == 3:
        print("Tarjeta bloqueada por seguridad.")