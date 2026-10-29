# TEST CASE PROYEK KALKULATOR GEOMETRI

## 1. Tujuan Pengujian

Pengujian ini bertujuan untuk memastikan bahwa program Kalkulator Geometri dapat menghitung luas dan keliling bangun datar dengan benar serta menangani input yang tidak valid.

## 2. Hasil Pengujian

| No. | Kasus Pengujian | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Menghitung persegi | Sisi = 5 | Luas = 25.00 dan keliling = 20.00 | Luas = 25.00 dan keliling = 20.00 | Berhasil |
| 2 | Menghitung persegi panjang | Panjang = 8, lebar = 4 | Luas = 32.00 dan keliling = 24.00 | Luas = 32.00 dan keliling = 24.00 | Berhasil |
| 3 | Menghitung segitiga | Alas = 6, tinggi = 4, sisi = 5, 5, 6 | Luas = 12.00 dan keliling = 16.00 | Luas = 12.00 dan keliling = 16.00 | Berhasil |
| 4 | Menghitung lingkaran | Jari-jari = 7 | Luas = 153.94 dan keliling = 43.98 | Luas = 153.94 dan keliling = 43.98 | Berhasil |
| 5 | Validasi input persegi | Sisi = 0 | Program menampilkan pesan kesalahan karena sisi harus lebih dari 0 | Input tidak valid: Sisi harus lebih dari 0. | Berhasil |
| 6 | Menampilkan menu kembali | Program selesai menghitung satu bangun datar | Menu ditampilkan kembali agar pengguna dapat memilih perhitungan lain | Menu ditampilkan kembali setelah setiap perhitungan | Berhasil |

## 3. Analisis Hasil Pengujian

Berdasarkan hasil pengujian, program berhasil melakukan perhitungan luas dan keliling pada empat jenis bangun datar, yaitu persegi, persegi panjang, segitiga, dan lingkaran. Hasil perhitungan sesuai dengan rumus matematika yang digunakan.

Program juga berhasil melakukan validasi terhadap input sisi persegi bernilai nol. Input tersebut ditolak dan program menampilkan pesan kesalahan yang sesuai.

Selain itu, menu program ditampilkan kembali setelah proses perhitungan selesai sehingga pengguna dapat melakukan perhitungan lainnya tanpa harus menjalankan ulang program.

## 4. Kesimpulan

Berdasarkan enam kasus pengujian yang dilakukan, seluruh kasus menunjukkan hasil sesuai dengan yang diharapkan. Dengan demikian, fungsi utama program telah berjalan sesuai dengan skenario pengujian yang dicoba.

Pengujian ini mencakup perhitungan empat bangun datar, validasi input nol, dan pengulangan menu program.
