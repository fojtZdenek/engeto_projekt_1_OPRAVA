"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Fojt
email: zdenek.fojt@gmail.com
discord: Zdeněk F.
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


ODDELOVAC = "----------------------------------"


reg_uziv = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
jmeno = input("Username: ")

heslo = input("Pasword: ")
print(ODDELOVAC)

if reg_uziv.get(jmeno) == heslo:
    print(f"Vítej v aplikaci {jmeno}!")
    print("Máme 3 texty k analyzování")
else:
    print("Uživatelské jmeno nebo heslo nejsou v pořádku ukončuji program!")
    exit()

print(ODDELOVAC)


vyber_textu = input("Zadej číslo textu od 1 do 3: ")
if int(vyber_textu.isnumeric()) > 3 or int(vyber_textu.isnumeric()) < 1:
    print("Špatné číslo nebo hodnota!") 

else:
    print(f"Správný výběr, vybral jsi text číslo {vyber_textu}")
print(ODDELOVAC)


cista_slova = []
for slovo in TEXTS[int(vyber_textu) -1].split():
    cista_slova.append(slovo.strip("., ,, ;"))

soucet_slov = len(cista_slova)
print(f"Ve vybraném textu je {soucet_slov}")


slova_z_v_pismeny = []
for slovo in TEXTS[int(vyber_textu) -1].split():
    if slovo[0].isupper():
        slova_z_v_pismeny.append(slovo)
                   
pocet_slov2 = len(slova_z_v_pismeny)
print(f"Počet slov začínajícími velkými písmeny je {pocet_slov2}")


slova_V_pismena = []
for slovo in TEXTS[int(vyber_textu) -1].split():
    for pismeno in slovo.split():
        if pismeno.isupper() and slovo.isalpha():
            slova_V_pismena.append(slovo)

soucet_slov3 = len(slova_V_pismena)
print(f"Součet slov psanými velkými písmeny je {soucet_slov3}")



slova_M_pismena = []
for slovo in TEXTS[int(vyber_textu) -1].split():
    for pismeno in slovo.split():
        if pismeno.islower():
            slova_M_pismena.append(slovo)

soucet_slov4 = len(slova_M_pismena)
print(f"Součet slov psanými malými písmeny je {soucet_slov4}")

pocet_cisel = []
for slovo in TEXTS[int(vyber_textu) -1].split():
    if slovo.isnumeric():
            pocet_cisel.append(slovo)

soucet_cisel = len(pocet_cisel)

print(f"V textu je {soucet_cisel} čísel")

soucet_vsech_cisel = []

for slovo in TEXTS[int(vyber_textu) -1].split():
    if slovo.isnumeric():
        soucet_vsech_cisel.append(int(slovo))
            
suma_cisel = sum(soucet_vsech_cisel)
print(f"Součet všech čísel v textu je {suma_cisel}")

print(ODDELOVAC)

print(f"LEN|   VYSKYT  |CISLO|")
print(ODDELOVAC)  


vycistena_slova = []
for slovo in TEXTS[int(vyber_textu) -1].split():
    ciste_slovo = slovo.strip(",.:;'")
    vycistena_slova.append(ciste_slovo.lower())


delka_slov = {}


for slovo in vycistena_slova:
    delka_slova = len(slovo)
    if delka_slova in delka_slov:
        delka_slov[delka_slova] += 1
    else:
        delka_slov[delka_slova] = 1


for delka, cetnost in sorted(delka_slov.items()):
    vyskyt_slov = int(delka_slov[delka]) * "*"
    print(
        f"{delka:>3}|{vyskyt_slov:<12}|{cetnost:}",
        sep="\n")
    











   






