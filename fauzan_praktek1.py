#nama : fauzan alwafi zufar
#kelas: XI TKJ2
#no absen: 11
#destinasi waktu yg akan selesai
#soal Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika
#estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat
#waktu," jika tidak, program harus mencetak "Terlambat."
from datetime import datetime
estimasi_waktu_selesai = input ("Masukkan estimasi waktu selesai (tahun-bulan-hari): ")
tanggal_target_selesai = input ("Masukkan tanggal target selesai (tahun-bulan-hari): ")


if estimasi_waktu_selesai <= tanggal_target_selesai:
    print("Tepat waktu")
else:
    print("Terlambat")