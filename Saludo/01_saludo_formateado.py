while True:
    name = input("Dime tu nombre: ")
    if name != "":
        break
    print("El nombre no puede estar vacío.")
while True:
    age = input("Cuántos años tienes: ")
    if age.isdigit():
        age = int(age)
        if age > 0:
            break
    print("Edad inválida. Ingresa un número mayor que 0.")
while True:
    city = input("Dónde vives: ")
    if city != "":
        break
    print("La ciudad no puede estar vacía.")
print(f"Hola {name}, tienes {age} años y resides en {city}.")