print("Vérifier la réciproque de Pythagore.")
print("Ne marche qu'avec des nombres entiers.")

a = input("longueur du côté A: ")
b = input("Longueur du côté B: ")
hyp = input("Longueur du côté C (hypoténuse): ")
a_b_lenght_square = pow(int(a), 2) + pow(int(b), 2)  # additionne les carrés des côtés A et B

if a_b_lenght_square == pow(int(hyp), 2):  # si la sommes edes carrés est strictement égale au carré de l'hypothénuse
    print("La réciproque de Pythagore est vérifiée. Le triangle est rectangle.")
else:  # sinon, donc si elle n'est pas égale
    print("La réciproque de Pythagore n'est pas vérifiée. Le triangle n'est pas rectangle.")

# Clémentin Bonneau-Riera
