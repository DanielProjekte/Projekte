
import random

def vokabel_trainer():
    
    vokabeln = {
        "Haus": "house",
        "Baum": "tree",
        "Auto": "car",
        "Buch": "book",
        "Stuhl": "chair",
        "Tisch": "table",
        "Fenster": "window",
        "Tür": "door",
        "Straße": "street",
    }
    vokabel_falsch = []
    deutsche_woerter = list(vokabeln.keys())
    random.shuffle(deutsche_woerter)
    score = 0
    
    # VOKABELN ABFRAGEN
    for deutsches_wort in deutsche_woerter:
        englisches_wort = vokabeln[deutsches_wort]
        richtung = random.choice(["deutsch-englisch", "englisch-deutsch"])
        if richtung == "deutsch-englisch":
            eingabe = input(f"Wie heißt '{deutsches_wort}' auf Englisch? ")
            if eingabe.strip().lower() == englisches_wort:
                print("Richtig!")
                score += 1
            else:
                vokabel_falsch.append((deutsches_wort, englisches_wort))
                print(f"Falsch! Die richtige Antwort ist '{englisches_wort}'.")
        else:
            eingabe = input(f"Wie heißt '{englisches_wort}' auf Deutsch? ")
            if eingabe.strip().lower() == deutsches_wort.lower():
                print("Richtig!")
                score += 1
            else:
                vokabel_falsch.append((deutsches_wort, englisches_wort))
                print(f"Falsch! Die richtige Antwort ist '{deutsches_wort}'.")
    print(f"Dein Ergebnis: {score} von {len(vokabeln)} richtig. Das sind {score / len(vokabeln) * 100:.1f}% richtig.")
    
    
    
    # DIE FALSCHEN VOKABELN NOCHMAL ÜBEN
    while score < len(vokabeln):
        print("\nLass uns die falsch beantworteten Vokabeln noch einmal üben.")
        for deutsches_wort, englisches_wort in vokabel_falsch[:]:
            eingabe = input(f"Wie heißt '{deutsches_wort}' auf Englisch? ")
            if eingabe.strip().lower() == englisches_wort:
                print("Richtig!")
                score += 1
                vokabel_falsch.remove((deutsches_wort, englisches_wort))
            else:
                print(f"Falsch! Die richtige Antwort ist '{englisches_wort}'.")
        


vokabel_trainer()    