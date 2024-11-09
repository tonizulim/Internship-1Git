def unos(polje, igrac, popunjeno_polje):
    while True:
        pozicija=int(input(f"Igrac {'x' if igrac==1 else 'o'}: "))-1
        if pozicija+1 not in range(1,10) or polje[pozicija]!=0:
            print("nepravilan unos pokusaj ponovo")
        else:
            polje[pozicija]=igrac
            popunjeno_polje[pozicija] = 'x' if igrac == 1 else 'o'
            return polje

def zamjena(igrac):
    if igrac == 1:
        return 2
    else:
        return 1

def provjera(polje, igrac):
    if polje[0] == polje[1] == polje[2] == igrac:
        return igrac
    elif polje[3] == polje[4] == polje[5] == igrac:
        return igrac
    elif polje[6] == polje[7] == polje[8] == igrac:
        return igrac
    
    #okomito
    elif polje[0] == polje[3] == polje[6] == igrac:
        return igrac
    elif polje[1] == polje[4] == polje[7] == igrac:
        return igrac
    elif polje[2] == polje[5] == polje[8] == igrac:
        return igrac
    #diagonalno
    elif polje[0] == polje[4] == polje[8] == igrac:
        return igrac
    elif polje[6] == polje[4] == polje[2] == igrac:
        return igrac
    else:
        return 0

def ispis(polje):
    print(f"\033[4m{polje[0]}|{polje[1]}|{polje[2]}\033[0m")
    print(f"\033[4m{polje[3]}|{polje[4]}|{polje[5]}\033[0m")
    print(f"{polje[6]}|{polje[7]}|{polje[8]}")
    


polje=[0,0,0,0,0,0,0,0,0]
ispunjeno_polje=["1","2","3","4","5","6","7","8","9"]
igrac=1
pobjednik=0
brojac=0

while not pobjednik and brojac<9:
    brojac+=1
    ispis(ispunjeno_polje)
    polje=unos(polje, igrac, ispunjeno_polje)
    pobjednik=provjera(polje, igrac)
    igrac=zamjena(igrac)

if pobjednik:
    print(f"Pobjednik je {'x' if pobjednik==1 else 'o'}")
else:
    print("Nema pobjednika")