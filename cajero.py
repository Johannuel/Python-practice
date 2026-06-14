# Is a variable.
Saldo = 1000
# Is a Bucle whith options and conditions , start whith a menu, end whith a option to exit
while True:
    print("\n Welcome to Menu!: ")
    print("\n 1. Ver saldo")
    print("\n 2. Retirar dinero")
    print("\n 3. Depositar dinero")
    print("\n 4. Salir")

    Opcion = input("\n Seleccione una opcion : ")
    if Opcion == "1":
        print(f"\n Tu saldo es :{Saldo} \n")

    elif Opcion == "2":
        Monto = int(input("\n Cuanto dinero quiere retirar : "))

        if Monto > Saldo:
            print("\n Saldo Insuficiente :( \n")

        else:
            Saldo -= Monto
            print("\n Retiro Exitoso")
            print(f"\n Tu nuevo monto es : {Saldo} \n")

    elif Opcion == "3":
        Monto = int(input("\n Cuanto dinero quiere depositar : "))
        Saldo += Monto
        print("\n Deposito Exitoso")
        print(f"\n Tu nuevo monto es : {Saldo} \n")

    elif Opcion == "4":
        print("\n Hasta la proxima! :)")
        break

    else:
        print("\n Opcion no valida :/ ")
