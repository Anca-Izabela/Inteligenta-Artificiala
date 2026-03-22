import random

print("--- Bine ai venit la Loteria Python! ---")
print("Alege 6 numere între 1 și 49.\n")

numere_utilizator = []
while len(numere_utilizator) < 6:
    try:
        nr = int(input(f"Numărul {len(numere_utilizator) + 1}: "))
        
        if nr < 1 or nr > 49:
            print("Eroare: Te rog alege un număr între 1 și 49.")
        elif nr in numere_utilizator:
            print("Eroare: Ai ales deja acest număr. Introdu unul diferit.")
        else:
            numere_utilizator.append(nr)
    except ValueError:
        print("Eroare: Te rog introdu un număr întreg valid.")

numere_extrase = random.sample(range(1, 50), 6)

ghicite = list(set(numere_utilizator) & set(numere_extrase))
nr_ghicite = len(ghicite)


print("\n" + "="*30)
print(f"Numerele tale:    {sorted(numere_utilizator)}")
print(f"Numere extrase:   {sorted(numere_extrase)}")
print(f"Ai ghicit {nr_ghicite} numere: {ghicite}")

if nr_ghicite == 6:
    print("WOW! Marele Premiu! Ești milionar!")
elif nr_ghicite >= 4:
    print("Felicitări! Ai câștigat un premiu substanțial!")
elif nr_ghicite == 3:
    print("Felicitări! Ai câștigat un premiu mic!")
else:
    print("Din păcate, biletul nu este câștigător. Mai încearcă!")