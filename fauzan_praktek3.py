# Meminta input total belanjaan dan status anggota
total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (premium/biasa): ")

# Inisialisasi variabel diskon
diskon = 0

# Mengecek status anggota dan menghitung diskon berdasarkan aturan yang diberikan
if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15  # Diskon 15% untuk anggota premium jika total belanjaan > 500.000
    else:
        diskon = 0.10  # Diskon 10% untuk anggota premium jika total belanjaan <= 500.000
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07  # Diskon 7% untuk anggota biasa jika total belanjaan > 300.000

# Menghitung jumlah yang harus dibayar setelah diskon
jumlah_setelah_diskon = total_belanjaan - (total_belanjaan * diskon)

# Menampilkan jumlah yang harus dibayar setelah diskon
print(f"Total belanjaan: {total_belanjaan} IDR")
print(f"Diskon: {diskon * 100}%")
print(f"Total yang harus dibayar setelah diskon: {jumlah_setelah_diskon} IDR")