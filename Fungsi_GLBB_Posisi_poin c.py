import numpy as np
import matplotlib.pyplot as plt

a = 2 # percepatan konstan sebesar 2 m/s^2
t = 100 # waktu maksimum sebesar 100 detik

# Definisi fungsi x(t)
def x(t):
    return (1/2) * a * t**2

# Mendefinisikan rentang data waktu (t)
t = np.arange(0, 100, 1)

# Menghitung nilai y untuk setiap nilai x
y = x(t)

#Menampilkan grafik f(x) dan g(x)
plt.plot(t, y, marker="o", color="r", linestyle="-")

# Menambah Label 
plt.title("Grafik GLBB")
plt.xlabel("posisi (a)")
plt.ylabel("waktu (t)")
plt.grid(True)
plt.show()