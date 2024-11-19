import numpy as np
import matplotlib.pyplot as plt

vo = 60 # kecepatan awal sebesar 60 m/s
a = 2.25 # percepatan konstan sebesar 2.25 m/s^2
t = 20 # waktu sebesar 20 detik

# Definisi fungsi x(t)
def x(t):
    return vo * t - (1/2) * a * t**2

# Mendefinisikan rentang data waktu (t)
t = np.arange(0, 20, 1)

# Menghitung nilai y untuk setiap nilai x
y = x(t)

#Menampilkan grafik f(x) dan g(x)
plt.plot(t, y, marker="o", color="purple", linestyle="-")

# Menambah Label 
plt.title("Grafik GLBB dengan Percepatan Konstan dan Kecepatan awal")
plt.xlabel("posisi (a)")
plt.ylabel("waktu (t)")
plt.grid(True)
plt.show()