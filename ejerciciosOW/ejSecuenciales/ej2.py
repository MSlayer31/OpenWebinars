#Calcular el perímetro y área de un rectángulo dada su base y su altura.
#variables tipo float, per si es vol anyadir decimals

base = float(input("Introduzca la base:\n"))
altura = float(input("Introduzca la altura:\n"))

perimetro = 2*(base + altura)
area = base + altura

print("El perimetro es",perimetro,", y el area es",area,".")