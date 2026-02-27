while True:
    distancia = float(input("Ingrese la distancia recorrida en km: "))
    hora = int(input("Ingrese la hora del viaje (0-23): "))
    if hora >= 0 and hora <= 23:
        tarifa_base = 1
        if hora >= 6 and hora <= 19:
            costo_km = 0.50
            tipo = "diurno"
        else:
            costo_km = 0.65
            tipo = "nocturno"
        total = tarifa_base + (distancia * costo_km)
        if distancia > 10:
            total = total + 2
        print("Horario:", tipo)
        print("Distancia:", distancia, "km")
        print("Total a pagar: $", total)
        break
    else:
        print("Hora inválida. Intente nuevamente.")
        print("Distancia inválida. Debe ser un número.")