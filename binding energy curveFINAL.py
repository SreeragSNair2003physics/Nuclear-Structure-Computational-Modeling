import matplotlib.pyplot as plt
import numpy as np

Z = np.arange(1, 119)
A = np.array([1, 4, 6, 9, 10, 12, 14, 15, 18, 20, 22, 24, 26, 28, 30, 32, 35, 39, 39, 40, 
     44, 47, 50, 51, 55, 56, 59, 58, 63, 65, 69, 72, 74, 78, 79, 83, 85, 87, 88, 
     91, 92, 95, 97, 101, 102, 106, 107, 112, 114, 118, 121, 127, 126, 131, 132, 
     137, 138, 140, 140, 144, 145, 150, 151, 157, 158, 162, 164, 167, 168, 173, 
     174, 178, 180, 183, 186, 190, 192, 195, 196, 200, 204, 207, 208, 207, 208, 
     209, 210, 222, 223, 226, 227, 232, 231, 238, 237, 244, 243, 247, 251, 252, 
     257, 258, 259, 262, 267, 270, 269, 270, 278, 281, 281, 285, 286, 289, 289, 
     293, 293, 294])

a1, a2, a3, a4, a5 = 15.75, 17.8, 0.711, 23.7, 34

vol_E = a1 * A
sur_E = a2 * A**(2/3)
cou_E = a3 * Z * (Z - 1) / A**(1/3)
asy_E = a4 * (A - 2*Z)**2 / A
pai_E = np.where(A % 2 == 0, np.where(Z % 2 == 0, a5 * A**(-3/4), -a5 * A**(-3/4)), 0)
BE = vol_E - sur_E - cou_E - asy_E + pai_E
Bind = BE / A

plt.figure(figsize=(15, 10))
plt.plot(A, Bind, 'r-', linewidth=2, label='SEMF Prediction')

important_A = [4, 12, 16, 20, 24, 28, 32, 40, 56, 58, 90, 120, 140, 180, 208, 238]
important_labels = ['He-4', 'C-12', 'O-16', 'Ne-20', 'Mg-24', 'Si-28', 'S-32', 'Ca-40',
                     'Fe-56', 'Ni-58', 'Zr-90', 'Sn-120', 'Ce-140', 'Hf-180', 'Pb-208', 'U-238']
for a, label in zip(important_A, important_labels):
    if a in A:
        idx = np.where(A == a)[0][0]
        plt.annotate(label, (A[idx], Bind[idx]), xytext=(5, 5), textcoords='offset points',
                     arrowprops=dict(arrowstyle='->'), fontsize=9)

plt.title('Nuclear Binding Energy per Nucleon\n(Semi-Empirical Mass Formula)', fontsize=14)
plt.xlabel('Mass Number (A)', fontsize=12)
plt.ylabel('Binding Energy per Nucleon (MeV)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.axis([0, 250, 0, 10])
plt.tight_layout()
plt.show()
