import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

N_max = 7
base_energy_offset = 5
orbital_labels = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'j', 'k']
x0, x1, x2 = [0, 0.75], [1, 1.75], [2.25, 3]

def get_orbital_label(l):
    return orbital_labels[l] if l < len(orbital_labels) else f"l={l}"

def calculate_energy(N, l, D):
    return N + base_energy_offset + D * l * (l + 1)

def spin_orbit_split(E, l, C):
    return E + C * l / 2, E - C * (l + 1) / 2

def draw_levels(ax, C, D):
    ax.clear()
    ax.set_title("Interactive Single-Particle Shell Model", fontsize=16)
    ax.set_xticks([])
    ax.set_ylabel("Energy", fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.3)

    for N in range(N_max + 1):
        base_E = N + base_energy_offset
        label_offset = 0 + N * 0.03
        ax.plot(x0, [base_E, base_E], color='b')
        ax.text(0.2, base_E + label_offset, f'N={N}', fontsize=12, weight='bold')

        for l in range(N % 2, N + 1, 2):
            n = (N + 2 - l) // 2
            label = get_orbital_label(l)
            E = calculate_energy(N, l, D)
            E_upper, E_lower = spin_orbit_split(E, l, C)

            # Plot levels
            ax.plot(x1, [E, E], color='g')
            ax.plot(x2, [E_upper, E_upper], color='r')
            if l > 0:
                ax.plot(x2, [E_lower, E_lower], color='b')

            # Dashed transitions
            ax.plot([1.75, 2.25], [E, E_upper], '--', color='black')
            if l > 0:
                ax.plot([1.75, 2.25], [E, E_lower], '--', color='m')
            ax.plot([0.75, 1], [base_E, E], '--', color='yellow')

            ax.text(1.4, E + 0.08 + l * 0.02, f"{label} (l={l})", fontsize=10)
            ax.text(2.25, E_upper - 0.07, f"{n}{label}{int(2 * l + 1)}/2", fontsize=9)
            if l > 0:
                ax.text(3.01, E_lower - 0.18, f"{n}{label}{int(2 * l - 1)}/2", fontsize=9)

    ax.figure.canvas.draw_idle()

fig, ax = plt.subplots(figsize=(15, 10))
plt.subplots_adjust(left=0.1, bottom=0.25)

initial_C = -0.1
initial_D = -0.0225
draw_levels(ax, initial_C, initial_D)

axcolor = 'lightgoldenrodyellow'
ax_C = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_D = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)

slider_C = Slider(ax_C, 'C (Spin-Orbit)', -0.3, 0.0, valinit=initial_C, valstep=0.005)
slider_D = Slider(ax_D, 'D (Deformation)', -0.05, 0.0, valinit=initial_D, valstep=0.001)

def update(val):
    C = slider_C.val
    D = slider_D.val
    draw_levels(ax, C, D)

slider_C.on_changed(update)
slider_D.on_changed(update)

plt.show()