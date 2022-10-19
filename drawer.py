import pygame

# Here to create the screen
screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption('Bolivern')


def drawer(color_choice, y_coord):
    pygame.draw.circle(screen, color_choice, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color_choice, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, (0, 0, 0), [75, y_coord - 10, 190, 20])
