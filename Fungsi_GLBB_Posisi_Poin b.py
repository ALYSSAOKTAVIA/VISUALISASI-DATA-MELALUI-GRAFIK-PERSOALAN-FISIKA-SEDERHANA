import numpy as np
import matplotlib.pyplot as plt

g = 9.8 # percepatan gravitasi konstan sebesar 9.8 m/s^2
t = 120 # Waktu sebesar 120 detik (2 menit)

# Definisi fungsi x(t)
def x(t):
    return (1/2)* g * t**2

# Mendefinisikan rentang data waktu (t)
t = np.arange(0, 120, 1)

# Menghitung nilai y untuk setiap nilai x
y = x(t)

#Menampilkan grafik f(x) dan g(x)
plt.plot(t, y, marker="o", color="b", linestyle="-")

# Menambah Label 
plt.title("Grafik GLBB")
plt.xlabel("posisi (g)")
plt.ylabel("waktu (t)")
plt.grid(True)
plt.show()