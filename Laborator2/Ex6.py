import time

def incepe_aventura():
    inventar = []
    print("--- 🌲 Bun venit în Pădurea Magică! 🌲 ---")
    print("Te trezești la o răscruce. Aerul miroase a praf de stele și mușchi umed.")
    
   
    directie = input("\nÎncotro mergi? (stânga / dreapta): ").lower().strip()
    
    if directie == "stânga":
        print("\nMergi spre vest, unde copacii devin tot mai deși...")
        time.sleep(1)
        print("Întâlnești un Spiriduș bătrân care îți cere ajutorul.")
        
        ajutor = input("Îl ajuți să-și găsească ochelarii? (da / nu): ").lower().strip()
        if ajutor == "da":
            print("Spiridușul este fericit! Îți dă o **Amuletă de Smarald**.")
            inventar.append("Amuletă de Smarald")
        else:
            print("Spiridușul dispare într-un nor de fum, lăsându-te singur.")
            
    elif directie == "dreapta":
        print("\nMergi spre est, unde soarele pătrunde printre frunze...")
        time.sleep(1)
        print("Găsești un cufăr vechi, acoperit de iederă.")
        
        deschide = input("Încerci să deschizi cufărul? (da / nu): ").lower().strip()
        if deschide == "da":
            print("Interiorul strălucește! Ai găsit o **Sabie de Argint**.")
            inventar.append("Sabie de Argint")
        else:
            print("Ești precaut și mergi mai departe, dar ratezi o oportunitate.")
    else:
        print("\nTe-ai rătăcit prin mărăcini pentru că n-ai ales o direcție clară.")

    
    print("\n" + "-"*30)
    print("Deodată, un Lup Argintiu îți taie calea!")
    time.sleep(1)

    if "Sabie de Argint" in inventar:
        print("Lupul vede Sabia de Argint, se înclină și te lasă să treci. Ești stăpânul pădurii!")
    elif "Amuletă de Smarald" in inventar:
        print("Amuleta strălucește puternic, hipnotizând lupul. Reușești să fugi teafăr!")
    else:
        print("Nu ai nimic să te apere... Lupul te fugărește până la marginea pădurii. Ai pierdut!")

    
    print("\n" + "="*30)
    if inventar:
        print(f"Obiecte adunate în aventură: {', '.join(inventar)}")
    else:
        print("Inventarul tău este gol.")
    print("SFÂRȘITUL AVENTURII")


incepe_aventura()