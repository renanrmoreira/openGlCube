from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math


def transform_vertex(vertex, translation=(0, 0, 0), scale=(1, 1, 1), mirror=(1, 1, 1)):
    """
    Aplica transformações geométricas em um vértice:
    - Translação: move o vértice no espaço
    - Escala: aumenta ou diminui o tamanho
    - Espelhamento: inverte coordenadas (usando valor -1)
    """
    x, y, z = vertex

    x *= scale[0] * mirror[0]
    y *= scale[1] * mirror[1]
    z *= scale[2] * mirror[2]

    x += translation[0]
    y += translation[1]
    z += translation[2]
    return (x, y, z)


vertices = [(0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5)]

edges = [(0, 1), (1, 3), (3, 2), (2, 0),
         (4, 5), (5, 7), (7, 6), (6, 4),
         (0, 6), (1, 7), (2, 4), (3, 5)]


def draw_cube(translation, scale, mirror):

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            # aplica as transformações em cada vertice
            transformed_vertex = transform_vertex(vertices[vertex], translation, scale, mirror)
            glVertex3fv(transformed_vertex)
    glEnd()


def draw_cubes(rotation_angle, time):
    # Calcula a escala usando uma função senoidal para criar um efeito pulsante
    scale_factor = 1.4 + 0.6 * math.sin(time * 0.05)

    # Calcula a translação horizontal usando uma função senoidal e faz os cubos moverem-se horizontalmente
    x_offset = 1.0 * math.sin(time * 0.03)

    # distância base entre os cubos
    base_distance = 2.0

    scale = (scale_factor, scale_factor, scale_factor)  # Escala animada para ambos os cubos

    # Cubo da esquerda (normal, rotação no sentido positivo)
    glPushMatrix()
    # Posiciona à esquerda e adiciona o deslocamento animado
    glTranslatef(-base_distance + x_offset, 0.0, 0.0)
    # Rotação normal
    glRotatef(rotation_angle, 1, 1, 1)
    draw_cube(translation=(0, 0, 0), scale=scale, mirror=(1, 1, 1))
    glPopMatrix()

    # Cubo da direita (espelhado, rotação no sentido negativo)
    glPushMatrix()
    # Posiciona à direita e adiciona o mesmo deslocamento animado
    glTranslatef(base_distance + x_offset, 0.0, 0.0)
    # Rotação em sentido oposto (valores negativos)
    glRotatef(-rotation_angle, 1, 1, 1)
    draw_cube(translation=(0, 0, 0), scale=scale, mirror=(-1, 1, 1))  # Espelhamento no eixo X
    glPopMatrix()