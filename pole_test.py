konzole = ["Xbox One", "Xbox series X", "Xbox series S", "Playstation 4", "Playstation 5", "KFC station"]
kosik = []

print("------------------------------")
print("Vítejte v Techtown obchodu")
print("------------------------------")

def vypis_konzole():
    print("------------------------------")
    print("Zde je náš výběr herních konzolí")
    print("------------------------------")

def vypis_kosik():
    print("------------------------------")
    print("Zde je stav Vašeho košíku")
    print("------------------------------")

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"Konzole s číslem {x+1}: {prvek[x]}")
        print("------------------------------")

print("Zde si můžete vybrat z našeho dostupného zboží")
print("Vybírat můžete číslem produktu ve skladu")
print("Pro ukončení nebo pokračování Vašeho nákupu potom zadejte příkaz ano, nebo ne ")


while True:
        vypis_konzole()
        vypis_pole(konzole)

        vyber = int(input("Zadejte číslo produktu, který chcete vybrat: "))


        if 0 < vyber <=len(konzole):
            kosik.append(konzole[vyber-1])
            vypis_kosik()
            vypis_pole(kosik)
            konzole.pop(vyber-1)

        elif len(konzole) == 0:
         print("Tohle jsou všechny produkty, které jsme měli dostupné")
         vypis_kosik()
         vypis_pole(kosik)
         print("Děkujeme za Váš nákup v Techtownu")

        else:
            print("Obáváme se, že tenhle produkt teď není ve skladě")
            continue

        pokracovat = input("Chcete pokračovat v nákupu? (ano/ne) ").lower()
        
        if pokracovat != 'ano':
            vypis_kosik()
            vypis_pole(kosik)
            print("Děkujeme za Váš nákup v Techtownu")
            break
