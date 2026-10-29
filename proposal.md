# PROPOSAL PROYEK
## KALKULATOR GEOMETRI BANGUN DATAR BERBASIS PYTHON

### Identitas Mahasiswa

Nama: Kesya Nur Aprilliani

NIM: 2225250219

Program Studi: Pendidikan Matematika

Kelas: 3E

Mata Kuliah: Algoritma dan Pemrograman

Pertemuan: 15 — Proyek

Tahun Akademik: 2026/2027 Ganjil


## 1. Judul Proyek

Kalkulator Geometri Bangun Datar Berbasis Python

## 2. Latar Belakang

Matematika merupakan salah satu ilmu yang banyak diterapkan dalam kehidupan sehari-hari. Salah satu materi yang dipelajari dalam matematika adalah geometri, khususnya bangun datar. Dalam materi ini, peserta didik mempelajari berbagai bentuk bangun datar beserta cara menghitung luas dan kelilingnya.

Namun, dalam proses pembelajaran, masih terdapat peserta didik yang mengalami kesulitan dalam mengingat rumus dan melakukan perhitungan luas serta keliling bangun datar. Oleh karena itu, diperlukan sebuah program sederhana yang dapat membantu proses perhitungan secara lebih praktis.

Berdasarkan permasalahan tersebut, dibuat proyek Kalkulator Geometri Bangun Datar menggunakan bahasa pemrograman Python. Program ini dirancang untuk menghitung luas dan keliling beberapa bangun datar serta memberikan hasil perhitungan berdasarkan nilai yang dimasukkan oleh pengguna.

## 3. Identifikasi Masalah

1. Peserta didik terkadang mengalami kesulitan dalam mengingat rumus luas dan keliling bangun datar.
2. Perhitungan secara manual membutuhkan ketelitian agar tidak terjadi kesalahan.
3. Belum semua peserta didik memanfaatkan program sederhana untuk membantu perhitungan matematika.

## 4. Rumusan Masalah

1. Bagaimana merancang program kalkulator geometri menggunakan Python?
2. Bagaimana menerapkan rumus luas dan keliling bangun datar ke dalam program?
3. Bagaimana membuat program yang mudah digunakan dan dapat memvalidasi masukan pengguna?

## 5. Tujuan Proyek

1. Membuat program perhitungan luas dan keliling bangun datar menggunakan Python.
2. Menerapkan konsep matematika ke dalam pemrograman.
3. Membantu pengguna melakukan perhitungan secara praktis.
4. Melatih kemampuan menggunakan fungsi, percabangan, perulangan, dan validasi input dalam Python.

## 6. Manfaat Proyek

1. Membantu pengguna menghitung luas dan keliling bangun datar.
2. Mempermudah pemahaman penerapan rumus geometri.
3. Menjadi sarana pembelajaran pemrograman Python.
4. Mengembangkan kemampuan berpikir logis dan sistematis.

## 7. Fitur Program

Program memiliki beberapa fitur utama, yaitu:

1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Memvalidasi input agar pengguna tidak memasukkan nilai yang tidak sesuai.
6. Menampilkan hasil perhitungan.
7. Menyediakan pilihan untuk melakukan perhitungan kembali.

## 8. Input, Proses, dan Output (IPO)

### A. Input

- Pilihan jenis bangun datar.
- Panjang sisi persegi.
- Panjang dan lebar persegi panjang.
- Alas, tinggi, dan sisi-sisi segitiga.
- Jari-jari lingkaran.

### B. Proses

Program memproses nilai yang dimasukkan pengguna menggunakan rumus matematika sesuai jenis bangun datar.

Rumus yang digunakan:

**Persegi**
- Luas = sisi × sisi
- Keliling = 4 × sisi

**Persegi Panjang**
- Luas = panjang × lebar
- Keliling = 2 × (panjang + lebar)

**Segitiga**
- Luas = ½ × alas × tinggi
- Keliling = sisi a + sisi b + sisi c

**Lingkaran**
- Luas = π × r × r
- Keliling = 2 × π × r

### C. Output

- Jenis bangun datar yang dipilih.
- Hasil perhitungan luas.
- Hasil perhitungan keliling.
- Pesan kesalahan apabila input tidak valid.

## 9. Algoritma Program

1. Mulai program.
2. Menampilkan menu pilihan bangun datar.
3. Pengguna memilih jenis bangun datar.
4. Program meminta pengguna memasukkan nilai yang diperlukan.
5. Program memeriksa validitas input.
6. Program menghitung luas dan keliling berdasarkan rumus.
7. Program menampilkan hasil perhitungan.
8. Program memberikan pilihan untuk mengulangi perhitungan.
9. Program selesai apabila pengguna memilih keluar.

## 10. Pseudocode

```text
START

REPEAT
    Tampilkan menu bangun datar
    Input pilihan pengguna

    IF pilihan = 1 THEN
        Input sisi
        Hitung luas persegi
        Hitung keliling persegi

    ELSE IF pilihan = 2 THEN
        Input panjang dan lebar
        Hitung luas persegi panjang
        Hitung keliling persegi panjang

    ELSE IF pilihan = 3 THEN
        Input alas, tinggi, dan tiga sisi
        Hitung luas segitiga
        Hitung keliling segitiga

    ELSE IF pilihan = 4 THEN
        Input jari-jari
        Hitung luas lingkaran
        Hitung keliling lingkaran

    ELSE
        Tampilkan pesan pilihan tidak valid
    END IF

    Tampilkan hasil perhitungan
    Tanya apakah ingin mengulang

UNTIL pengguna memilih keluar

END
```

## 11. Struktur Program

Struktur folder proyek direncanakan sebagai berikut:

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
├── tests/
│   └── test_case.md
│
└── .gitignore
```

## 12. Rencana Pengujian

| No. | Jenis Pengujian | Tujuan |
|---|---|---|
| 1 | Menghitung luas dan keliling persegi | Memastikan rumus persegi berjalan benar |
| 2 | Menghitung luas dan keliling persegi panjang | Memastikan perhitungan sesuai rumus |
| 3 | Menghitung luas dan keliling segitiga | Memastikan hasil perhitungan benar |
| 4 | Menghitung luas dan keliling lingkaran | Memastikan penggunaan nilai pi benar |
| 5 | Memasukkan nilai negatif | Memastikan validasi input berjalan |
| 6 | Memasukkan pilihan menu yang salah | Memastikan program menangani pilihan tidak valid |

## 13. Teknologi yang Digunakan

1. Bahasa pemrograman Python.
2. Visual Studio Code sebagai editor kode.
3. Git sebagai sistem pengelolaan versi.
4. GitHub sebagai tempat penyimpanan repository proyek.

## 14. Penutup

Proyek Kalkulator Geometri Bangun Datar diharapkan dapat menjadi salah satu bentuk penerapan ilmu matematika ke dalam teknologi pemrograman. Melalui proyek ini, konsep geometri tidak hanya dipelajari secara teori, tetapi juga diterapkan dalam sebuah program yang dapat digunakan untuk membantu perhitungan luas dan keliling bangun datar.

Selain itu, proyek ini menjadi sarana untuk meningkatkan keterampilan dalam menggunakan Python, menyusun algoritma, menerapkan fungsi, serta melakukan pengujian program.
