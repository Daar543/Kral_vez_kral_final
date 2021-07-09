1. Program ZkousFin

1.0 - Jak funguje tento program

Program "ZkousFin" vygeneruje všechny možné pozice (tento soubor se dále bude označovat jako "databáze") které mohou vzniknout v koncovce "král a věž proti králi". Každé z těchto pozic přiřadí 
hodnocení, které rozhodne o tom, zdali je daná pozice remíza, či za kolik nejvíce půltahů (jeden půltah = hraje bílý nebo černý) lze vynutit mat.
Výstupem je soubor, obsahující všechny pozice ve formátu pythonovských seznamů.

1.1 - Možné vstupy
Při spuštění dostane uživatel 4 možnosti + možnost ukončení programu. Volba možnosti se provádí stisknutím příslušného tlačítka na klávesnici (na velikosti nezáleží) a stisknutím klávesy "Enter".
Je-li vstup neplatný či je stisknuta pouze klávesa "Enter", provede se defaultní možnost, označena "Jinak".

1.1.1 Přepisování starých pozic

Tato volba se ukáže, není-li zvolena možnost ukončení. Potvrzením ("A") se budou přepisovat databáze, které již byly vygenerovány
a nacházejí se ve stejné složce jako spouštěný program. V případě defaultní možnosti (viz 1.1.4) bude uživatel v případě nepotvrzení dotázán ještě jednou.

1.1.2 Volba "náhodně" (A)

Tato volba bude generovat databáze šachovnic velikostí od 3x3 do 12x12 (celkem 100) v náhodném pořadí. Nebudou znovu generovány již vygenerované databáze, nebyla-li potvrzena možnost přepsání.
V případě násilného ukončení programu přijdete pouze o momentálně generovanou databázi.

1.1.3 Volba "systematicky vzestupně" (B)

Tato volba bude generovat databáze šachovnic velikostí od 3x3 do 12x12, seřazeny vzestupně podle součinu rozměrů (tzn. celkového počtu polí na šachovnici).
Další informace viz 1.1.2

1.1.4. Volba "systematicky sestupně" (C)

Tato volba bude generovat databáze šachovnic velikostí od 3x3 do 12x12, seřazeny sestupně podle součinu rozměrů (tzn. celkového počtu polí na šachovnici).

1.1.5 Defaultní volba (jinak)

Tato volba umožňuje uživateli zvolit libovolné rozměry šachovnice, přičemž vstupem musí být dvě čísla od 3 do 12. Vygenerována je pouze jedna databáze.
Existuje-li databáze daných rozměrů a nebylo-li povoleno přepisování (viz 1.1.1), bude uživatel znovu dotázán, zdali chce danou databázi přepsat.

1.2 Textové výstupy v průběhu programu

Význam těchto výstupů je popsán v dokumentaci pro vývojáře. 

1.3 Výstupní soubory

1.3.1 Format_Pozice_Finish

Viz část 2 (Jak číst výstupní soubor). Pouze tento soubor je nutný pro samotné hraní - ostatní soubory lze bez problému smazat (po vygenerování).

1.3.2 Pozice_Finish

Obsahuje stejná data jako soubor v 1.3.1, pouze bez konců řádků.

1.3.3. Format_Stromecek_pred, Format_Stromecek_nasl

Soubory reprezentující strom hry. Každý řádek obsahuje seznam ID pozic, z nichž se dalo dostat do pozice, (resp. do nichž se dá dostat z pozice), jejíž ID je číslo řádku. Algoritmus pro generování pozic je vždy generuje ve stejném pořadí, a tak ID jednoznačně určuje danou pozici.

1.3.4 Vyvoj_Pozice_Finish

Spojitý graf ukazující, že [osa X] pozic potřebuje [osa Y] tahů do matu.

2. Jak číst výstupní soubor 

Výstupní soubor obsahuje na každém řádku šestimístný seznam, kde jednotlivé prvky značí (číslováno 1-6):

2.1 Pozice bílého krále

2.2 Pozice černého krále

2.3 Pozice bílé věže - je-li zde uvedeno "'X'", věž se nenachází na šachovnici 

2.4 Strana, která je na tahu

B = Bílý, C = černý

2.5 Počet tahů do matu

0 = v pozici je mat

liché číslo (L) = bílý při nejlepší hře obou stran dá mat za L půltahů, tedy (L+1)/2 celých tahů

sudé číslo (S) = černý při nejlepší hře obou stran dostane mat za S půltahů, tedy S/2 celých tahů

R = pozice je okamžitě remíza

R1 = černý může remizovat svým tahem

Pat = v pozici je pat, tzn. černý nemá platný tah a zároveň není v šachu

Nex = pozice neexistuje, v této pozici daná strana nemůže být na tahu

2.6 Strana, která je v šachu

B = bílý, C = černý, N = nikdo

3. Program Hotovo_hraj

Tento program dokáže simulovat skutečnou šachovou hru. O tom, který tah je dobrý či nikoli, rozhoduje právě ohodnocení dané pozice, viz 2.5.

Při spuštění programu "Hotovo_hraj" bude uživatel dotázán, aby specifikoval velikost šachovnice. Po zadání této velikosti je zkontrolováno, zdali se soubor vygenerovaný programem ZkousFin nachází v dané složce, a pokud ano, uživatel může zadat číslo pozice (odpovídá řádku v textovém souboru Format_Pozice_Finish...) nebo zkusit napsat pozici sám volbou "0", nebo nechat pozici náhodně, volbou "-1". 

Počítač pak bude z výsledné pozice hrát nejlepší tahy (je-li jich více, pak náhodně) a uživateli se zobrazí pozice po tomto provedeném tahu - musí tedy zapojit svoji představivost. 

Další tah spustí klávesou "Enter". Pokud před stisknutím klávesy "Enter" zadá "A" nebo "a", počítač ihned dohraje pozici až do matu.

Vždy po dokončení pozice se na výstup vytiskne i původní pozice a zápis jednotlivých tahů.

Po dalším stisknutí "Enter" se program neukončí, uživatel může zadat další pozici, ze které se bude hrát, ovšem na šachovnici stejných rozměrů (již se nemusí znovu načítat).

