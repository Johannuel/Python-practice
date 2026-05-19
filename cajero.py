Saldo = 1000

while True:
    print("Menu cajero")
    print("\n 1. Ver saldo")
    print("\n 2. Retirar dinero")
    print("\n 3. Salir")

    Opcion = input("\n Seleccione una opcion : ")
    if Opcion == "1":
        print(f"\n Tu saldo es :{Saldo} \n")

    elif Opcion == "2":
        Monto = int(input("\n Cuanto dinero quiere retirar : "))
        if Monto > Saldo:
            print("\n Saldo Insuficiente \n")

        else:
            Saldo -= Monto
            print("\n Retiro Exitoso")
            print(f"\n Tu nuevo monto es : {Saldo} \n")

    elif Opcion == "3":
        print("\n Hasta la proxima!")
        break
