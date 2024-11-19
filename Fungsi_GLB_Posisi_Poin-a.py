import numpy as np
import matplotlib.pyplot as plt

v = 20 # kecepatan konstan sebesar 20 m/s
# Definisi fungsi x(t)
def x(t):
    return v*t

# Mendefinisikan rentang data waktu (t)
t = np.arange(0, 5, 1)

# Menghitung nilai y untuk setiap nilai x
y = x(t)

#Menampilkan grafik f(x) dan g(x)
plt.plot(t, y, marker="o", color="r", linestyle="-")

# Menambah Label 
plt.title("Grafik Persoalan Fisika Gerak Benda Kecepatan Konstan dengan Fungsi")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()