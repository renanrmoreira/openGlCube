import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import Cubo
import math

pygame.init()

screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Cubos com Rotação Espelhada, Movimento e Escala')


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -8)
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


# controla o ângulo de rotação
rotation_angle = 0
# contador de tempo para animar escala e translação
time_counter = 0


def display():
    global rotation_angle, time_counter

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rotation_angle += 1
    time_counter += 1

    Cubo.draw_cubes(rotation_angle, time_counter)

    pygame.display.flip()

initialise()

# configura o relógio para controle de FPS
clock = pygame.time.Clock()

# Loop principal
done = False
while not done:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    # 60 FPS
    clock.tick(60)

pygame.quit()