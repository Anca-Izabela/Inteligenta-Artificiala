def determina_castigator(alegere1, alegere2):
    if alegere1 == alegere2:
        return "Egalitate!"
    
    if (alegere1 == "piatra" and alegere2 == "foarfeca") or \
       (alegere1 == "foarfeca" and alegere2 == "hartie") or \
       (alegere1 == "hartie" and alegere2 == "piatra"):
        return "Felicitări Jucătorul 1! Ai câștigat!"
    else:
        return "Felicitări Jucătorul 2! Ai câștigat!"

def joaca_rps():
    vrea_sa_joace = True
    
    while vrea_sa_joace:
        jucator1 = input("Jucător 1 (piatra/hartie/foarfeca): ").lower().strip()
        jucator2 = input("Jucător 2 (piatra/hartie/foarfeca): ").lower().strip()
        
        optiuni = ["piatra", "hartie", "foarfeca"]
        if jucator1 not in optiuni or jucator2 not in optiuni:
            print("Alegere invalidă!")
            continue
            
        print(determina_castigator(jucator1, jucator2))
        
        raspuns = input("Doriți să începeți un nou joc? (da/nu): ").lower().strip()
        if raspuns != "da":
            vrea_sa_joace = False

if __name__ == "__main__":
    joaca_rps()