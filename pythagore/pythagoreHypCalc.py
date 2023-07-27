import math

print("Calcul de l'hypoténuse.")
print("Le calcul est valable dans le cas où le triangle est rectangle. Ne marche qu'avec des nombres entiers.")

a = input("longueur du côté A: ")
b = input("Longueur du côté B: ")
a_square = pow(int(a), 2)  # mise au carré de a
b_square = pow(int(b), 2)  # mise au carré de b
hyp = int(math.sqrt(a_square + b_square))  # carré de l'hypoténuse = a^carré plus b^carré

print("La longueur de l'hypoténuse est de " + str(hyp) + " unités.")

# Clémentin Bonneau-Riera
