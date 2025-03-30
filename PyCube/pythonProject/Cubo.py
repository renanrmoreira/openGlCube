from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


def transform_vertex(vertex, translation=(0, 0, 0), scale=(1, 1, 1), mirror=(1, 1, 1)):
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


def wireCube():
    translation = (0.5, 0.5, 0)  # Translação (x, y, z)
    scale = (1.5, 1.5, 1.5)  # Escala (x, y, z)
    mirror = (-1, 1, 1)  # Espelhamento (x, y, z) (-1 inverte eixo correspondente)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            transformed_vertex = transform_vertex(vertices[vertex], translation, scale, mirror)
            glVertex3fv(transformed_vertex)
    glEnd()
