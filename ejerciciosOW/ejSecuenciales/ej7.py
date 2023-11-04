#Realiza un programa que reciba una cantidad de minutos
# y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minTotal = int(input("Introduzca una cantidad de minutos: "))

horas = minTotal//60
minutos = minTotal%60

print(horas,"horas y",minutos,"minutos")