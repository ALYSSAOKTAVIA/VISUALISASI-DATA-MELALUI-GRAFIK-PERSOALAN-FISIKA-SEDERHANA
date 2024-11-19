import matplotlib.pyplot as plt

# Parameter gerak benda
kecepatan = 20 # kecepatan konstan dalam meter per detik
waktu_total = 5 # waktu total dalam detik

# Variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# Loop untuk menghitung posisi setiap detik
for t in range(waktu_total + 1):
    x = kecepatan * t # posisi benda pada waktu t
    waktu.append(t)
    posisi.append(x)

# Plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='r', linestyle='-')
plt.title("Grafik Persoalan Fisika Gerak Benda dengan Kecepatan Konstan")
plt.xlabel("Waktu (detik)")
plt.ylabel("Posisi (meter)")
plt.grid(True)
plt.show()