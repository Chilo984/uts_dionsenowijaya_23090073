def hitung_bmi(berat, tinggi):
    """
    Menghitung BMI dari berat dan tinggi badan.

    Argumen:
        berat (mengambang): Berat dalam kilogram.
        tinggi (mengambang): Tinggi dalam meter.

    Pengembalian:
        mengambang: nilai BMI.
    """
    bmi = berat badan / (tinggi badan ** 2)
    kembali bmi

def bmi_rekomendasi(bmi):
    """
    Memberikan rekomendasi kesehatan berdasarkan nilai BMI.

    Argumen:
        bmi (mengambang): nilai BMI.

    Pengembalian:
        str: Rekomendasi kesehatan.
    """
    jika bmi <18,5:
        rekomendasi = "Berat badan kurang, silakan makan lebih banyak makanan sehat."
    elif 18.5 <= bmi < 24.9:
        rekomendasi = "Berat badan normal, selamat!"
    elif 25 <= bmi < 29.9:
        rekomendasi = "Kelebihan berat badan, silakan olahraga dan makan sehat."
    kalau tidak:
        rekomendasi = "Obesitas, silakan hubungi dokter dan segera mulai olahraga dan makan sehat."
    rekomendasi pengembalian

# Dapatkan masukan pengguna
berat = float(input("Masukkan berat badan anda dalam kilogram: "))
height = float(input("Masukkan tinggi badan anda dalam meter: "))

# Hitung BMI
bmi = hitung_bmi(berat badan, tinggi badan)

# Cetak nilai BMI
print(f"Nilai BMI anda adalah: {bmi:.2f}")

# Cetak rekomendasi kesehatan
cetak(bmi_rekomendasi(bmi))
