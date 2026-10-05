import csv

vsetky_produkty = []
with open("produkty.csv", "r", encoding="utf-8") as subor:
    citat = csv.DictReader(subor)
    for riadok in citat:

        riadok["cena"] = float(riadok["cena"])
        riadok["na_sklade"] = riadok["na_sklade"] == "True"
        vsetky_produkty.append(riadok)

print(f"Naložených bolo {len(vsetky_produkty)} produktov.\n")

elektronika_na_sklade = []
celkova_suma = 0.0

for produkt in vsetky_produkty:
    if produkt["kategoria"] == "Elektronika" and produkt["na_sklade"]:
        elektronika_na_sklade.append(produkt)
        celkova_suma += produkt["cena"] 
print("--- ELEKTONIKA NA SKLADE ---")
for item in elektronika_na_sklade:
 print(f"{item['produkt']} - {item['cena']} €")

print(f"\nCelkova suma elektroniky na sklade je: {celkova_suma} €")

