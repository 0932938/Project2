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

#images
carImg = pygame.image.load('racecar.png')
dobbelNiks = pygame.image.load('DObelsteen niks.png')
dobbelImg1 = pygame.image.load('DObelsteen 1.png')
dobbelImg2 = pygame.image.load('DObelsteen 2.png')
dobbelImg3 = pygame.image.load('DObelsteen 3.png')
dobbelImg4 = pygame.image.load('DObelsteen 4.png')
dobbelImg5 = pygame.image.load('DObelsteen 5.png')
dobbelImg6 = pygame.image.load('DObelsteen 6.png')

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


def vragenoproep():
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

###definitions

def updatetime():
    pygame.display.update()
    pygame.time.delay(1000)

#dobbelsteen
def dobbelsteen(x,y):
    gameDisplay.blit(dobbelNiks,(x,y))
def dobbel1(x,y):
    gameDisplay.blit(dobbelImg1,(x,y))
    aantal_ogen = 1
def dobbel2(x,y):
    gameDisplay.blit(dobbelImg2,(x,y))
    aantal_ogen = 2
def dobbel3(x,y):
    gameDisplay.blit(dobbelImg3,(x,y))
    aantal_ogen = 3
def dobbel4(x,y):
    gameDisplay.blit(dobbelImg4,(x,y))
    aantal_ogen = 4
def dobbel5(x,y):
    gameDisplay.blit(dobbelImg5,(x,y))
    aantal_ogen = 5
def dobbel6(x,y):
    gameDisplay.blit(dobbelImg6,(x,y))
    aantal_ogen = 6

#begin
def beginroll():

#    werp = 0
#    while werp < 5:
#        a = 0
#        randnummer = 0
#        def nummer():
#            randnummer = random.randint(1, 6)
#            if randnummer == a:
#                randnummer += 1
#                while randnummer > 6:
#                    nummer()
#            werp += 1
#        button("Werp",480,620,100,50,bright_red,  light_red, nummer)
#        a = randnummer
#        print (a)

    randnummer1 = random.randint(1, 100)
    check_nummer = randnummer1
    randnummer2 = random.randint(1, 100)
    while randnummer2 == check_nummer:
        randnummer1 = random.randint(1,100)
        randnummer2 = random.randint(1,100)
        check_nummer = randnummer1
    if randnummer2 > check_nummer:
        check_nummer = randnummer2
    randnummer3 = random.randint(1, 100)
    while randnummer3 == check_nummer:
        randnummer2 = random.randint(1,100)
        randnummer3 = random.randint(1,100)
        check_nummer = randnummer2
    if randnummer3 > check_nummer:
        check_nummer = randnummer3
    randnummer4 = random.randint(1, 100)
    while randnummer4 == check_nummer:
        randnummer3 = random.randint(1,100)
        randnummer4 = random.randint(1,100)
        check_nummer = randnummer3
    if randnummer4 > check_nummer:
        check_nummer = randnummer4
    print(check_nummer)


def vragen():
    vraag = random.choice (vragenlijst)
    print(vraag)
    vragenlijst.remove(vraag)
    

#verplaatsing richting
def steen():
    time = 0
    while time < 3:
        dobbelsteen(50,50)
        updatetime()
        time+=1
    nummer = random.randint(1, 10)
    if nummer <= 5:
        while time < 7:
            dobbel1(50,50)
            updatetime()
            time+=1
    elif nummer <= 8:
        while time < 7:
            dobbel2(50,50)
            updatetime()
    elif nummer >= 9:
        while time < 7:
            dobbel3(50,50)
            updatetime()
            time+=1

def go_left():
    direction = "left"
    steen()
def go_up():
    direction = "up"
    steen()
def go_right():
    direction = "right" 
    steen()

def lopen():
    button("Left",  480,620,100,50,bright_red,  light_red, go_left)
    button("Up",    590,620,100,50,light_red,   red,       go_up)
    button("Right", 700,620,100,50,bright_red,  light_red, go_right)

def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                quitgame()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont(None, 115)
        pygame.display.update()
        clock.tick(15)
        

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
      

        x += x_change
        gameDisplay.fill(white)

        vragenoproep()
        lopen()
        car(500,300)
 
        pygame.display.update()
        clock.tick(60)

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
game_loop()
pygame.quit()
quit()