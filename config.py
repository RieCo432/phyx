from colors import Color

class Config:

    field_width = 1000  # px
    field_height = 700  # px
    particle_numbers = 2
    particle_colors = [Color.white, Color.red, Color.green, Color.blue]
    particle_densities = [10**3] * 4   # kg / m³
    particle_radi = [0.0008, 0.0004, 0.0004, 0.0008]  # m
    particle_charges = [10 ** (-5), 10 ** (-5)] * 4  # C
    px_per_m = 6000  # px / m
    G_const = 6.674 * 10 ** (-11)
    K_const = 8.987 * 10 ** 9
    target_fps = 60
    friction_coeff = 0.001
    max_speed = 0.0005