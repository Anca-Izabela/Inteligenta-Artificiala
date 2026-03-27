primele_10_pare = {x for x in range(20) if x % 2 == 0}

text_exemplu = "laborator de inteligenta artificiala"
litere_distincte = {caracter for caracter in text_exemplu if caracter.isalpha()}

fraza = "Python este un limbaj de programare foarte puternic si versatil"
cuvinte_lungi = {cuvant for cuvant in fraza.split() if len(cuvant) >= 5}

print(f"Primele 10 pare: {primele_10_pare}")
print(f"Litere distincte: {litere_distincte}")
print(f"Cuvinte >= 5 litere: {cuvinte_lungi}")