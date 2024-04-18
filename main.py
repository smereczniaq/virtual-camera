import numpy as np
import pygame
import scene
import math

WIDTH = 1600
HEIGHT = 900

MOVE_RIGHT = [-20, 0, 0]
MOVE_LEFT = [20, 0, 0]
MOVE_UP = [0, 20, 0]
MOVE_DOWN = [0, -20, 0]
MOVE_FORWARD = [0, 0, -20]
MOVE_BACKWARD = [0, 0, 20]
ANGLE = 10

d = 200

scene = scene.Scene("objects.txt")


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    scene.move(MOVE_RIGHT)
                elif event.key == pygame.K_a:
                    scene.move(MOVE_LEFT)
                elif event.key == pygame.K_w:
                    scene.move(MOVE_UP)
                elif event.key == pygame.K_s:
                    scene.move(MOVE_DOWN)
                elif event.key == pygame.K_e:
                    scene.move(MOVE_FORWARD)
                elif event.key == pygame.K_q:
                    scene.move(MOVE_BACKWARD)
                elif event.key == pygame.K_l:
                    scene.rotate("y", ANGLE)
                elif event.key == pygame.K_j:
                    scene.rotate("y", -ANGLE)
                elif event.key == pygame.K_i:
                    scene.rotate("x", -ANGLE)
                elif event.key == pygame.K_k:
                    scene.rotate("x", ANGLE)
                elif event.key == pygame.K_u:
                    scene.rotate("z", -ANGLE)
                elif event.key == pygame.K_o:
                    scene.rotate("z", ANGLE)
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for obj in scene.objects:
            obj.draw(screen, WIDTH, HEIGHT, d)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
