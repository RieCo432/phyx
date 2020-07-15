from colors import Color

class Config:

    field_width = 1800  # px
    field_height = 900  # px
    particle_numbers = 35
    particle_colors = [Color.red, Color.white, Color.blue, Color.green]
    particle_densities = [10**12, 10**12, 10**8, 10**12]  # kg / m³
    particle_radi = [0.01, 0.01, 0.005, 0.03]  # m
    particle_charges = [1 * 10 ** (-15), 0, -1 * 10 ** (-15), 0]  # C
    px_per_m = 1000  # px / m
    G_const = 6.674 * 10 ** (-11)
    K_const = 8.987 * 10 ** 9
    target_fps = 60
    friction_coeff = 0.05
    field_width_m = field_width / px_per_m
    field_height_m = field_height / px_per_m