import pygame
import time
import random
from array import array
    
pygame.init()
 
###global variable

#colores
display_width = 1280
display_height = 720
 
black = (0,0,0)
white = (255,255,255)

red = (150,0,0)
light_red = (200,0,0)
bright_red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

#Dit zijn alle afbeeldingen van de vragen
#sportvraag afbeeldingen
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

# historyvragen afbeeldingen
hv1 = pygame.image.load('historyvragen 1.jpg')
hv2 = pygame.image.load('historyvragen 2.jpg')
hv3 = pygame.image.load('historyvragen 3.jpg')
hv4 = pygame.image.load('historyvragen 4.jpg')
hv5 = pygame.image.load('historyvragen 5.jpg')
hv6 = pygame.image.load('historyvragen 6.jpg')
hv7 = pygame.image.load('historyvragen 7.jpg')
hv8 = pygame.image.load('historyvragen 8.jpg')
hv9 = pygame.image.load('historyvragen 9.jpg')
hv10 = pygame.image.load('historyvragen 10.jpg')
hv11 = pygame.image.load('historyvragen 11.jpg')
hv12 = pygame.image.load('historyvragen 12.jpg')
hv13 = pygame.image.load('historyvragen 13.jpg')
hv14 = pygame.image.load('historyvragen 14.jpg')
hv15 = pygame.image.load('historyvragen 15.jpg')

# entertainmentvragen afbeeldingen
ev1 = pygame.image.load('entertainmentvragen 1.jpg')
ev2 = pygame.image.load('entertainmentvragen 2.jpg')
ev3 = pygame.image.load('entertainmentvragen 3.jpg')
ev4 = pygame.image.load('entertainmentvragen 4.jpg')
ev5 = pygame.image.load('entertainmentvragen 5.jpg')
ev6 = pygame.image.load('entertainmentvragen 6.jpg')
ev7 = pygame.image.load('entertainmentvragen 7.jpg')
ev8 = pygame.image.load('entertainmentvragen 8.jpg')
ev9 = pygame.image.load('entertainmentvragen 9.jpg')
ev10 = pygame.image.load('entertainmentvragen 10.jpg')
ev11 = pygame.image.load('entertainmentvragen 11.jpg')
ev12 = pygame.image.load('entertainmentvragen 12.jpg')
ev13 = pygame.image.load('entertainmentvragen 13.jpg')
ev14 = pygame.image.load('entertainmentvragen 14.jpg')
ev15 = pygame.image.load('entertainmentvragen 15.jpg')

# technologievragen afbeeldingen
tv1 = pygame.image.load('technologievragen 1.jpg')
tv2 = pygame.image.load('technologievragen 2.jpg')
tv3 = pygame.image.load('technologievragen 3.jpg')
tv4 = pygame.image.load('technologievragen 4.jpg')
tv5 = pygame.image.load('technologievragen 5.jpg')
tv6 = pygame.image.load('technologievragen 6.jpg')
tv7 = pygame.image.load('technologievragen 7.jpg')
tv8 = pygame.image.load('technologievragen 8.jpg')
tv9 = pygame.image.load('technologievragen 9.jpg')
tv10 = pygame.image.load('technologievragen 10.jpg')
tv11 = pygame.image.load('technologievragen 11.jpg')
tv12 = pygame.image.load('technologievragen 12.jpg')
tv13 = pygame.image.load('technologievragen 13.jpg')
tv14 = pygame.image.load('technologievragen 14.jpg')
tv15 = pygame.image.load('technologievragen 15.jpg')

#Een class met de attributen voor vragen
# categorie zodat ik later kan zeggen - if categorie = blabla dan vragen uit die lijst
# vraagafbeelding omdat ik die wil laten zien aan de speler
# antwoord omdat elke vraag een antwoord heeft, die gecheckt moet worden.
# (if user input = antwoord dan correct oid)
# soortvraag omdat de speler moet dobbelen voor open/meerkeuze.
# if dobbel =< 6 dan keuze, anders open

class vragen:
    def __init__(self, categorie, vraagafbeelding, antwoord, soortvraag):
        self.Categorie = categorie
        self.vraag = vraagafbeelding
        self.Antwoord = antwoord
        self.Soortvraag = soortvraag

