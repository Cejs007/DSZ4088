import os
import pickle
import json

# data ke stažení na https://www.google.com/url?q=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F11N7UM7qUWlRxbvMwMKKbDj6Js7yy7_GJ%2Fview%3Fusp%3Dsharing

# do listu uložit soubory, které jsou ve složce files
soubory = os.listdir("Files")
# roztřídit soubory podle koncovky -> různé formáty se načítají trošku jinak
json_soubory = [soubor for soubor in soubory if soubor.endswith(".json")]
pickle_soubory = [soubor for soubor in soubory if soubor.endswith(".obj")]
text_soubory = [soubor for soubor in soubory if soubor.endswith(".txt")]
# nachystáme disctionary na výsledky -> nazev_souboru: text
texty = {}
# zpracování pickle souborů
for soubor in pickle_soubory:
    # získat název ze souboru (5.txt -> rozdělit podle tečky a vzít první část)
    nazev = soubor.split(".")[0]
    # načtení dat z pickle souboru
    with open(f"Files{os.sep}{soubor}", "rb") as reference:
        texty[nazev] = pickle.load(reference)
# zpracování json souborů
for soubor in json_soubory:
    # získat název ze souboru (5.txt -> rozdělit podle tečky a vzít první část)
    nazev = soubor.split(".")[0]
    # načtení dat z json souboru
    with open(f"Files{os.sep}{soubor}", "rt") as reference:
        texty[nazev] = json.load(reference)
# zpracování txt souborů
for soubor in text_soubory:
    # získat název ze souboru (5.txt -> rozdělit podle tečky a vzít první část)
    nazev = soubor.split(".")[0]
    # načtení dat z txt souboru
    with open(f"Files{os.sep}{soubor}", "rt") as reference:
        texty[nazev] = reference.read()
# jak seřadit slova ve správném pořadí?
# kolik slov mám?
pocet = len(texty.keys())
# vytvořím list s nulami -> placeholder pro každé slovo
vysledny_text = pocet * [0]
# číslování souobrů odpovídá indexování v Pythonu -> vezmu název souboru (číslo) a použiji jako index
for pozice, text in texty.items():
    # do výsledků pod index zapiš dané slovo
    vysledny_text[int(pozice)] = text
# spoj list se slovy do souvislého textu -> přes mezeru
print(" ".join(vysledny_text))