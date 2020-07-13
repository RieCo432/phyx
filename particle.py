from random import randint
from config import Config
from math import pi, sin, cos, tan, floor
import physics
import pygame


class Particle:

    def __init__(self):

        self.type = randint(0, 3)
        self.color = Config.particle_colors[self.type]
        self.radius = Config.particle_radi[self.type]
        self.density = Config.particle_densities[self.type]
        self.charge = Config.particle_charges[self.type]
        self.volume = 4/3 * pi * self.radius ** 3
        self.mass = self.volume * self.density
        self.x = randint(0, Config.field_width-1)
        self.y = randint(0, Config.field_height-1)
        self.pos_x = self.x / Config.px_per_m
        self.pos_y = self.y / Config.px_per_m
        self.vel_x = 0
        self.vel_y = 0
        self.acc_x = 0
        self.acc_y = 0

    def update(self, particles):

        self.acc_x = 0
        self.acc_y = 0

        #self.acc_x = Config.friction_coeff * self.vel_x ** 2
        #self.acc_y = Config.friction_coeff * self.vel_y ** 2

        #if self.vel_x < 0:
        #    self.acc_x *= -1
        #if self.vel_y < 0:
        #    self.acc_y *= -1

        for particle in particles:
            if particle.pos_x != self.pos_x or particle.pos_y != self.pos_y and physics.dist(self.pos_x, self.pos_y, particle.pos_x, particle.pos_y) > (self.radius + particle.radius):
                grav_F = physics.gravitational_force(self, particle)
                grav_F_x, grav_F_y = physics.get_vector_components(grav_F, self, particle)
                elec_F = physics.electric_force(self, particle)
                elec_F_x, elec_F_y = physics.get_vector_components(elec_F, self, particle)

                self.acc_x += grav_F_x / self.mass
                self.acc_x += elec_F_x / self.mass
                self.acc_y += grav_F_y / self.mass
                self.acc_y += elec_F_y / self.mass

                self.acc_x /= Config.target_fps
                self.acc_y /= Config.target_fps


        self.vel_x += self.acc_x
        self.vel_y += self.acc_y

        # temp solution for excessive speeds
        if self.vel_x > Config.max_speed:
            self.vel_x = Config.max_speed
        elif self.vel_x < Config.max_speed:
            self.vel_x = -Config.max_speed
        if self.vel_y > Config.max_speed:
            self.vel_y = Config.max_speed
        elif self.vel_y < Config.max_speed:
            self.vel_y = -Config.max_speed

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        self.x = floor(self.pos_x * Config.px_per_m)
        self.y = floor(self.pos_y * Config.px_per_m)

        if self.x < 0:
            if self.vel_x < 0:
                self.vel_x = - self.vel_x
            self.x = 1
            self.pos_x = 1 / Config.px_per_m
        elif self.x > Config.field_width:
            if self.vel_x > 0:
                self.vel_x = - self.vel_x
            self.x = Config.field_width - 1
            self.pos_x = (Config.field_width - 1) / Config.px_per_m
        if self.y < 0:
            if self.vel_y < 0:
                self.vel_y = - self.vel_y
            self.y = 1
            self.pos_y = 1 / Config.px_per_m
        elif self.y > Config.field_height:
            if self.vel_y > 0:
                self.vel_y = - self.vel_y
            self.y = Config.field_height - 1
            self.pos_y = (Config.field_height - 1) / Config.px_per_m

        print(self.pos_x, self.pos_y, self.vel_x, self.vel_y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius * Config.px_per_m)
