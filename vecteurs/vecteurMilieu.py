
def milieu_coord():
    x_a = int(input("Coordonnées x de A: "))
    y_a = int(input("Coordonnées y de A: "))
    x_b = int(input("Coordonnées x de B: "))
    y_b = int(input("Coordonnées y de B: "))
    coord_x = (x_a - x_b) / 2
    coord_y = (y_a - y_b) / 2
    print("")
    print("Le milieu du vecteur AB est ", coord_x, "x ; ", coord_y, "y")


milieu_coord()
