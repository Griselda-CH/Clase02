#Escribe un programa que solicite al usuario un número entero y calcule
#si es divisible por 3 y por 5.
#AND :Y
#OR : O
# == : Igualdad
#= : Asignacion
num= int(input("Ingresa un nùmero entero: "))
#Aqui verificamos que el numero si es  divicible 
num%3==0 and num%5==0
print(f"{num} es divicible por 3 y por 5")
print(f"{num} no es divicible por 3 y por 5")
