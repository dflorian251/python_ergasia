from tkinter import CENTER
from turtle import back
import pygame

WIDTH,HEIGHT = 500,700 #platos kai ypsos efarmoghs 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def display_screen(teleytaio_pshfio,doihkhsh_is_active,python_is_active):
    if input:
        if doihkhsh_is_active:
            if teleytaio_pshfio=='1' or teleytaio_pshfio=='3':
                image = pygame.image.load("assets/wrologia_programmata/doihkhsh_epixeirhsewn/dioikhsh_monos(1,3).jpg")  
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
            elif teleytaio_pshfio=='5' or teleytaio_pshfio=='7' or teleytaio_pshfio=='9':
                image = pygame.image.load("assets/wrologia_programmata/doihkhsh_epixeirhsewn/dioikhsh_monos(5,7,9).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
            elif teleytaio_pshfio=='0' or teleytaio_pshfio=='2' or teleytaio_pshfio=='4':
                image = pygame.image.load("assets/wrologia_programmata/doihkhsh_epixeirhsewn/dioikhsh_zygos(0,2,4).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
            elif teleytaio_pshfio=='6'or teleytaio_pshfio=='8':
                image = pygame.image.load("assets/wrologia_programmata/doihkhsh_epixeirhsewn/dioikhsh_zygos(0,2,4).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
        elif python_is_active:
            if teleytaio_pshfio=='1' or teleytaio_pshfio=='3':
                image = pygame.image.load("assets/wrologia_programmata/python/python_monos(1,3).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
            elif teleytaio_pshfio=='5' or teleytaio_pshfio=='7' or teleytaio_pshfio=='9':
                image = pygame.image.load("assets/wrologia_programmata/python/python_monos(5,7,9).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
            elif teleytaio_pshfio=='0' or teleytaio_pshfio=='2' or teleytaio_pshfio=='4':
                image = pygame.image.load("assets/wrologia_programmata/python/python_zygos(0,2,4).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
            elif teleytaio_pshfio=='6' or teleytaio_pshfio=='8':
                image = pygame.image.load("assets/wrologia_programmata/python/python_zygos(6,8).jpg")
                background = pygame.transform.scale(image,(500,656))
                screen.blit(background,(0,0))
    else :
        background = pygame.image.load("assets/final_background.jpg")
        screen.blit(background,(0,0))
        screen.blit(button_dioikhshs,(150,325))
        screen.blit(button_python,(250,325))
        #text input box
        pygame.draw.rect(screen,color,input_rect,2)
        text_surface = base_font.render(user_text,True,(color))
        screen.blit(text_surface,(input_rect.x+7,input_rect.y+7))
        #button dioikhshs epixeirisewn 
        if doihkhsh_is_active:
            pygame.draw.rect(screen,GREEN,bDioikhshs_rect,1)
        else :
            pygame.draw.rect(screen,BLACK,bDioikhshs_rect,1)
        #button efarmosmenou programmatismou me python
        if python_is_active:
            pygame.draw.rect(screen,GREEN,bPython_rect,1)
        else :
            pygame.draw.rect(screen,BLACK,bPython_rect,1)



#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED = (255,0,0)
color = BLACK

#Images
button_dioikhshs = pygame.image.load("assets/button_dioikhshs.jpg")
button_python = pygame.image.load("assets/button_python.jpg")

#Text
base_font = pygame.font.Font(None,40)
user_text = " "

#Buttons
bDioikhshs_rect = button_dioikhshs.get_rect(topleft=[149,325])
bPython_rect = button_python.get_rect(topleft=[251,325])

#Dhmiourgia surface kai rectangle tou pediou pou tha plhktrologitai o AM tou foithth
input_surface = pygame.Surface([200,40])
input_rect = input_surface.get_rect(center=[250,300])


doihkhsh_is_active=False
python_is_active=False
input = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if bPython_rect.collidepoint(event.pos):
                python_is_active=True
            if bDioikhshs_rect.collidepoint(event.pos):
                doihkhsh_is_active=True

        if event.type == pygame.KEYDOWN:
            if len(user_text)>=11:
                color = RED
            else :
                color = BLACK
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[-1]
            elif event.key == pygame.K_RETURN :
                input = True
            else :
                user_text += event.unicode 
    

    display_screen(user_text[-1],doihkhsh_is_active,python_is_active)
    pygame.display.flip()


pygame.quit()

#Melh omadas
#Frorian Dima: inf2021044
#Konstantinos Lygkouris: inf2021124
#Giorgos Tsanikidhs: inf2021232