#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = int(input("Introduzca un numero:\n"))
num2 = int(input("Introduzca otro numero:\n"))

sum = num1 + num2
res = num1 - num2
mul = num1 * num2
div = num1 / num2
print("Valor suma:",sum,
      ".\nValor resta:",res,
      ".\nValor multiplicar:",mul,
      ".\nValor dividir:",div)

#Version mejorada
#print("La suma es", num1+num2)
#print("La resta es", num1-num2)
#print("La multiplicación es", num1*num2)
#print("La división es", num1/num2)