#importy
import random
import time
#---
def Hotovo(soubor,radky,sloupce):
    radky,sloupce = int(radky),int(sloupce)
    #Vytvoříme pure-databázi:
    print("Načítám")
    print(len(soubor))
    databaze = []
    #simulace funkce "eval"
    with open(soubor, "r") as f:
            celkem = 2* (radky*sloupce)*(radky*sloupce-1)*(radky*sloupce-1)
            print("Přibližně celkem:",celkem)
            pocitadlo = 0
            for line in f:
                line = line.replace("\n","")
                pocitadlo += 1
                if pocitadlo%(2**15) == 0:
                    print(pocitadlo)
                podseznam = eval(line)
                #Kdyby "eval" nefungovalo:
                """podseznam = []
                ukazatel = 0
                ukazuje = False
                while ukazatel < len(line) and line[ukazatel] != "]":
                    while ukazatel < len(line) and line[ukazatel] not in "'0123456789": #posouvám ukazatel
                        ukazatel += 1
                    #první ukazatel
                    prvek = ""
                    if line[ukazatel] == "'":
                        ukazatel += 1
                        while ukazatel < len(line) and line[ukazatel] != "'":
                            prvek += line[ukazatel]
                            ukazatel += 1
                    else:
                        while line[ukazatel] != ",":
                            prvek += line[ukazatel]
                            ukazatel += 1
                        prvek = int(prvek)
                    ukazatel += 1
                    podseznam.append(prvek)
                    #první prvek
                    prvek = ""
                try:
                    int(podseznam[4])
                except ValueError:
                    pass"""
                databaze.append(podseznam)
    print("Načteno")
    puredatabaze = []
    print(len(databaze))
    for k in range(len(databaze)):
        kara = databaze[k][:-3]
        karap = kara[:] #deepcopy
        puredatabaze.append(karap)
        #print(puredatabaze[-1:])
    #print(puredatabaze)
    return databaze,puredatabaze



