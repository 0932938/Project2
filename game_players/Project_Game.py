import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.init()
scherm = pygame.display.set_mode((800, 500))
pygame.display.set_caption('climb the EUROMAST!')
bg = pygame.image.load("bb.jpg")
bg = pygame.transform.scale(bg, (800,510))

class Player:
    def player(self,player,pos_x, pos_y, health, width, height ):
        self.player = player
        self.pos_x = pos_x
        #self.category = ("Sport", "Geschiedenis", "Entertainment", "Geografie")
        self.pos_y = pos_y
        self.health = 1
        self.width = width
        self.height = height

    def update(self,player):
        self.health += 1

    def object(self, scherm):
        pygame.draw.rect(scherm, black, [self.pos_x, self.pos_y, self.width, self.height])


pygame.draw.rect(scherm, black, [200, 100, 10, 10])


pos_y = 100
pos_x = 200
run_program = True
while run_program:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x -= 21
            if event.key == pygame.K_UP:
                pos_y -= 15
            if event.key == pygame.K_RIGHT:
                pos_x += 20

    scherm.blit(bg, (0,0))
    pygame.display.update()
pygame.quit()
quit()


