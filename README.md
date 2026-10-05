# python-csv-data-analysis
# Python CSV Data Analysis

Tento skript slúži na načítanie, filtrovanie a analýzu produktových dát uložených v CSV súbore.

## Funkcionalita
- **Načítanie dát:** Využíva vstavaný modul `csv` (`csv.DictReader`) na spracovanie structured dát.
- **Konverzia typov:** Prevádza textové dáta na dátové typy `float` (cena) a `bool` (dostupnosť na sklade).
- **Filtrovanie a agregácia:** Vyhľadáva špecifickú kategóriu produktov (napr. Elektronika) a spočítava ich celkovú sumu.

## Ako spustiť skript
1. Uisti sa, že súbor `produkty.csv` sa nachádza v rovnakej zložke ako skript.
2. Spusti skript pomocou príkazu:
   ```bash
   python analyza_produktov.py
