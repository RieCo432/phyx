import time

import pygame
from datetime import datetime
from os import environ
from config import Config
import sys
from colors import Color
from game import Game

if __name__ == "__main__":

    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
    pygame.init()
    game = Game()
    screen = pygame.display.set_mode((Config.field_width, Config.field_height))
    pygame.font.init()
    screen.fill(0)
    frameend = datetime.now()
    frametimes = [0.001] * 101
    last_framerate_update = datetime.now()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(Color.black)
        game.update_all()
        # print(game.particles[0].pos_x, game.particles[0].pos_y, game.particles[0].color)
        game.draw_all(screen)

        pygame.display.update()
        if len(frametimes) > 100:
            frametimes = frametimes[-100:-1]

        frametimes.append((datetime.now() - frameend).total_seconds())
        frameend = datetime.now()
        if (datetime.now() - last_framerate_update).total_seconds() > 0.5:
            pygame.display.set_caption("Framerate: %f" % (1 / (sum(frametimes) / len(frametimes))))
            last_framerate_update = datetime.now()

        time.sleep(0.01)
