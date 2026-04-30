import tkinter as tk
from tkinter import messagebox
import json
import os

SAVE_FILE = "todos.json"

# Funktion zum Laden und Speichern der To-Do-Liste
def laden():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def speichern():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# Logik der To-Do-Liste

def liste_aktualisieren():
    listbox.delete(0, tk.END)
    for i, aufgabe in enumerate(todos):
        symbol = "✅" if aufgabe["erledigt"] else "⬜"
        listbox.insert(tk.END, f"  {symbol}  {aufgabe['text']}")
        if aufgabe["erledigt"]:
            listbox.itemconfig(i, fg="#888888")

def aufgabe_hinzufuegen(event=None):
    text = eingabe.get().strip()
    if not text:
        return
    todos.append({"text": text, "erledigt": False})
    speichern()
    liste_aktualisieren()
    eingabe.delete(0, tk.END)

def aufgabe_erledigt():
    auswahl = listbox.curselection()
    if not auswahl:
        messagebox.showinfo("Hinweis", "Bitte eine Aufgabe auswählen.")
        return
    i = auswahl[0]
    todos[i]["erledigt"] = not todos[i]["erledigt"]
    speichern()
    liste_aktualisieren()

def aufgabe_loeschen():
    auswahl = listbox.curselection()
    if not auswahl:
        messagebox.showinfo("Hinweis", "Bitte eine Aufgabe auswählen.")
        return
    i = auswahl[0]
    bestaetigt = messagebox.askyesno("Löschen?", f"'{todos[i]['text']}' wirklich löschen?")
    if bestaetigt:
        todos.pop(i)
        speichern()
        liste_aktualisieren()
 
def alle_erledigten_loeschen():
    global todos
    todos = [t for t in todos if not t["erledigt"]]
    speichern()
    liste_aktualisieren()

# GUI erstellen

todos = laden()
 
root = tk.Tk()
root.title("📝 Meine To-do-Liste")
root.geometry("480x520")
root.configure(bg="#f5f5f5")
root.resizable(False, False)
 
# Titel
tk.Label(root, text="Meine To-do-Liste", font=("Helvetica", 18, "bold"),
         bg="#f5f5f5", fg="#333").pack(pady=(20, 10))
 
# Eingabebereich
eingabe_frame = tk.Frame(root, bg="#f5f5f5")
eingabe_frame.pack(padx=20, fill="x")
 
eingabe = tk.Entry(eingabe_frame, font=("Helvetica", 13), bd=2, relief="groove")
eingabe.pack(side="left", fill="x", expand=True, ipady=6)
eingabe.bind("<Return>", aufgabe_hinzufuegen)
 
tk.Button(eingabe_frame, text="➕ Hinzufügen", font=("Helvetica", 11),
          bg="#4CAF50", fg="white", bd=0, padx=10,
          command=aufgabe_hinzufuegen).pack(side="left", padx=(8, 0))
 
# Listbox
list_frame = tk.Frame(root, bg="#f5f5f5")
list_frame.pack(padx=20, pady=15, fill="both", expand=True)
 
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
 
listbox = tk.Listbox(list_frame, font=("Helvetica", 12), bd=2, relief="groove",
                     selectbackground="#d0e8ff", activestyle="none",
                     yscrollcommand=scrollbar.set, height=12)
listbox.pack(fill="both", expand=True)
scrollbar.config(command=listbox.yview)
 
# Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=5)
 
tk.Button(btn_frame, text="✅ Erledigt", width=14, font=("Helvetica", 11),
          bg="#2196F3", fg="white", bd=0, pady=6,
          command=aufgabe_erledigt).grid(row=0, column=0, padx=6)
 
tk.Button(btn_frame, text="🗑️ Löschen", width=14, font=("Helvetica", 11),
          bg="#f44336", fg="white", bd=0, pady=6,
          command=aufgabe_loeschen).grid(row=0, column=1, padx=6)
 
tk.Button(btn_frame, text="🧹 Erledigte löschen", width=18, font=("Helvetica", 11),
          bg="#FF9800", fg="white", bd=0, pady=6,
          command=alle_erledigten_loeschen).grid(row=1, column=0, columnspan=2, pady=(10, 0))
 
# Status-Label
status = tk.Label(root, text="💡 Tipp: Enter drücken zum schnellen Hinzufügen",
                  font=("Helvetica", 9), bg="#f5f5f5", fg="#999")
status.pack(pady=(8, 0))
 
liste_aktualisieren()
root.mainloop()