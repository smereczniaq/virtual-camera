import numpy as np
import pygame
import scene
import math
from bsp_tree import build_bsp_tree, traverse_bsp_tree

WIDTH = 1600
HEIGHT = 900

MOVE_RIGHT = [-3, 0, 0]
MOVE_LEFT = [3, 0, 0]
MOVE_UP = [0, 3, 0]
MOVE_DOWN = [0, -3, 0]
MOVE_FORWARD = [0, 0, -3]
MOVE_BACKWARD = [0, 0, 3]
ANGLE = 0.5
ZOOM = 1.1

d = 500

scene = scene.Scene("scenes/scene.txt")


def main():
    global d
    global scene
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            scene.move(MOVE_RIGHT)
        if keys[pygame.K_a]:
            scene.move(MOVE_LEFT)
        if keys[pygame.K_SPACE]:
            scene.move(MOVE_UP)
        if keys[pygame.K_LSUPER]:
            scene.move(MOVE_DOWN)
        if keys[pygame.K_w]:
            scene.move(MOVE_FORWARD)
        if keys[pygame.K_s]:
            scene.move(MOVE_BACKWARD)
        if keys[pygame.K_LEFT]:
            scene.rotate("y", ANGLE)
        if keys[pygame.K_RIGHT]:
            scene.rotate("y", -ANGLE)
        if keys[pygame.K_UP]:
            scene.rotate("x", -ANGLE)
        if keys[pygame.K_DOWN]:
            scene.rotate("x", ANGLE)
        if keys[pygame.K_COMMA]:
            scene.rotate("z", ANGLE)
        if keys[pygame.K_PERIOD]:
            scene.rotate("z", -ANGLE)
        if keys[pygame.K_EQUALS]:
            if d < 2000:
                d *= ZOOM
        if keys[pygame.K_MINUS]:
            if d > 50:
                d /= ZOOM
        if keys[pygame.K_r]:
            d = 500
            scene = scene.reload()

        screen.fill((255, 255, 255))
        scene.draw(screen, WIDTH, HEIGHT, d)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
