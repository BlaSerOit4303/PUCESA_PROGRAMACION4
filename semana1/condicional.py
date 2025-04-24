
print("1. Sumar dos numeros")
print("2. Restar dos numeros")
print("3. Multiplicar dos numeros")
print("4. Dividir dos numeros")
print("5. Salir")
print("Elige una opcion del menu")
opcion = int(input("Opcion: "))
"Validar la opcion elegida"
if opcion < 1 or opcion >5:
    print("Opcion no valida")
    
if opcion == 1:
    print("Usted eligió la suma")
    num1= float(input("Ingrese el primer numero: "))
    num2= float(input("ingrese el segundo numero: "))
    suma= num1 + num2
    print("La suma es: ", suma)
if opcion == 2:
    print("Usted eligió la resta")
    num1= float(input("Ingrese el primer numero: "))
    num2= float(input("ingrese el segundo numero: "))
    resta= num1 - num2
    print("La resta es: ", resta)
if opcion == 3:
    print("Usted eligió la multiplicación")
    num1= float(input("Ingrese el primer numero: "))
    num2= float(input("ingrese el segundo numero: "))
    multi= num1 * num2
    print("La multiplicación es: ", multi)
if opcion == 4:
    print("Usted eligió la división")
    num1= float(input("Ingrese el primer numero: "))
    num2= float(input("ingrese el segundo numero: "))
    if num2== 0:
        print("No se puede dividir para 0")
    else:
        div= num1 / num2
        print("La division es: ", div)
if opcion == 5:
    print("Usted eligió salir del programa")