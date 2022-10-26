import pygame
from color import color

# Here to create the screen
screen = pygame.display.set_mode((300, 450))
background = pygame.image.load("bg.jpg")
pygame.display.set_caption('Bolivern')
font = pygame.font.Font('freesansbold.ttf', 14)


def drawer(color_choice, y_coord):
    task = pygame.draw.circle(screen, color_choice, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color_choice, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, (0, 0, 0), [75, y_coord - 10, 190, 20])
    return task

def cleaner(y):
    pygame.draw.circle(screen, color['black'], (30, y), 15,20)


def value_drawer(y, value):
    value_text = font.render(str(value), True, color["white"])
    screen.blit(value_text, (18, y))

def hearth():
    image = pygame.image.load("coeur.png").convert()
    return image