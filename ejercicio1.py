#Escribe un programa que solicite al usuario dos números y muestre su
#suma, resta, multiplicación, división, división entera y residuo (módulo).
#Ingreso de datos por el usuario
num1 = input("Porfavor Ingresa un Numero: ")
num2 = input("Porfavor Ingresa un Numero: ")
#Suma
suma= num1+num2
#Resta
resta= num1-num2
#Multiplicacion
mult= num1*num2
#Tres cormas de imprimir el resultado 
#De esta forma tambien podemos imprimir el mensaje, debemos trasformar la variable a string con 
#agregando + str(nombre de la variable)
print("La Multiplicacion es: "+ str(mult))
print(f"Multiplicacion: {mult}")
print("La Multiplicacion es : ", mult)
#divicion 
#No se va a poder dividir entre 0
div= num1/num2 if num2!=0 else ("No se podra dividir por 0 ")
#Modulo o residuo
modulo = num1%num2 if num2!=0 else ("No se podra calcular el modulo CON 0 ")
 
#Manera concatenando los print
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {mult}")
print(f"Divicion: {div}")
print(f"Residuo: {modulo}")
#print(f"Suma: {suma}")



