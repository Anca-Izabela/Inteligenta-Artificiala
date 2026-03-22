def analizeaza_sentimentul():
    print("--- Analizor de Sentiment (v1.0) ---")
    comentariu = input("Introdu comentariul tău: ").lower()

   
    cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
    cuvinte_negative = ["urât", "prost", "groaznic", "dezamăgitor", "rau"]

    
    scor_pozitiv = any(cuvant in comentariu for cuvant in cuvinte_pozitive)
    scor_negativ = any(cuvant in comentariu for cuvant in cuvinte_negative)

    
    if scor_pozitiv and not scor_negativ:
        print("Sfat: ✨ Comentariu pozitiv!")
    elif scor_negativ and not scor_pozitiv:
        print("Sfat: ⚠️ Comentariu negativ!")
    elif scor_pozitiv and scor_negativ:
        print("Sfat: 🧐 Comentariu mixt (conține și bune, și rele).")
    else:
        print("Sfat: 😐 Comentariu neutru.")


analizeaza_sentimentul()