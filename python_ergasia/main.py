from tkinter import CENTER
import pygame

WIDTH,HEIGHT = 500,700 #platos kai ypsos efarmoghs 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)

#Images
background = pygame.image.load("assets/final_background.jpg")

#Text
base_font = pygame.font.Font(None,30)
user_text = ""

#Dhmiourgia surface kai rectangle tou pediou pou tha plhktrologitai o AM tou foithth
input_surface = pygame.Surface([200,40])
input_rect = input_surface.get_rect(center=[250,300])


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEBUTTONDOWN:#elexgos an to event einai klik tou MOUSE mas,dhladh an pathsame ta deksi button tou MOUSE mas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else :
                user_text +=event.unicode    

    screen.blit(background,(0,0))
    pygame.draw.rect(screen,BLACK,input_rect,2)
    text_surface = base_font.render(user_text,True,(BLACK))
    screen.blit(text_surface,(input_rect.x+10,input_rect.y+10))
    #pygame.display.update()
    pygame.display.flip()

pygame.quit()
