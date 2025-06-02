sek = float(input("SEK: "))
valuta = input("Valuta att konvertera till: ").upper()
if valuta == "USD":
    sektusd = sek * 0.092
    print(f"{sek} kr är värt {sektusd} USD")
elif valuta == "EUR":
    sekteur = sek * 0.10
    print(f"{sek} kr är värt {sekteur} EUR")
elif valuta == "GBP":
    sektgbp = sek * 0.077
    print(f"{sek} kr är värt {sektgbp} GBP")
elif valuta == "JPY":
    sektjpy = sek * 0.067
    print(f"{sek}kr är värt {sektjpy} JPY")
else:
    print("Denna valuta stöds inte än")