import numpy as np
import pygame
import scene
import math

WIDTH = 1600
HEIGHT = 900

MOVE_RIGHT = [-10, 0, 0]
MOVE_LEFT = [10, 0, 0]
MOVE_UP = [0, 10, 0]
MOVE_DOWN = [0, -10, 0]
MOVE_FORWARD = [0, 0, -10]
MOVE_BACKWARD = [0, 0, 10]
ANGLE = 6

d = 200

scene = scene.Scene("scenes/scene.txt")


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_d:
            #         scene.move(MOVE_RIGHT)
            #     if event.key == pygame.K_a:
            #         scene.move(MOVE_LEFT)
            #     if event.key == pygame.K_w:
            #         scene.move(MOVE_UP)
            #     if event.key == pygame.K_s:
            #         scene.move(MOVE_DOWN)
            #     if event.key == pygame.K_e:
            #         scene.move(MOVE_FORWARD)
            #     if event.key == pygame.K_q:
            #         scene.move(MOVE_BACKWARD)
            #     if event.key == pygame.K_l:
            #         scene.rotate("y", ANGLE)
            #     if event.key == pygame.K_j:
            #         scene.rotate("y", -ANGLE)
            #     if event.key == pygame.K_i:
            #         scene.rotate("x", -ANGLE)
            #     if event.key == pygame.K_k:
            #         scene.rotate("x", ANGLE)
            #     if event.key == pygame.K_u:
            #         scene.rotate("z", -ANGLE)
            #     if event.key == pygame.K_o:
            #         scene.rotate("z", ANGLE)

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
        if keys[pygame.K_RIGHT]:
            scene.rotate("y", ANGLE)
        if keys[pygame.K_LEFT]:
            scene.rotate("y", -ANGLE)
        if keys[pygame.K_UP]:
            scene.rotate("x", -ANGLE)
        if keys[pygame.K_DOWN]:
            scene.rotate("x", ANGLE)
        if keys[pygame.K_COMMA]:
            scene.rotate("z", -ANGLE)
        if keys[pygame.K_PERIOD]:
            scene.rotate("z", ANGLE)

        screen.fill((255, 255, 255))

        for obj in scene.objects:
            obj.draw(screen, WIDTH, HEIGHT, d)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
