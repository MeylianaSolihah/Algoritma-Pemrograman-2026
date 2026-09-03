# Program Penyelesaian SPLV (Sistem Persamaan Linear Dua Variabel)

# Input koefisien persamaan pertama
print("Masukkan koefisien persamaan pertama (a1x + b1y = c1):")
a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))

# Input koefisien persamaan kedua
print("\nMasukkan koefisien persamaan kedua (a2x + b2y = c2):")
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))

# Hitung determinan
det = a1 * b2 - a2 * b1

# Proses pengecekan dan perhitungan solusi
if det != 0:
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    print(f"\nSolusi SPLV adalah (x, y) = ({x}, {y})")
else:
    print("\nERROR: Sistem tidak memiliki solusi unik.")

