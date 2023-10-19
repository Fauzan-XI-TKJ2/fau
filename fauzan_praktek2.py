# Nama file yang ingin diperiksa
nama_file = input ("Masukkan nama file: ")

# Daftar file yang ada di server
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

# Memeriksa apakah nama_file sudah ada di daftar_file_di_server
if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")