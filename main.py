from src.kalkulator_geometri import (
    persegi,
    persegi_panjang,
    segitiga,
    lingkaran,
)


def tampilkan_menu():
    print("\n=== KALKULATOR GEOMETRI BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")


def jalankan_program():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        try:
            if pilihan == "1":
                sisi = float(input("Masukkan sisi: "))
                luas, keliling = persegi(sisi)

            elif pilihan == "2":
                panjang = float(input("Masukkan panjang: "))
                lebar = float(input("Masukkan lebar: "))
                luas, keliling = persegi_panjang(panjang, lebar)

            elif pilihan == "3":
                alas = float(input("Masukkan alas: "))
                tinggi = float(input("Masukkan tinggi: "))
                a = float(input("Masukkan sisi A: "))
                b = float(input("Masukkan sisi B: "))
                c = float(input("Masukkan sisi C: "))
                luas, keliling = segitiga(alas, tinggi, a, b, c)

            elif pilihan == "4":
                r = float(input("Masukkan jari-jari: "))
                luas, keliling = lingkaran(r)

            elif pilihan == "5":
                print("Program selesai. Terima kasih!")
                break

            else:
                print("Pilihan tidak valid.")
                continue

            print(f"Luas     : {luas:.2f}")
            print(f"Keliling : {keliling:.2f}")

        except ValueError as error:
            print(f"Input tidak valid: {error}")


if __name__ == "__main__":
    jalankan_program()
