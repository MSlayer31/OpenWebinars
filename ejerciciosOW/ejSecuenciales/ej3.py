#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

import math

cat1 = float(input("Cuanto mide el primer cateto?\n"))
cat2 = float(input("Cuanto mide el segundo cateto?\n"))

#Version mejorada(en la linia 9 se compacta de la 11 a la 16)
#hipotenusa = math.sqrt(pow(cat1, 2)+pow(cat2,2))

cat1 = pow(cat1,2)
cat2 = pow(cat2,2)
hipotenusa = cat1 + cat2

#Raiz cuadrada de la hipotenusa
hipotenusa = math.sqrt(hipotenusa)

print("La hipotenusa es",hipotenusa)