def sistem_detectie_frauda():
    tari_risc = ["Coreea de Nord", "Siria", "Iran"]
    tranzactii_suspecte_totale = 0
    cont_blocat = False
    
    print("--- 🛡️ Sistem de Monitorizare Bancară ---")
    
    while not cont_blocat:
        print(f"\n[Status: {tranzactii_suspecte_totale}/3 alerte detectate]")
        
        try:
            
            suma = float(input("Introduceți suma tranzacției (RON): "))
            tara = input("Introduceți țara de origine: ").strip().title()
            
            
            este_suspecta = False
            mesaj_risc = ""

            
            if tara in tari_risc:
                mesaj_risc = f"❌ Frauduloasă (țară cu risc ridicat: {tara})"
                este_suspecta = True
            
            
            elif suma > 10000:
                mesaj_risc = "⚠️ Suspicioasă (sumă mare > 10.000 RON)"
                este_suspecta = True
            
            
            else:
                print(f"✅ Tranzacție: {suma} RON din {tara} → Sigură")

            
            if este_suspecta:
                print(f"Tranzacție: {suma} RON din {tara} → {mesaj_risc}")
                tranzactii_suspecte_totale += 1

            
            if tranzactii_suspecte_totale >= 3:
                print("\n" + "!"*40)
                print("🚨 ALERTĂ DE SECURITATE: 3 tranzacții suspecte detectate!")
                print("🔒 CONT BLOCAT. Vă rugăm să contactați banca.")
                print("!"*40)
                cont_blocat = True

        except ValueError:
            print("Eroare: Te rugăm să introduci o sumă numerică validă.")


sistem_detectie_frauda()