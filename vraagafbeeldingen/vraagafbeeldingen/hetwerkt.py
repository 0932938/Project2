import random
import pygame

sv1 = pygame.image.load('sportvragen 1.jpg')
sv2 = pygame.image.load('sportvragen 2.jpg')
sv3 = pygame.image.load('sportvragen 3.jpg')
sv4 = pygame.image.load('sportvragen 4.jpg')
sv5 = pygame.image.load('sportvragen 5.jpg')
sv6 = pygame.image.load('sportvragen 6.jpg')
sv7 = pygame.image.load('sportvragen 7.jpg')
sv8 = pygame.image.load('sportvragen 8.jpg')
sv9 = pygame.image.load('sportvragen 9.jpg')
sv10 = pygame.image.load('sportvragen 10.jpg')
sv11 = pygame.image.load('sportvragen 11.jpg')
sv12 = pygame.image.load('sportvragen 12.jpg')
sv13 = pygame.image.load('sportvragen 13.jpg')
sv14 = pygame.image.load('sportvragen 14.jpg')
sv15 = pygame.image.load('sportvragen 15.jpg')


class vragen:
    def __init__(self, categorie, vraagafbeelding, antwoord, soortvraag):
        self.Categorie = categorie
        self.vraag = vraagafbeelding
        self.Antwoord = antwoord
        self.Soortvraag = soortvraag

#vanaf hier komen de vragen met al hun attributen te staan als global variable
#sportvragen
a1 = vragen("sportvragen", sv1,"180", "open")
a2 = vragen("sportvragen","Hoe lang is Jawed","164","open")

#historyvragen
#b1 = vragen("Welk jaar werd Rotterdam gebombardeerd door de Duitsers?", "1940")
#b2 = vragen("Hoe heet de oudste tunnel van Rotterdam?", "Maastunnel")

#entertainmentvragen



#Hier maak ik duidelijk welke vragen/ variables er tot de categorie sportvragen behoren
sportvragen = [a1, a2]
#historyvragen = [b1, b2]
#entertainmentvragen = [c1]

randomvraag = random.choice(sportvragen)
print(randomvraag.Antwoord)


#print(str(c1.vraag))
#userinput = str(input("Zet hier je input \n"))
#if userinput == c1.Antwoord:
#    print("correct")
#else:
#    print("incorrect")

