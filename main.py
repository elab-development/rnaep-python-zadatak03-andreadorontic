import random
import math

# 1. Lista proizvoda
proizvodi = [
    "Laptop",
    "Mis",
    "Tastatura",
    "Monitor",
    "Slusalice",
    "Web kamera",
    "USB memorija",
    "Stampac"
]

# 2. Recnik proizvoda i cena
cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 49.99,
    "Monitor": 220.50,
    "Slusalice": 89.90,
    "Web kamera": 45.75,
    "USB memorija": 15.49,
    "Stampac": 130.00
}

# 3. Ispis svih proizvoda i cena
print("Svi proizvodi i njihove cene:")
for proizvod in proizvodi:
    print(f"- {proizvod} - {cene[proizvod]} €")

print()

# 4. Unos budzeta i ispis proizvoda koje korisnik moze da priusti
budzet = float(input("Unesite svoj budzet u evrima: "))

print("Proizvodi koje mozete da priustite:")
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(f"- {proizvod} - {cene[proizvod]} €")

print()

# 5. Funkcija najskuplji_proizvod()
def najskuplji_proizvod(recnik_cena):
    return max(recnik_cena, key=recnik_cena.get)

najskuplji = najskuplji_proizvod(cene)
print(f"Najskuplji proizvod je: {najskuplji} - {cene[najskuplji]} €")

print()

# 6. Nasumican proizvod
nasumican_proizvod = random.choice(proizvodi)
print(f"Korisniku je privukao paznju proizvod: {nasumican_proizvod}")

print()

# 7. Prosecna cena
zbir_cena = sum(cene.values())
prosecna_cena = zbir_cena / len(cene)
prosecna_cena = math.floor(prosecna_cena * 100 + 0.5) / 100
print(f"Prosecna cena svih proizvoda je: {prosecna_cena:.2f} €")

print()

# 8. Broj prodatih komada i ukupan prihod
prodati_komadi = [5, 20, 12, 7, 10, 8, 25, 4]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]

print(f"Ukupan prihod je: {ukupan_prihod:.2f} €")

print()

# 9. Dodavanje novog proizvoda
novi_proizvod = "Tablet"
proizvodi.append(novi_proizvod)
cene[novi_proizvod] = 299.99

print("Azurirana lista proizvoda:")
for proizvod in proizvodi:
    print(f"- {proizvod}")

print()

# 10. Sortiranje proizvoda po ceni
sortirani_proizvodi = sorted(cene.items(), key=lambda x: x[1])

print("Proizvodi sortirani po ceni:")
for proizvod, cena in sortirani_proizvodi:
    print(f"- {proizvod} - {cena} €")