from particle import Particle
from config import Config


class Game:

    def __init__(self):

        self.particles = []
        for i in range(Config.particle_numbers):
            self.particles.append(Particle())

    def calc_forces_all(self):
        for particle in self.particles:
            particle.calc_forces(self.particles)

    def update_all(self, dT):
        for particle in self.particles:
            particle.update(dT)

    def detect_collisions_all(self):
        for part_num in range(len(self.particles)):
            self.particles[part_num].detect_collisions(self.particles[part_num:])

    def draw_all(self, screen):
        for particle in self.particles:
            particle.draw(screen)
