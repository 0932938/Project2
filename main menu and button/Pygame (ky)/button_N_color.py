import pygame, sys, time, random, math

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

reaction = None

def getFont(name = "Arial", size = 20, style = ''): 
    return pygame.font.SysFont(name, size, style)

class click: 
    def __init__(self, pos, size):
        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = position
        self.clicked = False

    def mouse_moveover(self):
        cursor = pygame.mouse.get_pos()

        if self.rect.left < cursor[0] < self.rect.right and self.rect.top < cursor[1] < self.rect.bottum:
            return True
        else:
            return False

    def mouse_notmoveover(self):
        pass

    def leftmouse(self):
        return self.clicked

    def leftmouseclicked(self):
        pass
    
    def clicking(self):
        global interact
        mouse = pygame.mouse.get_pressed()
        
        if self.mouse_moveover():
            if mouse[0] and self.clicked == False and not reaction:
                self.clicked = True
                reaction = self 
                return True
        if mouse[0] == False and self.clicked == True:
            self.clicked = False
            reaction = none
        return False

    def click_release(self):
        print("Test message: if you get this message when you released the button then the button works") 

    def update(self, screen):
        if self.mouse_moveover():
            self.mouse_notmoveover()

        if self.leftmouse():
            self.click_release()

class button(click):
    def __init__(self, pos, size, color, action):
        click.__init__(self, pos, size)

        self.color = color 
        self.image = pygame.Surface(size) 
        self.image.set_alpha(128)
        self.image.fill(self.color)
        self.action = action
        
    def mouse_notmoveover(self):
        overlay = pygame.Surface(selff.rect.size)
        overlay.set_alpha(50)
        overlay.fill(black)
        self.image.blit(overlay, (0, 0))

    def click_release(self):
        self.action()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        self.image.fill(self, screen)

        click.update(self, screen)

        self.draw(screen)

class text_n_button(button):
    def __init__(self, pos, size, color, text, action):
        button.__init__(self, pos, size, color, action)

        self.fontsize = self.rect.h
        self.text = getFont(size=self.fontsize, style='bold').render(text, True, black)
        self.textRect = self.text.get_rect()

    def draw(self, screen):
        self.image.blit(self.text, ((self.rect.w - self.textRect.w)/2, (self.rect.h - self.textRect.h)/2))
        button.draw(self, screen)