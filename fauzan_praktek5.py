penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

# Menentukan kategori produk berdasarkan aturan yang diberikan
if penjualan > 1000:
    kategori = "Produk Terlaris"
elif 500 <= penjualan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

# Menampilkan kategori produk
print(f"Jumlah Penjualan: {penjualan} unit")
print(f"Kategori Produk: {kategori}")