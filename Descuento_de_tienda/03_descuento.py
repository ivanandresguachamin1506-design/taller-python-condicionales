while True:
    i = input("¿Cuánto te costó?: ")
    if i.isdigit():
        i = float(i)
        if i < 0:
            print("El precio no puede ser negativo.")
        else:
            pos = input("¿Sos vip o regular?: ")
            if pos == "vip":
                print("Te costó:", i)
                print("Descuento 15%")
                print("Total:", i - i * 0.15)
                break
            elif pos == "regular":
                print("Te costó:", i)
                if i >= 100:
                    print("Descuento 5%")
                    print("Total:", i - i * 0.05)
                else:
                    print("Sin descuento")
                    print("Total:", i)
                break
            else:
                print("Debes escribir vip o regular.")
    else:
        print("Precio inválido. Intenta otra vez.")