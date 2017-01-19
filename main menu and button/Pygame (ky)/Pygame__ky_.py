import pygame, sys, time, random, math
from button_N_color import text_n_button, getFont
 
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

#screen 
width = 1280
height = 720
screen_size = (width, height)




#background menu
class Euromast_game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Beklim de Euromast")
    
    def quitGame(self):
        pygame.quit()
        quit()

    def Mainmenu(self): 
        rect = self.screen.get_rect()
            
        def startgame():
            self.menu = False

        playButton = text_n_button((rect.centerx, rect.centery -225), (200, 80), d_red, "Play", None)
        IntrucButton = text_n_button((rect.centerx, rect.centery -150), (200, 80), d_red, "Intructie", None)
        HiScoreButton = text_n_button((rect.centerx, rect.centery -75), (200, 80), d_red, "Highscore", None)
        Option = text_n_button((rect.centerx, rect.centery), (200, 80), d_red, "Option", None)
        quitButton = text_n_button((rect.centerx, rect.centery +75), (200, 80), d_red, "Quit", self.quitGame)

        self.menu = True
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = False
                
                menubg = pygame.image.load("euromast_wallpaper_v1.png") 
                self.screen.fill(white)
                self.screen.blit(menubg (0, 0))
       
                text = getFont(size=82, style="bold").render("Beklim de Euromast", True, black)
                textRect = text.get_rect()
                textRect.center = self.screen.get_rect().center
                textRect.y -= 200
                self.screen.blit(text, textRect)

                quitbutton.update(self.screen)
                pygame.display.update()

    def pause(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print("game unpaused")
                        pause = False

                text = utils.getFont(size=96, style="bold").render("Paused", True, utils.black)
                textRect = text.get_rect()
                textRect.center = self.gw.get_rect().center

                self.gw.blit(text, textRect)

                pygame.display.update()
                self.clock.tick(self.FPS)

    def playGame(self):
        self.gotoMenu()

        gameActive = True
        while gameActive:                                                  #Game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print("game Paused")
                        self.pause()

    
        self.gotoMenu()

game = Euromast_game()
game.playGame