import pygame, pygame.mixer ,sys, math, time, random

pygame.init()
black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
d_red = (139,0,0)
gold = (255, 215,0)
green = (0,128,0)
d_blue = (30, 114, 225)
 
width = 1280
height = 720
size = (width,height)
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
 
gameDisplay = pygame.display.set_mode((size))
pygame.display.set_caption('Beklim de Euromast')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, d_red)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()   
                  
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        


    smallText = pygame.font.SysFont("Arial black",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    


def quitgame():
    pygame.quit()
    quit()


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        bg = pygame.image.load("euromast_wallpaper_v2.jpg")   
        gameDisplay.fill(white)
        gameDisplay.blit(bg, (0, 0)) 
        largeText = pygame.font.SysFont("comicsansms",115)

        button("Play",1050,150,150,50,black,(80,80,80),None)
        button("Intructie",1050,250,150,50,black,(80,80,80),instructies)
        button("High Score",1050,350,150,50,black,(80,80,80),None)
        button("Option",1050,450,150,50,black,(80,80,80),None)
        button("Quit",1050,550,150,50,black,(80,80,80),quitgame)

        pygame.display.update()
        clock.tick(15)


def instructies():
    pygame.display.set_caption("Instruction Screen")
    done = False
    display_instructions = True
    instruction_page = 1

    # LOOP INSTRUCTIEPAGINA
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                instruction_page += 1
                if instruction_page == 4:
                    instruction_page = 1
            elif key[pygame.K_LEFT]:
                instruction_page -= 1
                if instruction_page == 0:
                    instruction_page = 3

        # Set the screen background
        gameDisplay.fill(black)

        if instruction_page == 1:
            # Draw instructions, page 1
            instruc1 = pygame.image.load("instructiepagina1.jpg")
            instruc1 = pygame.transform.scale(instruc1, (size))
            gameDisplay.blit(instruc1,(0,0))

        if instruction_page == 2:
            # Draw instructions, page 1
            instruc2 = pygame.image.load("instructiepagina2.jpg")
            instruc2 = pygame.transform.scale(instruc2, (size)) 
            gameDisplay.blit(instruc2,(0,0))

        if instruction_page == 3:
            # Draw instructions, page 1
            instruc3 = pygame.image.load("instructiepagina3.jpg")
            instruc3 = pygame.transform.scale(instruc3, (size))
            gameDisplay.blit(instruc3,(0,0))

        button("<",940,40,50,50,black,(80,80,80),None)
        button(">",1170,40,50,50,black,(80,80,80),None)
        button("Back To menu",1000,40,160,50,black,(80,80,80),game_intro)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


game_intro()
pygame.quit()
quit()