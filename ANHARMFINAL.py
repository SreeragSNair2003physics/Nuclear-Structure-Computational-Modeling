import numpy as np
import matplotlib.pyplot as plt

delta_values = np.linspace(-1.0, 1.0, 1000)
max_N = 5
hcrossomegazero = 1
energy_levels = []

for N in range(max_N + 1):
    for n_z in range(N + 1):
        n_perp = N - n_z
        label = f"N={N}, n_z={n_z}, n_p={n_perp}"
        E = hcrossomegazero * (N + 1.5 - (1/3) * delta_values * (2 * n_z - n_perp))
        energy_levels.append((E, label))

plt.figure(figsize=(10, 12))
for E, label in energy_levels:
    plt.plot(delta_values, E, label=label, lw=1)

plt.xlabel(r'Deformation factor $\delta_{\text{osc}}$', fontsize=14)
plt.ylabel(r'Energy ($\hbar\omega_0$)', fontsize=17)
plt.title('Anharmonic Oscillator', fontsize=20)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(fontsize=15)  # X-tick font size
plt.yticks(fontsize=15)  # Y-tick font size
plt.tight_layout()
plt.show()

