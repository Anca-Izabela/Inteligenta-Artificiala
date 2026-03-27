def normalize_data(lista_numere):
    if not lista_numere:
        return []
    
    minim = min(lista_numere)
    maxim = max(lista_numere)
    
    if maxim == minim:
        return [0.0] * len(lista_numere)
    
    rezultat = []
    for x in lista_numere:
        valoare_normalizata = (x - minim) / (maxim - minim)
        rezultat.append(valoare_normalizata)
        
    return rezultat

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    normalized_data = normalize_data(data)
    print(f"Date originale: {data}")
    print(f"Date normalizate: {normalized_data}")