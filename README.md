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
V případě ukončení programu přijdete pouze o momentálně generovanou databázi.
1.1.3 Volba "systematicky vzestupně" (B)
Tato volba bude generovat databáze šachovnic velikostí od 3x3 do 12x12, seřazeny vzestupně podle součinu rozměrů (tzn. celkového počtu polí na šachovnici).
Další informace viz 1.1.2
1.1.4. Volba "systematicky sestupně" (C)
Tato volba bude generovat databáze šachovnic velikostí od 3x3 do 12x12, seřazeny sestupně podle součinu rozměrů (tzn. celkového počtu polí na šachovnici).
1.1.5 Defaultní volba (jinak)
Tato volba umožňuje uživateli zvolit libovolné rozměry šachovnice, přičemž vstupem musí být dvě čísla od 3 do 12. Vygenerována je pouze jedna databáze.
Existuje-li databáze daných rozměrů a nebylo-li povoleno přepisování (viz 1.1.1), bude uživatel znovu dotázán, zdali chce danou databázi přepsat.
2. Jak číst výstupní soubor
Výstupní soubor obsahuje na každém řádku šestimístný seznam, kde jednotlivé prvky značí (číslováno 1-6).

Druhý program pak přijímá tento soubor jako vstup a dokáže simulovat skutečnou hru. O tom, který tah je dobrý či nikoli, rozhoduje právě ohodnocení dané pozice.
Při spuštění programu "ZkousFin" budete dotázáni, 
