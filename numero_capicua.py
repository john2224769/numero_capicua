# Quiz N. 2 Leer un numero entero de 5 digitos y determinar si es capicua

#input
print(" ")
n=int(input("Ingrese el numero entero de 5 digitos:  "))
print(" ")

#processing
if 10000<= n <=99999:
    if n%10 == n//10000:
        if ((n%100)-n%10)/10 == (n//1000)%10:
            print("El numero es capicúa")
            print(" ")
        else:
            print("El numero no es capicúa")
            print(" ")
    else: 
        print("El numero no es capicúa")
        print(" ")
else:
    print("El numero ingresado no es de 5 digitos ")
    print(" ")