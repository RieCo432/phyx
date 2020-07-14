from random import randint, uniform
from config import Config
from math import pi, sin, cos, tan, floor
import physics
import pygame


class Particle:

    def __init__(self):

        self.type = randint(0, len(Config.particle_colors)-1)
        self.color = Config.particle_colors[self.type]
        self.radius = Config.particle_radi[self.type]
        self.radius_px = floor(self.radius * Config.px_per_m)
        self.density = Config.particle_densities[self.type]
        self.charge = Config.particle_charges[self.type]
        self.volume = 4/3 * pi * self.radius ** 3
        self.mass = self.volume * self.density
        self.x = randint(self.radius_px + 10, Config.field_width - self.radius_px - 10)
        self.y = randint(self.radius_px + 10, Config.field_height - self.radius_px - 10)
        self.pos_x = self.x / Config.px_per_m
        self.pos_y = self.y / Config.px_per_m
        self.vel_x = uniform(-1, 1)
        self.vel_y = uniform(-1, 1)
        self.acc_x = 0
        self.acc_y = 0
        self.force_x = 0
        self.force_y = 0

    def calc_forces(self, particles):

        self.force_x = 0
        self.force_y = 0

        for particle in particles:
            if particle is not self and physics.get_particle_dist(self, particle) > self.radius + particle.radius:
                F_elec = physics.electric_force(self, particle)
                F_elec_x, F_elec_y = physics.get_vector_components(F_elec, self, particle)
                F_grav = physics.gravitational_force(self, particle)
                F_grav_x, F_grav_y = physics.get_vector_components(F_grav, self, particle)

                # print(F_grav, F_elec)

                self.force_x += F_elec_x + F_grav_x
                self.force_y += F_elec_y + F_grav_y
                #print(self, "vs", particle)
            #elif particle is self:
                #print(self, "vs", particle, "same, skip")
            #else:
                #print(self, "and", particle, "merged, skip")

        #print(self.force_x, self.force_y)

    def update(self, dT):

        self.acc_x = self.force_x / self.mass
        self.acc_y = self.force_y / self.mass

        self.vel_x *= (1 - Config.friction_coeff * dT)
        self.vel_y *= (1 - Config.friction_coeff * dT)

        self.vel_x += self.acc_x * dT
        self.vel_y += self.acc_y * dT

        self.pos_x += self.vel_x * dT
        self.pos_y += self.vel_y * dT

    def detect_collisions(self, particles, dT):

        if self.pos_x - self.radius < 0:
            self.pos_x = self.radius
            self.vel_x *= -1
        elif self.pos_x + self.radius > Config.field_width_m:
            self.pos_x = Config.field_width_m - self.radius
            self.vel_x *= -1

        if self.pos_y - self.radius < 0:
            self.pos_y = self.radius
            self.vel_y *= -1
        elif self.pos_y + self.radius > Config.field_height_m:
            self.pos_y = Config.field_height_m - self.radius
            self.vel_y *= -1

        for particle in particles:
            if physics.get_particle_dist(self, particle) <= self.radius + particle.radius:
                new_self_vel_x = (self.vel_x * (abs(self.mass) - abs(particle.mass)) + (2 * abs(particle.mass) * particle.vel_x)) / (abs(self.mass) + abs(particle.mass))
                new_self_vel_y = (self.vel_y * (abs(self.mass) - abs(particle.mass)) + (2 * abs(particle.mass) * particle.vel_y)) / (abs(self.mass) + abs(particle.mass))

                new_particle_vel_x = (particle.vel_x * (abs(particle.mass) - abs(self.mass)) + (2 * abs(self.mass) * self.vel_x)) / (abs(self.mass) + abs(particle.mass))
                new_particle_vel_y = (particle.vel_y * (abs(particle.mass) - abs(self.mass)) + (2 * abs(self.mass) * self.vel_y)) / (abs(self.mass) + abs(particle.mass))

                self.vel_x = new_self_vel_x
                self.vel_y = new_self_vel_y

                particle.vel_x = new_particle_vel_x
                particle.vel_y = new_particle_vel_y

                self.pos_x += self.vel_x * dT
                self.pos_y += self.vel_y * dT

                particle.pos_x += particle.vel_x * dT
                particle.pos_y += particle.vel_y * dT

    def draw(self, screen):

        self.x = floor(self.pos_x * Config.px_per_m)
        self.y = floor(self.pos_y * Config.px_per_m)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius_px)
