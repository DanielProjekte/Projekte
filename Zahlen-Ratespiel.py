import random

zahl = random.randint(1, 100)
versuche = 0

while True:
    eingabe = int(input("Rate die Zahl (1-100): "))
    versuche += 1

    if eingabe == zahl:
        print(f"Glückwunsch! Du hast die Zahl in {versuche} Versuchen erraten.")
        if versuche <= 5 and eingabe == zahl:
                print("Du bist ein Super-Star!")
        break
    elif eingabe < zahl:
        print("Die gesuchte Zahl ist größer.")
    else:
        print("Die gesuchte Zahl ist kleiner.")
    if versuche >= 10:
        print(f"Leider hast du die Zahl nicht erraten. Die gesuchte Zahl war {zahl}.")
        if input("Möchtest du es noch einmal versuchen? (j/n): ").lower() == 'j':
            zahl = random.randint(1, 100)
            versuche = 0
        else:
            break
            
    


