#nama    :afrizal varellino braga
#kelas   :XI TKJ2
#no absen: 1
#soal Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek
#tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek
#diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

# Meminta input status persiapan proyek (Siap atau Tunda)
status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ").strip().lower()

# Menentukan apakah proyek dapat diluncurkan
if status_persiapan == "siap":
    print("Proyek diluncurkan.")
elif status_persiapan == "tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Masukkan 'Siap' atau 'Tunda'.")