import pygame

# Kleuren die we kunnen gebruiken
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Grootte van scherm bepalen
schermresolutie = ((800, 600))
screen = pygame.display.set_mode(schermresolutie)

# Dit bepaald de framerate van onze display
FPS = pygame.time.Clock()

# Grootte van letters bepalen
font = pygame.font.Font(None, 20)

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
                    display_instructions = False
            elif key[pygame.K_LEFT]:
                instruction_page -= 1
                if instruction_page == 0:
                    display_instructions = False

        # Set the screen background
        screen.fill(BLACK)

        if instruction_page == 1:
            # Draw instructions, page 1
            image = pygame.image.load("instructiepagina1.jpg")
            screen.blit(image,(0,0))

        if instruction_page == 2:
            # Draw instructions, page 1
            image = pygame.image.load("instructiepagina2.jpg")
            screen.blit(image,(0,0))

        if instruction_page == 3:
            # Draw instructions, page 1
            image = pygame.image.load("instructiepagina3.jpg")
            screen.blit(image,(0,0))





        # Limit to 60 frames per second
        FPS.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

instructies()
pygame.quit()
