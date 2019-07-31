import pandas as pd

df = pd.read_csv("20190722-100342708-umsatz.CSV",
                 sep=';', parse_dates=True, decimal=',', encoding='iso8859_15')
categories = []
for index, row in df.iterrows():
    if row["Betrag"] >= 0:
        categories.append("Einnahme")
        continue
    print("-- Categories: --")
    print("1) Nahrung & Verbrauchsartikel")
    print("2) Kleidung & Accessoires")
    print("3) Dienstleistungen & Gebühren")
    print("4) Miete & laufende Verträge")
    print("5) Möbel & Einrichtung")
    print("6) Transport")
    print("7) Unterhaltung")
    print("8) Technik")
    print("9) Unbekannt & Bargeld")
    r = row[["Buchungstag", "Buchungstext", "Verwendungszweck",
             "Beguenstigter/Zahlungspflichtiger", "Betrag", "Waehrung"]]
    print(r["Buchungstag"] + ": " + r["Buchungstext"])
    print("  Verwendungszweck:")
    print(r["Verwendungszweck"])
    if r["Betrag"] >= 0:
        print("  Von: " + str(r["Beguenstigter/Zahlungspflichtiger"]))
    else:
        print("  An: " + str(r["Beguenstigter/Zahlungspflichtiger"]))
    print(str(r["Betrag"]) + " " + r["Waehrung"])
    no_input = True
    while(no_input):
        inp = input("Category: ")
        if inp == "1":
            categories.append("Nahrung & Verbrauchsartikel")
            no_input = False
        elif inp == "2":
            categories.append("Kleidung & Accessoires")
            no_input = False
        elif inp == "3":
            categories.append("Dienstleistungen & Gebühren")
            no_input = False
        elif inp == "4":
            categories.append("Miete & laufende Verträge")
            no_input = False
        elif inp == "5":
            categories.append("Möbel & Einrichtung")
            no_input = False
        elif inp == "6":
            categories.append("Transport")
            no_input = False
        elif inp == "7":
            categories.append("Unterhaltung")
            no_input = False
        elif inp == "8":
            categories.append("Technik")
            no_input = False
        elif inp == "9":
            categories.append("Unbekannt & Bargeld")
            no_input = False
df["Kategorie"] = categories
df = df[["Buchungstag", "Buchungstext", "Verwendungszweck",
         "Beguenstigter/Zahlungspflichtiger", "Betrag", "Waehrung", "Kategorie"]]
df = df[df["Kategorie"] != "Einnahme"]
df.to_csv("bankdaten.csv", sep=',')
