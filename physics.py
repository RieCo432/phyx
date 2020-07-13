from config import Config
from math import sqrt


def electric_force(p1, p2):
    return - Config.K_const * p1.charge * p2.charge / dist(p1.pos_x, p1.pos_y, p2.pos_x, p2.pos_y)**2


def gravitational_force(p1, p2):
    return Config.G_const * p1.mass * p2.mass / dist(p1.pos_x, p1.pos_y, p2.pos_x, p2.pos_y)**2


def get_x1y1x2y2(p1, p2):
    return p1.pos_x, p1.pos_y, p2.pos_x, p2.pos_y


def dist(x1, y1, x2, y2):
    dX = abs(x1 - x2)
    dY = abs(y1 - y2)

    return sqrt(dX**2 + dY**2)


def get_particle_dist(p1, p2):

    return dist(p1.pos_x, p1.pos_y, p2.pos_x, p2.pos_y)


def get_vector_components(F, p1, p2):

    sin_a = (p2.pos_y - p1.pos_y) / dist(p1.pos_x, p1.pos_y, p2.pos_x, p2.pos_y)
    cos_a = (p2.pos_x - p1.pos_x) / dist(p1.pos_x, p1.pos_y, p2.pos_x, p2.pos_y)

    F_x = F * cos_a
    F_y = F * sin_a

    return F_x, F_y