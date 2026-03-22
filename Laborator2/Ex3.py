import random

numar_secret = random.randint(1, 50)
incercari = 0
ghicit = False

print("Am ales un număr între 1 și 50. Încearcă să-l ghicești!")

while not ghicit:
    try:
        
        propunere = int(input("Ghicește numărul (1-50): "))
        incercari += 1
        
        if propunere < numar_secret:
            print("Numărul este mai mare!")
        elif propunere > numar_secret:
            print("Numărul este mai mic!")
        else:
            print(f"Felicitări! Ai ghicit numărul în {incercari} încercări.")
            ghicit = True 
            
    except ValueError:
        print("Te rog să introduci un număr întreg valid.")