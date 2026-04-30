import json
import os
SAVE_FILE = "passwoerter.json"

def laden():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def speichern(passwoerter):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(passwoerter, f, ensure_ascii=False, indent=2)
# Logik des Passwort-Managers


def aktualisieren(passwoerter):
    if not passwoerter:
        print("Keine Passwörter gespeichert.")
        return
    print("Gespeicherte Passwörter:")
    for website, daten in passwoerter.items():
        print(f"Website: {website}, Benutzername: {daten['benutzername']}, Passwort: {daten['passwort']}")


def passwort_hinzufuegen(passwoerter):
    website = input("Gib die Website ein: ").strip()
    benutzername = input("Gib den Benutzernamen ein: ").strip()
    passwort = input("Gib das Passwort ein: ").strip()
    if not website or not benutzername or not passwort:
        print("Alle Felder müssen ausgefüllt werden.")
        return
    passwoerter[website] = {"benutzername": benutzername, "passwort": passwort}
    speichern(passwoerter)
    print(f"Passwort für {website} hinzugefügt.")  

def passwort_loeschen(passwoerter):
    website = input("Gib die Website ein, dessen Passwort du löschen möchtest: ").strip()
    if website in passwoerter:
        bestaetigt = input(f"Passwort für {website} wirklich löschen? (j/n): ").lower()
        if bestaetigt == 'j':
            del passwoerter[website]
            speichern(passwoerter)
            print(f"Passwort für {website} gelöscht.")
        else:
            print("Löschen abgebrochen.")
    else:
        print(f"Keine Passwörter für {website} gefunden.")  

laden()  
speichern(laden())
aktualisieren(laden())
passwort_hinzufuegen(laden())
passwort_loeschen(laden())               
