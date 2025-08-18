def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = vuelto - pesos
    print("ingrese el gasto: ")
    print(expense)
    print("ingrese el dinero recibido: ")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos: ")
    print(pesos)
    print("centavos: ")
    print(centavos)
