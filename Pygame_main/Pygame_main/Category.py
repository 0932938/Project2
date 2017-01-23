import pygame
import time
import random
    
pygame.init()
width = 1280
height = 720
size = (width,height)
FIRST_DICE = 0
black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
d_red = (139,0,0)
yellow = (227,207,87)
gold = (255, 215,0)
green = (0,128,0)
d_blue = (30, 114, 225)

pygame.display.set_caption("Dice Roller (with images!)")
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
already_rolled = False
Catergory_selected = False 
bg = pygame.image.load("bb.jpg")
cpup = pygame.image.load("Blanco_Frame.png")  
Csound = pygame.mixer.Sound("moving cursor.wav")
Open_vraag = pygame.image.load('Openvraag.png')
Meerkeu_vraag = pygame.image.load('Meerkeuze.png')

def Qanimation():
    global Open_vraag, Meerkeu_vraag
    screen.blit(Open_vraag,(0,0))


#text for button
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

# text on display(large text) 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
#buttons 
def button(msg,x,y,w,h,ic,ac,action=None):
    global Csound
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            Csound.play()
            pygame.time.delay(1000)
            action()       
            pygame.mixer.stop()       
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("Arial black",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def roll_a_dice():
    typeQ = ["open"] * 20 + ["meerkeuze"] * 80
    result = random.choice(typeQ)
    return result

# determines which first dice is used
def display_first(first):

    if (first == "open"):
        screen.blit(Open_vraag,(0,0))
        pygame.display.flip()
        produce_button_message("Klik Doorgaan", 575,250)
        produce_button_message2("Type vraag", 615,152) 
        button("Doorgaan", 423,520,458,32,yellow,gold, Select_Catagory)
    elif (first == "meerkeuze"):
        screen.blit(Meerkeu_vraag,(0,0))
        pygame.display.flip()
        produce_button_message("Klik Doorgaan", 575,250)
        produce_button_message2("Type vraag", 615,152) 
        button("Doorgaan", 423,520,458,32,yellow,gold, Select_Catagory)
        
       
# tells the user how to roll
def produce_button_message(text, x, y):
    our_font = pygame.font.SysFont("Arial black", 20)
    #render the text now
    produce_text = our_font.render(text, 1, black)
    screen.blit(produce_text, (x, y))

def produce_button_message2(text, x, y):
    our_font = pygame.font.SysFont("Arial black", 15)
    #render the text now
    produce_text = our_font.render(text, 1, black)
    screen.blit(produce_text, (x, y))

# our roll will display message with our roll converted to text form, alongside
def before_roll():
    blank_popup = pygame.image.load('empty_popup.png')
    screen.blit(blank_popup,(0,0))
    produce_button_message("Druk op 'Rol' om te dobbelen", 505,280)
    produce_button_message2("Type vraag", 615,152)
    button("roll", 372,357,560,83,(139,131,134),(75,75,75), rollfunc)

def our_roll():
     #Completed roll Message. Cast int to str to output the message clearly
     text = "Je hebt " + str(FIRST_DICE) + " gegooid."
     print(text)
     produce_roll_message(text, 200, 200)
        
def rollfunc(): 
    global FIRST_DICE, already_rolled
    FIRST_DICE = roll_a_dice()
    roll_occur = True
    
    
# We don't want our roll value output before the first roll occurs.
def typeQroll():
    global already_rolled
    roll_occur = False
    while already_rolled == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                already_rolled = True

        screen.fill(white)
        screen.blit(bg, (0, 0)) 
        before_roll()
        display_first(FIRST_DICE)
        pygame.display.flip()
        # If the roll is requested, our_roll will execute.
 

def Select_Catagory():
    global Catergory_selected
    while Catergory_selected == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Catergory_selected = True
        screen.blit(cpup, (0 ,0))
        produce_button_message("Kies een categorie", 555,250)
        produce_button_message2("Categorie", 620,152)  
        button("Entertainment", 402,300,180,70,yellow,gold, None)
        button("Geschiedenis", 730, 300,180,70,d_blue,blue, None)
        button("Sport", 730,390,180,70,green,lime, None)
        button("Techologie", 402,390,180,70,d_red,red, None)
        pygame.display.flip()

        
# Once the loop exits, the program will quit.
# Loop will exit when the 'Exit' button on the window is clicked.This bit of code just ensures you can actually
# click that and exit.
typeQroll()
pygame.quit()
quit()


