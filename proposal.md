# PROPOSAL PROYEK PERTEMUAN 15
# KALKULATOR GEOMETRI BANGUN DATAR BERBASIS PYTHON

## 1. Identitas Proyek

- Nama: Kesya Nur Aprilliani
- NIM: 2225250219
- Kelas: 3E
- Program Studi: Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman
- Pertemuan: 15

## 2. Deskripsi Proyek

Kalkulator Geometri Bangun Datar merupakan program sederhana berbasis Python yang dibuat untuk membantu pengguna menghitung luas dan keliling beberapa jenis bangun datar. Program ini menerapkan konsep matematika ke dalam bahasa pemrograman sehingga proses perhitungan dapat dilakukan secara lebih praktis dan sistematis.

Bangun datar yang tersedia dalam program meliputi persegi, persegi panjang, segitiga, dan lingkaran. Pengguna dapat memilih jenis bangun datar, memasukkan nilai yang diperlukan, kemudian memperoleh hasil perhitungan secara otomatis.

## 3. Latar Belakang

Geometri merupakan salah satu materi matematika yang berkaitan dengan bentuk, ukuran, luas, dan keliling suatu bangun. Dalam pembelajaran matematika, peserta didik perlu memahami rumus serta mampu menerapkannya untuk menyelesaikan permasalahan.

Perkembangan teknologi memberikan kesempatan untuk menerapkan konsep matematika melalui program komputer. Oleh karena itu, dibuat program Kalkulator Geometri Bangun Datar menggunakan Python sebagai bentuk penerapan materi matematika dalam pemrograman.

Program ini diharapkan dapat membantu pengguna melakukan perhitungan serta menjadi media pembelajaran untuk memahami hubungan antara rumus matematika dan algoritma pemrograman.

## 4. Tujuan Proyek

1. Mengembangkan program kalkulator geometri menggunakan Python.
2. Menerapkan rumus luas dan keliling bangun datar ke dalam program.
3. Melatih penerapan variabel, fungsi, percabangan, perulangan, dan validasi input.
4. Menghasilkan program yang mudah digunakan.
5. Menguji ketepatan hasil perhitungan program.

## 5. Manfaat Proyek

1. Mempermudah perhitungan luas dan keliling bangun datar.
2. Membantu memahami penerapan rumus geometri.
3. Meningkatkan keterampilan pemrograman Python.
4. Melatih kemampuan berpikir logis, sistematis, dan teliti.
5. Menjadi contoh penerapan teknologi dalam pembelajaran matematika.

## 6. Fitur Program

1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Menerima input dari pengguna.
6. Melakukan validasi nilai masukan.
7. Menampilkan hasil perhitungan.
8. Menyediakan menu untuk mengulangi perhitungan atau mengakhiri program.

## 7. Rumus Matematika

### A. Persegi
Luas = sisi × sisi

Keliling = 4 × sisi

### B. Persegi Panjang
Luas = panjang × lebar

Keliling = 2 × (panjang + lebar)

### C. Segitiga
Luas = ½ × alas × tinggi

Keliling = sisi a + sisi b + sisi c

### D. Lingkaran
Luas = π × r²

Keliling = 2 × π × r

Keterangan:
- π = 3,14 atau 22/7.
- r = jari-jari lingkaran.

## 8. Analisis Input, Proses, dan Output

### A. Input
- Pilihan jenis bangun datar.
- Nilai sisi persegi.
- Nilai panjang dan lebar persegi panjang.
- Nilai alas, tinggi, dan sisi segitiga.
- Nilai jari-jari lingkaran.

### B. Proses
1. Menerima pilihan bangun datar dari pengguna.
2. Meminta nilai sesuai bangun datar yang dipilih.
3. Memeriksa validitas nilai masukan.
4. Melakukan perhitungan menggunakan rumus matematika.
5. Menyiapkan hasil luas dan keliling.

### C. Output
- Jenis bangun datar.
- Hasil luas.
- Hasil keliling.
- Pesan apabila terdapat kesalahan input.

## 9. Algoritma Program

1. Memulai program.
2. Menampilkan menu pilihan bangun datar.
3. Meminta pengguna memilih menu.
4. Memeriksa pilihan pengguna.
5. Meminta nilai yang dibutuhkan.
6. Memvalidasi nilai masukan.
7. Menghitung luas dan keliling.
8. Menampilkan hasil perhitungan.
9. Menanyakan apakah pengguna ingin melakukan perhitungan kembali.
10. Mengakhiri program apabila pengguna memilih keluar.

## 10. Pseudocode

```text
START

WHILE pengguna ingin melanjutkan:
    Tampilkan menu bangun datar
    Input pilihan

    IF pilihan = 1:
        Input sisi
        Hitung luas dan keliling persegi

    ELSE IF pilihan = 2:
        Input panjang dan lebar
        Hitung luas dan keliling persegi panjang

    ELSE IF pilihan = 3:
        Input alas, tinggi, sisi a, sisi b, sisi c
        Hitung luas dan keliling segitiga

    ELSE IF pilihan = 4:
        Input jari-jari
        Hitung luas dan keliling lingkaran

    ELSE:
        Tampilkan pesan pilihan tidak valid

    Tampilkan hasil jika input valid

END WHILE

END
```

## 11. Struktur Program

```text
Proyek_Matematika_2225250219/
│
├── README.md
├── proposal.md
├── main.py
│
├── src/
│   └── kalkulator_geometri.py
│
└── tests/
    └── test_case.md
```

## 12. Rencana Pengujian

Pengujian dilakukan untuk memastikan program menghasilkan perhitungan yang sesuai dengan rumus matematika.

| No. | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Perhitungan persegi | Luas dan keliling benar |
| 2 | Perhitungan persegi panjang | Luas dan keliling benar |
| 3 | Perhitungan segitiga | Luas dan keliling benar |
| 4 | Perhitungan lingkaran | Luas dan keliling benar |
| 5 | Input nilai negatif | Ditolak oleh validasi |
| 6 | Pilihan menu tidak tersedia | Pesan kesalahan ditampilkan |

## 13. Teknologi yang Digunakan

- Python untuk mengembangkan program.
- Visual Studio Code sebagai editor.
- Git untuk pengelolaan versi.
- GitHub untuk penyimpanan dan dokumentasi proyek.

## 14. Kesimpulan

Proyek Kalkulator Geometri Bangun Datar merupakan penerapan konsep matematika ke dalam pemrograman Python. Program ini dirancang untuk membantu pengguna menghitung luas dan keliling beberapa bangun datar melalui menu yang sederhana.

Melalui proyek ini, konsep geometri dapat diterapkan secara langsung dengan memanfaatkan algoritma, fungsi, percabangan, perulangan, dan validasi input. Dengan demikian, proyek ini dapat menjadi sarana untuk meningkatkan pemahaman matematika sekaligus keterampilan pemrograman.
