pare_0_100 = [x for x in range(101) if x % 2 == 0]

cuburi = [x**3 for x in range(10)]

lista1 = [1, 2, 3, 4, 5, 10]
lista2 = [3, 4, 5, 6, 7, 10]
elemente_comune = [x for x in lista1 if x in lista2]

print(f"Pare 0-100: {pare_0_100}")
print(f"Cuburi: {cuburi}")
print(f"Elemente comune: {elemente_comune}")