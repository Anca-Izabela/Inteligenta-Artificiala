def genereaza_factura(nume_client, **produse):
    print(f"Factură pentru clientul: {nume_client}")
    print("-" * 30)
    total = 0
    
    for produs, pret in produse.items():
        print(f"Produs: {produs} | Preț: {pret} RON")
        total += pret
        
    print("-" * 30)
    print(f"Total de plată: {total} RON")

if __name__ == "__main__":
    genereaza_factura("Mihai Popescu", Laptop=3500, Mouse=150, Tastatura=250)