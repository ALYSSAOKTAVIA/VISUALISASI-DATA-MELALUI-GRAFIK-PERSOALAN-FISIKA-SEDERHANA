import matplotlib.pyplot as plt

#Parameter gerak benda
percepatan_gravitasi = 9.8 # Percepatan gravitasi konstan dalam meter per detik^2
waktu_maksimum = 120 # waktu dalam detik (2 menit)

# Variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# Loop untuk menghitung posisi setiap detik 
for t in range(waktu_maksimum + 1):
    x = (1/2) * percepatan_gravitasi * t**2 #posisi benda pada waktu t
    waktu.append(t)
    posisi.append(x)

# Plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='b', linestyle='-')
plt.title("Grafik GLBB Gerak Benda dengan Percepatan Gravitasi Konstan")
plt.xlabel("Waktu (detik)")
plt.ylabel("Posisi (meter)")
plt.grid(True)
plt.show()