def Nova_Partie(databaze,puredatabaze,radky,sloupce):
    #NORMÁLNÍ ŠACHOVÁ TERMINOLOGIE - NYNÍ
    def sloupec(x): #napíšu číslo, vrátí písmeno
        return chr(ord("a")-1+x)
    def desloupec(x): #písmeno sloupce na číslo
        return ord(x)+1-ord("a")
    def SouradnicePole(x):#string na dvojici
        j = [0,0]
        j[0] = desloupec(x[0])
        j[1] = int(x[1:])
        return j
    def NazevPole(x):#dvojici na string
        return str(sloupec(x[0]))+str(x[1])

    def TahKralem(konpozice,kde): #konpozice - pozice: kde - integer (umisteni krale)
            kde= konpozice[kde]
            rada = int(kde[1:])
            sloupek = desloupec(kde[0])
            tahy = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if i !=0 or j!=0:
                        if sloupek +i <= sloupce and sloupek + i > 0 and rada + j <= radky and rada + j > 0:
                                cil = NazevPole([sloupek + i, rada + j])
                                if cil not in konpozice or (konpozice.index(cil)%2 != (konpozice.index(kde))%2): #jiný index = nežeru vlasní figuru
                                    tahy.append(cil)
            return tahy
    def MuzeVez(konpozice,kde=2):
            kde= konpozice[kde]
            #print(konpozice)
            if kde != "X":
                tahy = []
                rada = int(kde[1:])
                sloupek = desloupec(kde[0])
                #DOLEVA
                for i in range(1,sloupek): 
                    r = NazevPole([sloupek-i,rada])
                    if r not in konpozice:
                        tahy.append(r)
                    else:
                        if konpozice.index(r) == 1:
                            tahy.append(r)
                        break
                #DOPRAVA
                for i in range(1,sloupce-sloupek+1):
                    r = NazevPole([sloupek+i,rada])
                    if r not in konpozice:
                        tahy.append(r)
                    else:
                        if konpozice.index(r) == 1:
                            tahy.append(r)
                        break
                #NAHORU
                for i in range(1,radky-rada+1):
                    r = NazevPole([sloupek,rada+i])
                    if r not in konpozice:
                        tahy.append(r)
                    else:
                        if konpozice.index(r) == 1:
                            tahy.append(r)
                        break
                #DOLŮ
                for i in range(1,rada): 
                    r = NazevPole([sloupek,rada-i])
                    if r not in konpozice:
                        tahy.append(r)
                    else:
                        if konpozice.index(r) == 1:
                            tahy.append(r)
                        break
                return tahy
            else:
                return []
    def Odmazkonec(seznam):
        while seznam[-1] in [None,"",0,"0"]:
            seznam.pop()
        return seznam
    def TahyObec(databaze,cislo,figura): #tahy nikoli neomezené, ale neřeším legalitu
            if figura == 0 or figura == 1:
                return TahKralem(databaze[cislo],figura) #vrací list
            elif figura == 2:
                return MuzeVez(databaze[cislo],figura) #vrací list
            return

    def JeLegalni(konpozice):
            if konpozice[1] == "X" or konpozice[0] == "X":
                return False
            bilkra = SouradnicePole(konpozice[0])
            cerkra = SouradnicePole(konpozice[1])
            if bilkra[0]-cerkra[0] in range(-1,2) and bilkra[1]-cerkra[1] in range(-1,2):
                return False
            return True
    def Presunpozice(databaze,cislo,figura,pole): #Narozdíl od Finalpozice toto pouze řeší vzniknutí nové pozice přesunutím dané figury
        j = (databaze[cislo])[:]
        if pole not in j: #jestli pole není obsazeno
            j[figura] = pole
        else: #braní
            k = j.index(pole)
            j[k] = "X" #odstraníme figuru ze šachovnice
            j[figura] = pole
        return j
    def easy_JeSach(databaze,cislopozice):
            j = databaze[cislopozice]
            sach = ""
            if j[2] == "X" or j[0] == "X":
                return "N"
            else:
                umisteniv = j[2]
                radav = int(umisteniv[1])
                sloupecv = desloupec(umisteniv[0])
                umistenik = j[1]
                radak = int(umistenik[1])
                sloupeck = desloupec(umistenik[0])
                #jsou na stejné řadě/sloupci?
                if radav == radak or sloupecv == sloupeck: #může být šach
                    umistenib = j[0] #neblokuje bílýkrál?
                    sloupecb = desloupec(umistenib[0])
                    radab = int(umistenib[1])
                    if radav == radak:
                        if radab == radav:
                            if sloupecv>sloupeck: #napravo věž
                                if sloupecb in range(sloupeck+1,sloupecv): #král mezinima
                                    return "N"
                                else:
                                    return "C"
                            else: #nalevo věž
                                if sloupecb in range(sloupecv+1,sloupeck): #král mezinima
                                    return "N"
                                else:
                                    return "C"
                        else:
                            return "C" #král je na jiné řadě
                    else:
                        if sloupecb == sloupecv:
                            if radav>radak: #nad věž
                                if radab in range(radak+1,radav): #král mezinima
                                    return "N"
                                else:
                                    return "C"
                            else: #pod věž
                                if radab in range(radav+1,radak): #král mezinima
                                    return "N"
                                else:
                                    return "C"
                        else:
                            return "C" #král je na jiném sloupci

            return
    """def Explain_All_Moves_old(databaze,puredatabaze,cislo):
        vsechny_tahy = []
        if databaze[cislo][3] == "B":
            tahy = TahyObec(databaze,cislo,0) #seznam cílových polí
            for j in tahy:
                novapoz = Presunpozice(databaze,cislo,0,j)[:-3] #král
                if JeLegalni(novapoz): #jestli nejedu do nemožné pozice
                    novapoz = databaze[puredatabaze.index(novapoz)+len(databaze)//2] #přehodím stranu, co je na tahu
                    if novapoz[4] != "Nex":
                       vsechny_tahy.append(["K",j,novapoz[4]]) #figura - cíl. pole - hodnocení
            tahy = TahyObec(databaze,cislo,2) #to samé, ale s věží
            for j in tahy:
                novapoz = Presunpozice(databaze,cislo,2,j)[:-3] 
                if JeLegalni(novapoz): #jestli nejedu do nemožné pozice
                    novapoz = databaze[puredatabaze.index(novapoz)+len(databaze)//2] #přehodím stranu, co je na tahu
                    if novapoz[4] != "Nex":
                       vsechny_tahy.append(["V",j,novapoz[4]]) #figura - cíl. pole - hodnocení
        else:
            tahy = TahyObec(databaze,cislo,1) #seznam cílových polí
            for j in tahy:
                novapoz = Presunpozice(databaze,cislo,1,j)[:-3] 
                if JeLegalni(novapoz): #jestli nejedu do nemožné pozice
                    novapoz = databaze[puredatabaze.index(novapoz)] #přehodím stranu, co je na tahu
                    if novapoz[4] != "Nex":
                        vsechny_tahy.append(["k",j,novapoz[4]]) #figura - cíl. pole - hodnocení
        return vsechny_tahy
    """
    def Explain_All_Moves(databaze,puredatabaze,cislo):
        vsechny_tahy = []
        if databaze[cislo][3] == "B":
            pocet = -1
            na_indexovani = []
            tahy = TahyObec(databaze,cislo,0) #seznam cílových polí
            for j in tahy:
                novapoz = Presunpozice(databaze,cislo,0,j)[:-3] #král
                if JeLegalni(novapoz) and easy_JeSach([novapoz],0)!="B": #jestli nejedu do nemožné pozice
                    pocet += 1
                    novapoz.append(pocet)
                    na_indexovani.append(novapoz)
                    vsechny_tahy.append(["K",j,None]) #figura - cíl. pole - hodnocení
            tahy = TahyObec(databaze,cislo,2) #to samé, ale s věží
            for j in tahy:
                novapoz = Presunpozice(databaze,cislo,2,j)[:-3] 
                if JeLegalni(novapoz) and easy_JeSach([novapoz],0)!="B": #jestli nejedu do nemožné pozice
                    pocet += 1
                    novapoz.append(pocet)
                    na_indexovani.append(novapoz)
                    vsechny_tahy.append(["V",j,None]) #figura - cíl. pole - hodnocení
        else: #černý
            pocet = -1
            na_indexovani = []
            tahy = TahyObec(databaze,cislo,1) #seznam cílových polí
            for j in tahy:
                
                novapoz = Presunpozice(databaze,cislo,1,j)[:-3] 
                if JeLegalni(novapoz) and easy_JeSach([novapoz],0)!="C": #jestli nejedu do nemožné pozice
                    pocet += 1
                    novapoz.append(pocet)
                    na_indexovani.append(novapoz)
                    vsechny_tahy.append(["k",j,None]) #figura - cíl. pole - hodnocení
        na_indexovani.sort()
        zara  = 0
        prepisovy = [[-1,-1] for i in range(len(na_indexovani))]
        for i in range(len(na_indexovani)):
            poop = na_indexovani[i].pop()
            zara = puredatabaze.index(na_indexovani[i],zara)
            prepisovy[i] = [poop,zara]
        prepisovy.sort()
        if databaze[cislo][3] == "B":
            for i in prepisovy: #Známe index cílové pozice, takže se na ni dostaneme a zjistíme její hodnocení - to pak napíšeme do seznamu "vsechny_tahy"
                k,j = i[0],i[1]+len(databaze)//2 #Po tahu bílého je na tahu černý 
                i[1] = databaze[j][4]
                vsechny_tahy[k][2] = i[1]
        else:
            for i in prepisovy:
                k,j = i[0],i[1]
                i[1] = databaze[j][4]
                vsechny_tahy[k][2] = i[1]
        return vsechny_tahy
    def Setridtahy(vsechnytahy,strana): #setřídí výstup Explain_All_Moves podle počtu tahů
        horlimit = 1
        for i in range(len(vsechnytahy)):
            a = vsechnytahy[i][2]
            if type(a) == int and a>=horlimit:
                horlimit = a
        for i in range(len(vsechnytahy)):
            a = vsechnytahy[i][2]
            if type(a) != int:
                if a == "Pat":
                    vsechnytahy[i][2] = horlimit +1
                elif a == "R1":
                    vsechnytahy[i][2] = horlimit +2
                elif a == "R":
                    vsechnytahy[i][2] = horlimit +3
                else:
                    print("Hovadina",vsechnytahy,i)
        vsechnytahy.sort(key=lambda x: x[2],reverse = (strana == "C")) #je-li strana bílá, nejmenší tah je první
        for i in range(len(vsechnytahy)):
            a = vsechnytahy[i][2]
            if a == horlimit+1:
                vsechnytahy[i][2] = "Pat"
            elif a == horlimit+2:
                vsechnytahy[i][2] = "R1"
            elif a == horlimit+3:
                vsechnytahy[i][2] = "R"
        return vsechnytahy
    #Setridtahy(Explain_All_Moves(databaze,puredatabaze,4647),"B")
    #A KONEC, ZACINAME DALSI
    def Vypis(databaze,cislopozice=None,detaily=None):
        if cislopozice == None:
            j = databaze[:]
        else:
            j = (databaze[cislopozice])[:]
        if j[2] == "X":
            print("B: K"+j[0]+"\nČ: K"+j[1])
        else:
            print("B: K"+j[0]+", V"+j[2],"\nČ: K"+j[1])
    def Blbuvzdornost(promenna,sloupce,radky):
        promenna = None
        while not promenna:
            promenna = input(".").strip()
            if promenna == "xx":
                return "X"
            sloup = promenna[0]
            if desloupec(sloup) not in range(1,sloupce+1):
                print("Tato šachovnice má jen",sloupce,"sloupce/ů, napiš znova")
                promenna = None
            else:
                try:
                    rada = int(promenna[1:]) 
                except ValueError:
                    promenna = None
                finally:
                    if rada not in range(1,radky+1):
                        print("Tato šachovnice má jen",radky,"řad/y,napiš znova")
                        promenna = None
        return promenna
    def Sestavpozici(radky,sloupce,puredatabaze):
        K,V,k = None,None,None
        print("Bílý král: ")
        K = Blbuvzdornost(K,sloupce,radky)
        print("Bílá věž (není-li, napiš xx):")
        V = Blbuvzdornost(V,sloupce,radky)
        print("Černý král: ")
        k = Blbuvzdornost(k,sloupce,radky)
        print("Bílý nebo černý na tahu? C/c černý, jinak bílý")
        strana = input().strip()
        if strana and strana[0].lower() == "c":
            strana = 1
        else:
            strana = 0
        try: 
            cislopzc = puredatabaze.index([K,k,V])+strana*len(puredatabaze)//2
            return cislopzc
        except ValueError: 
            print("Zadaná pozice neexistuje")
            return "Chyba"
    def Provedtah(vstup):
            vstup = vstup.replace(" ", "")
            if vstup[2] not in ("0123456789"):
                print("Není sloupec")
                return "Opak" 
            if vstup[0] in ("Kk"):
                return ("k"+vstup[1:])
            elif vstup[0] in ("Vv"):
                return ("v"+vstup[1:])
            else:
                print("Neplatná figura")
                return "Opak"
    def easy_Presunpozice(jasnapozice,figura,pole):
        j = jasnapozice[:]
        if pole not in j:
            j[figura] = pole
        else:
            k = j.index(pole)
            j[k] = "X" #odstraníme figuru ze šachovnice
            j[figura] = pole
        return j
    def Hraj(databaze,puredatabaze,cislopozice = None):
        if cislopozice == None:
            j = databaze[:]
        else:
            j = (databaze[cislopozice])[:]
        Vypis(j)
        if j[4] == "R":
            print ("Remiza")
            return
        elif j[4] == "P":
            print ("Pat, remiza")
            return
        elif j[4] != 0 and j[4] != "0":
            print("Hrac na tahu:",j[3])
            r = "Nelegalni"
            while r == "Nelegalni":
                va = "Opak"
                while va == "Opak":
                    va = Provedtah(input("Napis tah: figura-sloupec-řada\n"))
                t = databaze.index(j)
                if va[0] == "k":
                    a = t//(len(databaze)//2) #0 nebo 1 - za půlkou/před půlkou
                elif va[0] == "v":
                    a = 2
                r =  Finalpozice(databaze,t,a,va[1:],puredatabaze)
                if r == "Nelegalni":
                       print("Nemozny tah")
            print("Nova pozice:")
            Hraj(databaze,puredatabaze,databaze.index(r))
        else:
            print ("Je mat, vyhral bily")

    def Hraj_PvC(databaze,puredatabaze,cislopozice=None): #rekurzivně, až do matu
        if cislopozice == None:
            j = databaze
            if j in puredatabaze:
                t = databaze.index(j)
            else:
                print("Nepřípustná pozice")
                return
        else:
            j = databaze[cislopozice]
            t = cislopozice
        Vypis(j)
        if j[4] == "R":
            print ("Remiza")
            return
        elif j[4] != 0 and j[4] != "0":
            print("Hrac na tahu:",j[3])
            r = "Nelegalni"
            while r == "Nelegalni":
                if t < (len(puredatabaze)//2): #bílý
                    #Vygeneruju náhodný tah z možných
                    tahy = TahyObec(puredatabaze,t,0)
                    if tahy!=None:
                        tahy.append([1])
                    tahy.append(TahyNeom(puredatabaze,t,2))
                    if 1 in tahy:
                        f = tahy.index(1)
                        b = f+0
                    else:
                        b,f = (3*(radky+sloupce)),(3*(radky+sloupce))
                    while b == f:
                        b = random.randint(0,len(tahy)-1)
                    if b < f:
                        r =  Finalpozice(databaze,t,0,tahy[b],puredatabaze)
                    else:
                        r = Finalpozice(databaze,t,2,tahy[b],puredatabaze)
                else: #černý #ten má jenom jednu figuru, takže je to jednodušší
                    tahy = TahyObec(puredatabaze,t,1)
                    nel = NelegalKral(puredatabaze,t,1)
                    if all (tahy[i] in nel for i in range(len(tahy))):
                            print("Pat, remiza")
                            return
                    b = random.randint(0,len(tahy)-1)
                    r =  Finalpozice(databaze,t,1,tahy[b],puredatabaze)
            time.sleep(0.5)
            print("Nova pozice:")
            Hrajauto_random(databaze,puredatabaze,databaze.index(r))
        else:
            print ("Je mat, vyhral bily")
            return
    def Hraj_CvC(databaze,puredatabaze,cislopozice=None,tahy=1,zapis="",auto = 0): #rekurzivně, až do matu
        j = databaze[cislopozice]
        t = cislopozice
        Vypis(j)
        if j[4] == "Nex":
            print("Nepřípustná pozice")
            return "Není co zapisovat"
        if j[4] == "R":
            print ("Remiza")
            if zapis == "":
                return "Není co zapisovat"
            else:
                return zapis
        elif j[4] != 0 and j[4] != "0":
            if j[3] == "B":
                strana = "Bílý"
            else:
                strana = "Černý"
            print("Hrac na tahu:",strana,"; Zbývající tahy do matu:", (j[4]+1)//2)
            if zapis == "":
               if j[3] == "C":
                zapis += "1... "
                tahy += 1
               else:
                zapis += "1. "
            else:
                if j[3] == "C":
                    zapis += " "
                    tahy += 1
                else:
                    zapis += (" "+str(tahy)+". ")
            moznetahy = Setridtahy(Explain_All_Moves(databaze,puredatabaze,t),j[3])
            rozsah = 1 #rozsah nejlepších tahů
            nejlepsi_hodnoceni = moznetahy[0][2]
            while (rozsah <len(moznetahy)) and (moznetahy[rozsah][2] == nejlepsi_hodnoceni): #všechny nejlepší tahy
                rozsah += 1
            vyber = random.randint(1,rozsah) #vyberu náhodný tah z nejlepších
            vyber = moznetahy[vyber-1]
            if vyber[0] == "K":
                novapozice = Presunpozice(databaze,t,0,vyber[1])[:-3]
                novapozice = databaze[puredatabaze.index(novapozice)+len(puredatabaze)//2]
            elif vyber[0] == "k":
                novapozice = Presunpozice(databaze,t,1,vyber[1])[:-3]
                novapozice = databaze[puredatabaze.index(novapozice)]
            elif vyber[0] == "V":
                novapozice = Presunpozice(databaze,t,2,vyber[1])[:-3]
                novapozice = databaze[puredatabaze.index(novapozice)+len(puredatabaze)//2]
            else:
                print("Blbost",vyber)
            time.sleep(0.2)
            zapis += (vyber[0].upper()+vyber[1])
            if auto == 0:
                autom = input("Další tah-Enter; Napiš A pro hru automaticky do konce")
                if autom.lower() == "a":
                    auto = 1
                else:
                    auto = 0
            print("Nova pozice:")
            return Hraj_CvC(databaze,puredatabaze,databaze.index(novapozice),tahy,zapis,auto)
        else:
            if zapis == "":
                return "Není co zapisovat"
            else:
                return zapis
    """print("Nahrána databáze? Dobré. Jak to chceš?")
    print("A: vlastní tahy za obě strany\nB: Ty proti počítači\nC: Počítač proti sobě")
    cor = input()"""
    cor = "c" #nechám počítač vs počítač jako defaultní možnost, auto-input řešit nebudu
    """if type(cor) == str:
        #print(cor,"JO")
        cor=cor.casefold()
    while cor not in ("a","b","c"):
        print("Err\n")
        cor = input()
        if type(cor) == str:
            cor=cor.casefold()"""
    cislopzc = -2
    
    while cislopzc == -2:
              print("Dej:\n0 - pokud chceš pozici manuálně\n-1 - pokud náhodně\njiné číslo - konkrétní řádek pozice v databázi")
              k = input()
              try:
                  k = int(k)
                  if k not in range(-1,len(databaze)+1): #nulu a -1 mám speciálně vyhrazenou
                      print("Taková pozice není v databázi, má jen",len(databaze),"řádků, a neberu záporná čísla.")
                  else:
                    cislopzc = k
              except ValueError:
                  print("Není číslo")
                  pass

    if cislopzc == 0:
        zacatecni = Sestavpozici(radky,sloupce,puredatabaze)
        while zacatecni == "Chyba" or databaze[zacatecni][4] == "Nex":
            print("Pozice neexistuje")
            zacatecni = Sestavpozici(radky,sloupce,puredatabaze)
        cislopzc = zacatecni
    elif cislopzc == -1:
        a = "x"
        while a == "x":
            print("Kdo je na tahu?\n0/A - bílý\n1/L - černý\n2 - náhodně")
            a = input()
            if a not in "0aA1lL2":
                a = x
                print("Zadej znova")
            else:
                if a in "0aA":
                    a = 0
                elif a in "1lL":
                    a = 1
                else:
                    a = random.randint(0,1)
        cislopzc = (random.randint(0,len(databaze)//2)-1+a*len(databaze)//2)+1
        while databaze[cislopzc-1][4] == "Nex":
            cislopzc = (random.randint(0,len(databaze)//2-1)+a*len(databaze)//2)+1
    if cor == "a":
        zapsane = Hraj(databaze,puredatabaze,cislopzc-1) #začínám od nuly - první pozice = nultý řádek
    elif cor == "b":
        zapsane = Hraj_PvC(databaze,puredatabaze,cislopzc-1)
    elif cor == "c":
        zapsane = Hraj_CvC(databaze,puredatabaze,cislopzc-1)
    else:
        print(cor)
        print("Jakýže styl hry jsi chtěl? Nějaká blbost. Restartuj program")
        raise ValueError
    print("\n\n\nPůvodní pozice:")
    Vypis(databaze,cislopzc-1)
    print("Číslo pozice:",cislopzc)
    print("\n\n\nZápis:")
    print(zapsane)
    input()
def Deformat(soubor):
    # otevřeme
    with open(soubor, 'r') as f:
        cteme = f.read()

    # nahradíme
    novy = cteme.replace(']\n[','],[' )

    # zapíšeme pod novým názvem
    sos = soubor[7:]
    print(sos)
    with open(sos, 'w+') as f:
        pis = '['+novy+']' #závorky na konec
        f.write(pis)
    print("dne")
def Nahraj(soubor): #i s přípono
            with open(soubor,"r") as e:
                datab = e.read()
                print("rd")
                vysledek = eval(datab)
                print("evl")
            return vysledek
def Zadej_Velikost():
    a,b = 0,0
    while a == 0:
                k = input("Zadej počet řádků šachovnice (3-12) ")
                try:
                    k = int(k)
                    if k not in range(3,13):
                        print("Nepovolený rozsah")
                    else:
                        a = k
                except ValueError:
                    print("Není číslo")
                    pass
    while b == 0:
                l = input("Zadej počet sloupců šachovnice (3-12) ")
                try:
                    l = int(l)
                    if l not in range(3,13):
                        print("Nepovolený rozsah")
                    else:
                        b = l
                except ValueError:
                    print("Není číslo")
                    pass
    return a,b



print("Nejdřív vyber velikost šachovnice.")
a,b = Zadej_Velikost()
a,b = str(a),str(b)
zacatek = "Format_Pozice_Finish"+a+"x"+b+".txt"
soubor = False
try:
    soubor = open(zacatek,"r")
    soubor = True
except ValueError:
    print("Nemám databázi pro tuto šachovnici. Nejdříve ji vygeneruj.")
if soubor:
    dtb,prdtb = Hotovo(zacatek,a,b)
    znova = True
    while znova != "x":
        Nova_Partie(dtb,prdtb,int(a),int(b))
        znova = input("\n\n\n\nNová partie? Pokud chceš ukončit, napiš X ").lower()
