patrate = {x: x**2 for x in range(1, 11)}

text = "laborator"
frecventa_litere = {char: text.count(char) for char in text if char.isalpha()}

divizori_dict = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}

print(patrate)
print(frecventa_litere)
print(divizori_dict)