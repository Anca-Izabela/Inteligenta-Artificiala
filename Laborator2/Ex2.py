nota= int(input("Introduceti nota examen:"))
note_valide = list(range (1, 11))
while nota not in note_valide:
        nota = int (input("Reintroduceti nota examen:"))
if nota <=5:
        print("Reexaminare")
elif nota <=6:
        print("Suficient")
elif nota <=8:
         print("Bine")
elif nota <=10:
        print("Excelent")