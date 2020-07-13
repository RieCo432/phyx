from particle import Particle
from config import Config

class Game:

    def __init__(self):

        self.particles = []
        for i in range(Config.particle_numbers):
            self.particles.append(Particle())

    def update_all(self):
        for particle in self.particles:
            particle.update(self.particles)

    def draw_all(self, screen):
        for particle in self.particles:
            particle.draw(screen)
