#Escribe un programa que lea un número entero y determine si es
#positivo, negativo o cero.
                 #TEMA CONDICIONALES

num= int(input("Ingresa un número entero:"))
#Si la condicion  se cumple 
if num>0:
    print(f"{num} es positivo")
#Si no es 
elif num<0:
    print(f"{num} es negativo")
#No
else:
    print("El nùmero es 0")
    
    