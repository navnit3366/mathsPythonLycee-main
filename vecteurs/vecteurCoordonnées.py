
def vecteur_coord ():
    x_a = int(input("Coordonnées x de A: "))
    y_a = int(input("Coordonnées y de A: "))
    x_b = int(input("Coordonnées x de B: "))
    y_b = int(input("Coordonnées y de B: "))

    coord_X = x_b - x_a
    coord_Y = y_b - y_a

    print("")
    print("coordonnées du vecteur AB: ")
    print(str(coord_X) + "x")
    print(str(coord_Y) + "y")


vecteur_coord()
