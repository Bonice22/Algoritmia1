#IMC
nombre=input("Hola, cual es tu nombre?")
print(("hola" + nombre + "vamos a sacar tu IMC(indice de masa corporal)"))

peso= float(input("para comenzar,¿cual es tu peso?(kg) "))
altura= float(input("cual es tu altura?(m)"))
alturaf=altura * altura
imc= peso/alturaf
print("tu IMC es de " , imc )
if imc <= 18.5:
    print("tu IMC es muy bajo ")
elif imc >=18.5 <= 24.9:
    print("tu IMC es normal")
elif imc >= 24.9 <= 30:
    print("tu IMC indica que tienes sobrepeso")
elif imc >= 30 <= 35:
    print("Tu IMC indica que tienes sobrepeso Grado 1")
elif imc >= 35 <=40:
    print("Tu IMC indica que tienes Obesidad grado 2")
elif imc >= 40:
    print("Tu IMC indica que tienes Obesidad grado 3(obesidad Mórbida)")
print('muchas gracias')