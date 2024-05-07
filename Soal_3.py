# Input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Initialize total harga
total_harga = 0

# Input harga barang
for i in range(jumlah_barang):
    harga_barang = float(input("Masukkan harga barang ke-" + str(i+1) + ": "))
    total_harga += harga_barang

# Tampilkan total harga
print("Total harga belanjaan adalah: RM", round(total_harga, 2))



