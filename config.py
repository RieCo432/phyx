from colors import Color

class Config:

    field_width = 1000  # px
    field_height = 700  # px
    particle_numbers = 40
    particle_colors = [Color.white, Color.red, Color.green, Color.blue]
    particle_densities = [10**12] * 4   # kg / m³
    particle_radi = [0.005, 0.005, 0.01, 0.0035]  # m
    particle_charges = [1 * 10 ** (-3), - 1 * 10 ** (-3), 3 * 10 ** (-3), - 2 * 10 ** (-3)]  # C
    px_per_m = 1000  # px / m
    G_const = 6.674 * 10 ** (-11)
    K_const = 8.987 * 10 ** 9
    target_fps = 60
    friction_coeff = 0.001
    field_width_m = field_width / px_per_m
    field_height_m = field_height / px_per_m