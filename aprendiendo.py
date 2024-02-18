
while True:
    monto = float(input("Ingrese el monto de su sueldo: "))
    if monto > 500:
        print("Usted puede seguir con el programa")
        False
    else: 
        print("Su monto no es el adecuado, intentelo nuevamente")

comprobar = monto 

monto = float(input("Ingrese el nuevo monto: "))

while comprobar == monto:
    monto = float(input("El monto ingresado es el mismo, ingrese uno diferente: "))

