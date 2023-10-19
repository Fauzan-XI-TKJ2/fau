# Meminta input informasi pembaruan (misalnya: "Y" atau "N")
pembaruan = input("Apakah terdapat pembaruan yang memerlukan restart (Y/N)? ").strip().lower()

# Memeriksa apakah pembaruan memerlukan restart
if pembaruan == "y":
    print("Sistem perlu di-restart.")
elif pembaruan == "n":
    print("Sistem tidak perlu di-restart.")
else:
    print("Input tidak valid. Silakan masukkan 'Y' atau 'N' untuk mengindikasikan pembaruan.")