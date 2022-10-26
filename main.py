import pygame
import init
from color import color
from drawer import drawer, value_drawer, screen, cleaner, hearth, font, background
import amourette
import math


def printer():
    screen.blit(background, (0, 0))
    regard = drawer(color['red'], 50)
    caresse = drawer(color['orange'], 110)
    bisous = drawer(color['yellow'], 170)
    fete = drawer(color['green'], 230)
    sexe = drawer(color['blue'], 290)
    bonheur = drawer(color['purple'], 350)
    value_drawer(43, amourette.amour['regard'])
    value_drawer(103, amourette.amour['caresse'])
    value_drawer(163, amourette.amour['bisous'])
    value_drawer(223, amourette.amour['fete'])
    value_drawer(283, amourette.amour['sexe'])
    value_drawer(343, amourette.amour['bonheur'])
    screen.blit(font.render('REGARD', True, color["white"]), (100, 43))
    screen.blit(font.render('10', True, color["white"]), (200, 43))
    screen.blit(font.render('CARESSE', True, color["white"]), (100, 103))
    screen.blit(font.render('100', True, color["white"]), (200, 103))
    screen.blit(font.render('BISOUS', True, color["white"]), (100, 163))
    screen.blit(font.render('1000', True, color["white"]), (200, 163))
    screen.blit(font.render('FETE', True, color["white"]), (100, 223))
    screen.blit(font.render('10000', True, color["white"]), (200, 223))
    screen.blit(font.render('SEXE', True, color["white"]), (100, 283))
    screen.blit(font.render('100000', True, color["white"]), (200, 283))
    screen.blit(font.render('BONHEUR', True, color["white"]), (100, 343))
    screen.blit(font.render('1000000', True, color["white"]), (200, 343))
    return regard, caresse, bisous, fete, sexe, bonheur


def boucle():
    while init.running:
        init.timer.tick(60)
        regard, caresse, bisous, fete, sexe, bonheur = printer()
        coeur = screen.blit(hearth(), (114, 370))
        screen.blit(font.render(str(math.floor(amourette.coeur)), True, color["white"]), (132, 393))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                init.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if coeur.collidepoint(event.pos):
                    amourette.coeur += 1
                if regard.collidepoint(event.pos) and amourette.coeur >= 10:
                    cleaner(50)
                    amourette.coeur -= 10
                    amourette.amour['regard'] += 1
                if caresse.collidepoint(event.pos) and amourette.coeur >= 100:
                    cleaner(110)
                    amourette.coeur -= 100
                    amourette.amour['caresse'] += 1
                if bisous.collidepoint(event.pos) and amourette.coeur >= 1000:
                    cleaner(170)
                    amourette.coeur -= 1000
                    amourette.amour['bisous'] += 1
                if fete.collidepoint(event.pos) and amourette.coeur >= 10000:
                    cleaner(230)
                    amourette.coeur -= 10000
                    amourette.amour['fete'] += 1
                if sexe.collidepoint(event.pos) and amourette.coeur >= 100000:
                    cleaner(290)
                    amourette.coeur -= 100000
                    amourette.amour['sexe'] += 1
                if bonheur.collidepoint(event.pos) and amourette.coeur >= 1000000:
                    cleaner(350)
                    amourette.coeur -= 1000000
                    amourette.amour['bonheur'] += 1

        amourette.coeur += amourette.amour['regard'] / 360 + amourette.amour['caresse'] / 300 + amourette.amour[
            'bisous'] / 240 + amourette.amour['fete'] / 180 + amourette.amour['sexe'] / 120 + amourette.amour[
                               'bonheur'] / 60
        pygame.display.flip()


if __name__ == "__main__":
    boucle()
    pygame.quit()
