prețuri = [100, None, 250, 400, None, 50]

preturi_valide = filter(lambda x: x is not None, prețuri)

preturi_reduse = list(map(lambda x: x * 0.9, preturi_valide))

print(f"Lista originală: {prețuri}")
print(f"Lista procesată (fără None și reducere 10%): {preturi_reduse}")