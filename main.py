import pygame
import init
from color import color
from drawer import drawer

while init.running:
    init.timer.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            init.running = False
    drawer(color['red'], 50)
    drawer(color['orange'], 110)
    drawer(color['yellow'], 170)
    drawer(color['green'], 230)
    drawer(color['blue'], 290)
    drawer(color['purple'], 290)
    pygame.display.flip()

pygame.quit()
