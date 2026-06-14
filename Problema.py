# Goal: Allow up to 3 attempts to enter the correct password (1234)
clave_correcta = "1234"
intentos_realizados = 0

while intentos_realizados < 3:
    clave_usuario = input("Introduce tu clave de 4 dígitos: ")
    
    if clave_usuario == clave_correcta:
        print("Acceso concedido. Bienvenido.")
        break
        # ERROR 1: If guessed on the first try, the loop keeps asking for the password
    else:
        print("Clave incorrecta.")
        intentos_realizados += 1
        quedan = 3 - intentos_realizados
        print(f"Te quedan {quedan} intentos.")  #ERROR 2: Missing control to increment the attempt counter

if intentos_realizados == 3:
        print("Tarjeta bloqueada por seguridad.")