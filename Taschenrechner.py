def taschenrechner():
    
    rechnungen=[]

    print("Willkommen zum Taschenrechner!")
    
    while True:
        try:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            operator = input("Gib den Operator ein (+, -, *, /, %, **): ")
            zahl2 = float(input("Gib die zweite Zahl ein: "))

            if operator == "+":
                ergebnis = zahl1 + zahl2
            elif operator == "-":
                ergebnis = zahl1 - zahl2
            elif operator == "%":
                ergebnis = zahl1 % zahl2
            elif operator == "**":
                ergebnis = zahl1 ** zahl2
            elif operator == "*":
                ergebnis = zahl1 * zahl2
            elif operator == "/":
                if zahl2 != 0:
                    ergebnis = zahl1 / zahl2
                else:
                    print("Fehler: Division durch Null ist nicht erlaubt.")
                    continue
            else:
                print("Ungültiger Operator. Bitte versuche es erneut.")
                continue
            if ergebnis.is_integer() and zahl1.is_integer() and zahl2.is_integer():
                ergebnis = int(ergebnis)
                zahl1 = int(zahl1)
                zahl2 = int(zahl2) 
            print(f"Das Ergebnis von {zahl1} {operator} {zahl2} ist: {ergebnis}")
            rechnungen.append(f"{zahl1} {operator} {zahl2} = {ergebnis}")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")
        
        fortsetzen = input("Möchtest du eine weitere Berechnung durchführen? (j/n): ").lower()
        if fortsetzen != 'j':
            print("Danke fürs Benutzen des Taschenrechners! Auf Wiedersehen!")
            print("Hier sind deine bisherigen Berechnungen:")
            print("\n".join(rechnungen))
            break

taschenrechner()