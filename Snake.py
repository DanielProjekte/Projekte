import pygame
import random
from tkinter import messagebox

#Fenster erstellen
pygame.init()
fenster = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")


#Bewegung steuern
clock = pygame.time.Clock()
block_size = 20
schlange = [(100, 100), (80, 100), (60, 100)]
richtung = (block_size, 0) # Bewegt sich nach rechts
essen_position = (200, 200)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                neue_richtung = (0, -block_size)
                if neue_richtung[1] != -richtung[1]:  
                    richtung = neue_richtung
            elif event.key == pygame.K_DOWN:
                neue_richtung = (0, block_size)
                if neue_richtung[1] != -richtung[1]:  
                    richtung = neue_richtung
            elif event.key == pygame.K_LEFT:
                neue_richtung = (-block_size, 0)
                if neue_richtung[0] != -richtung[0]:  
                    richtung = neue_richtung
            elif event.key == pygame.K_RIGHT:
                neue_richtung = (block_size, 0)
                if neue_richtung[0] != -richtung[0]:  
                    richtung = neue_richtung       
    neuer_kopf = (schlange[0][0] + richtung[0], schlange[0][1] + richtung[1])
    schlange = [neuer_kopf] + schlange[:-1]

    fenster.fill((0, 0, 0))
    clock.tick(10)
    
    #Essen zeichnen und Schlange wächst
    pygame.draw.rect(fenster, (255, 0, 0), (essen_position[0], essen_position[1], block_size, block_size))
    if schlange[0] == essen_position:
        schlange.append(schlange[-1])  # Schlange wächst
        essen_position = (random.randint(0, 29) * block_size, random.randint(0, 29) * block_size)  # Neues Essen an zufälliger Position

    #Kollision mit sich selbst oder den Wänden
    if (schlange[0] in schlange[1:] or 
        schlange[0][0] < 0 or schlange[0][0] >= 600 or 
        schlange[0][1] < 0 or schlange[0][1] >= 600):
        messagebox.showinfo("Game Over", f"Du hast verloren! Deine Punktzahl: {len(schlange) - 3}")
        pygame.quit()
        break
    
    
    #Schlange zeichnen
    for block in schlange:
        pygame.draw.rect(fenster, (0, 255, 0), (block[0], block[1], block_size, block_size))
    pygame.display.update()
