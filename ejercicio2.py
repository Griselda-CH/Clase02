#Escribe un programa que solicite al usuario un número entero y calcule
#su cuadrado y su cubo.

#Utilizaremos la clase MATH  la debemos importar de la siguente manera
import math
#Math ya tiene funcionalidades estabecidas, como tambien parametros

#Solicitamos que ingrese un numero entero con int antes de input
num= int(input("Ingrese un numero entero: "))
cuadrado= math.pow(num,2)
cubo= math.pow(num,3)
cuarta= math.pow(num,4)
#Otra forma de elevar al cuadrado sin ocupar la clase MATH
potencia= num**3
#Sqrt:Retorna la raiz cuadrad
raiz= math.sqrt(16)
raizCuadrada= math.pow(num,1/2)

#Porcentajes
# 20% = 0.2
porcentaje20= num*0.2
precioconDescuento= num-porcentaje20



print("El cuadrado es:",cuadrado)
print("El cubo es: ",cubo)
print("El cubo es: ",cuarta)
print("El cuadrado es: ",potencia)
print("La raiz cadrada es: ",raiz)
print("La raiz 2 cuadrada es: ",raizCuadrada)
print("El 20 porciento es: ",porcentaje20)
print("El precio con descuento es: ",porcentaje20)