#vanaf hier komen de vragen met al hun attributen te staan als global variable
#sportvragen
s1 = vragen("sportvragen", sv1,"A", "keuze")
s2 = vragen("sportvragen", sv2,"A","keuze")
s3 = vragen("sportvragen", sv3,"B", "keuze")
s4 = vragen("sportvragen", sv4,"B", "keuze")
s5 = vragen("sportvragen", sv5,"A", "keuze")
s6 = vragen("sportvragen", sv6, "C", "keuze")
s7 = vragen("sportvragen", sv7,"B", "keuze")
s8 = vragen("sportvragen", sv8,"C", "keuze")
s9 = vragen("sportvragen", sv9,"A", "keuze")
s10 = vragen("sportvragen", sv10,"C", "keuze")
s11 = vragen("sportvragen", sv11,"DE KUIP", "open")
s12 = vragen("sportvragen", sv12,"DUNKEN", "open")
s13 = vragen("sportvragen", sv13,"CITY RACE ROTTERDAM", "open")
s14 = vragen("sportvragen", sv14,"B", "keuze")
s15 = vragen("sportvragen", sv15,"FEYENOORD", "open")

#historyvragen
h1 = vragen("historyvragen", hv1, "B", "keuze")
h2 = vragen("historyvragen", hv2, "A", "keuze")
h3 = vragen("historyvragen", hv3, "B", "keuze")
h4 = vragen("historyvragen", hv4, "C", "keuze")
h5 = vragen("historyvragen", hv5, "B", "keuze")
h6 = vragen("historyvragen", hv6, "C", "keuze")
h7 = vragen("historyvragen", hv7, "A", "keuze")
h8 = vragen("historyvragen", hv8, "B", "keuze")
h9 = vragen("historyvragen", hv9, "A", "keuze")
h10 = vragen("historyvragen", hv10, "A", "keuze")
h11 = vragen("historyvragen", hv11, "PIM FORTUYN", "open")
h12 = vragen("historyvragen", hv12, "BOKITO", "open")
h13 = vragen("historyvragen", hv13, "LOODS24", "open")
h14 = vragen("historyvragen", hv14, "C", "keuze")
h15 = vragen("historyvragen", hv15, "MAASVLAKTE", "open")

#entertainmentvragen
e1 = vragen("entertainmentvragen", ev1, "B", "keuze")
e2 = vragen("entertainmentvragen", ev2, "A", "keuze")
e3 = vragen("entertainmentvragen", ev3, "BLIJDORP", "open")
e4 = vragen("entertainmentvragen", ev4, "ERASMUSBRUG", "open")
e5 = vragen("entertainmentvragen", ev5, "AHOY", "open")
e6 = vragen("entertainmentvragen", ev6, "A", "keuze")
e7 = vragen("entertainmentvragen", ev7, "C", "keuze")
e8 = vragen("entertainmentvragen", ev8, "A", "keuze")
e9 = vragen("entertainmentvragen", ev9, "A", "keuze")
e10 = vragen("entertainmentvragen", ev10, "C", "keuze")
e11 = vragen("entertainmentvragen", ev11, "C", "keuze")
e12 = vragen("entertainmentvragen", ev12, "B", "keuze")
e13 = vragen("entertainmentvragen", ev13, "B", "keuze")
e14 = vragen("entertainmentvragen", ev14, "ZOMBIEWALK", "open")
e15 = vragen("entertainmentvragen", ev15, "B", "keuze")

#technologievragen
t1 = vragen("technologievragen", tv1, "POKEMON GO", "open")
t2 = vragen("technologievragen", tv2, "C", "keuze")
t3 = vragen("technologievragen", tv3, "B", "keuze")
t4 = vragen("technologievragen", tv4, "C", "keuze")
t5 = vragen("technologievragen", tv5, "B", "keuze")
t6 = vragen("technologievragen", tv6, "A", "keuze")
t7 = vragen("technologievragen", tv7, "B", "keuze")
t8 = vragen("technologievragen", tv8, "BINAIRE", "open")
t9 = vragen("technologievragen", tv9, "B", "keuze")
t10 = vragen("technologievragen", tv10, "KUBUSWONINGEN", "open")
t11 = vragen("technologievragen", tv11, "B", "keuze")
t12 = vragen("technologievragen", tv12, "A", "keuze")
t13 = vragen("technologievragen", tv13, "A", "keuze")
t14 = vragen("technologievragen", tv14, "B", "keuze")
t15 = vragen("technologievragen", tv15, "KABOUTER BUTTPLUG", "open")


#lijsten aanmaken voor de vragen, om later elementen te kunnen removen
# (je wilt niet 2 keer dezelfde vraag
sportvragen = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15]
historyvragen = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15]
entertainmentvragen = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]
technologievragen = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]


def vragenoproep():
    randomvraag = random.choice(sportvragen)
    gameDisplay.blit(randomvraag.vraag, (200, 200))
    return randomvraag

def vraagbeantwoord():
    sportvragen.remove(randomvraag)

###definitions

Question_given = False

def Give_Question():
    global Question_given
    while Question_given == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Question_given = True

        gameDisplay.fill(white)
        vragenoproep()

        pygame.display.update()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(None, 40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()

#main game 
Give_Question()
pygame.quit()
quit()