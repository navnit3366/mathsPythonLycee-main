
print("Puissances de 2.")

start_number = int(input("Entrez une puissance de départ: "))
repeat = int(input("Jusqu'à quelle puissance voulez vous allez: "))
times_exec = start_number

while times_exec <= repeat:
    start_number = pow(2, times_exec)
    print("2^", times_exec, ": ", start_number)
    times_exec += 1
