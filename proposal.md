# PROPOSAL PROYEK
## KALKULATOR GEOMETRI BANGUN DATAR BERBASIS PYTHON

### Identitas Mahasiswa

Nama: Kesya Nur Aprilliani

NIM: 2225250219

Program Studi: Pendidikan Matematika

Kelas: 3E

Mata Kuliah: Algoritma dan Pemrograman

Pertemuan: 14 — Perancangan Proyek

Tahun Akademik: 2026/2027 Ganjil

### 1. Judul Proyek

Kalkulator Geometri Bangun Datar Berbasis Python.

### 2. Latar Belakang

Geometri merupakan salah satu materi matematika yang mempelajari bentuk, ukuran, luas, dan keliling bangun. Dalam mempelajari materi ini, mahasiswa atau siswa terkadang mengalami kesulitan dalam mengingat rumus dan melakukan perhitungan secara tepat.

Perkembangan teknologi dapat dimanfaatkan untuk membantu proses pembelajaran matematika. Salah satu caranya adalah membuat program sederhana menggunakan bahasa pemrograman Python.

Oleh karena itu, dirancang program Kalkulator Geometri Bangun Datar yang dapat membantu pengguna menghitung luas dan keliling beberapa bangun datar secara praktis. Program ini juga dapat digunakan sebagai sarana latihan penerapan rumus matematika dan logika pemrograman.

### 3. Rumusan Masalah

1. Bagaimana merancang program sederhana untuk menghitung luas dan keliling bangun datar?
2. Bagaimana menerapkan rumus matematika ke dalam algoritma Python?
3. Bagaimana memvalidasi masukan agar program tidak memproses ukuran yang tidak sesuai?
4. Bagaimana menguji ketepatan hasil perhitungan program?

### 4. Pengguna dan Tujuan

**Pengguna sasaran:** siswa, mahasiswa, atau pengguna yang sedang mempelajari geometri dasar.

**Tujuan proyek:**

1. Membuat program untuk menghitung luas dan keliling bangun datar.
2. Menerapkan rumus matematika ke dalam program Python.
3. Melatih penggunaan fungsi, percabangan, perulangan, dan validasi input.
4. Menyediakan program yang sederhana dan mudah digunakan.
5. Menguji ketepatan hasil melalui beberapa test case.

### 5. Ruang Lingkup

**Fitur wajib:**

1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Menampilkan hasil perhitungan.
6. Memvalidasi masukan angka agar bernilai positif.
7. Menampilkan pesan kesalahan untuk masukan yang tidak sesuai.
8. Menyediakan menu untuk memilih bangun datar.

**Batasan proyek:**

- Program dijalankan melalui terminal.
- Program menggunakan bahasa Python.
- Perhitungan dibatasi pada empat bangun datar.
- Program tidak menggunakan basis data atau antarmuka grafis.
- Untuk segitiga, luas dihitung menggunakan alas dan tinggi, sedangkan keliling dihitung menggunakan tiga panjang sisi yang valid.

### 6. Kebutuhan Program

**A. Kebutuhan fungsional**

- Program menampilkan menu pilihan bangun datar.
- Program menerima ukuran yang dimasukkan pengguna.
- Program menghitung luas dan keliling berdasarkan rumus.
- Program menampilkan hasil perhitungan.
- Program menolak masukan ukuran yang tidak valid.

**B. Kebutuhan nonfungsional**

- Program mudah dipahami.
- Program memiliki struktur kode yang terorganisasi.
- Program memberikan pesan kesalahan yang jelas.
- Program dapat dijalankan menggunakan Python 3.
- Program dapat diuji dan dikembangkan kembali.

### 7. Input, Proses, dan Output (IPO)

**Input:**
- Pilihan bangun datar.
- Panjang sisi persegi.
- Panjang dan lebar persegi panjang.
- Alas, tinggi, dan panjang sisi segitiga.
- Jari-jari lingkaran.

**Proses:**
- Memeriksa pilihan pengguna.
- Memvalidasi ukuran yang dimasukkan.
- Menghitung luas dan keliling berdasarkan rumus.
- Menangani masukan yang tidak valid.

**Output:**
- Nama bangun datar.
- Nilai luas.
- Nilai keliling.
- Pesan kesalahan apabila masukan tidak sesuai.

### 8. Rumus Matematika

**Persegi**

Luas = sisi × sisi

Keliling = 4 × sisi

**Persegi panjang**

Luas = panjang × lebar

Keliling = 2 × (panjang + lebar)

**Segitiga**

Luas = ½ × alas × tinggi

Keliling = sisi 1 + sisi 2 + sisi 3

**Lingkaran**

Luas = π × jari-jari × jari-jari

Keliling = 2 × π × jari-jari

### 9. Algoritma atau Pseudocode

MULAI

1. Tampilkan menu bangun datar.
2. Minta pengguna memilih bangun datar.
3. Jika pilihan adalah persegi:
   - Masukkan panjang sisi.
   - Validasi panjang sisi.
   - Hitung luas dan keliling.
4. Jika pilihan adalah persegi panjang:
   - Masukkan panjang dan lebar.
   - Validasi kedua ukuran.
   - Hitung luas dan keliling.
5. Jika pilihan adalah segitiga:
   - Masukkan alas, tinggi, dan tiga panjang sisi.
   - Validasi semua ukuran.
   - Periksa apakah tiga sisi dapat membentuk segitiga.
   - Hitung luas dan keliling.
6. Jika pilihan adalah lingkaran:
   - Masukkan jari-jari.
   - Validasi jari-jari.
   - Hitung luas dan keliling.
7. Tampilkan hasil perhitungan.
8. Jika input tidak valid, tampilkan pesan kesalahan.
9. Sediakan pilihan untuk kembali ke menu atau keluar.

SELESAI

### 10. Rancangan Struktur Program

- `main.py`: mengatur menu, input pengguna, dan tampilan hasil.
- `src/kalkulator_geometri.py`: menyimpan fungsi perhitungan dan validasi.
- `tests/test_case.md`: mencatat rencana pengujian beserta hasilnya.
- `proposal.md`: menyimpan rancangan proyek.
- `README.md`: menjelaskan tujuan, struktur, dan cara penggunaan proyek.
- `.gitignore`: menentukan berkas yang tidak perlu dimasukkan ke Git.

### 11. Rancangan Struktur Data

Program menggunakan beberapa jenis data:

- `int` atau `float` untuk menyimpan ukuran bangun datar.
- `str` untuk menyimpan pilihan menu dan pesan.
- `float` untuk menyimpan hasil perhitungan yang memungkinkan bilangan desimal.
- Fungsi untuk memisahkan setiap proses perhitungan agar kode lebih mudah diuji.

### 12. Rencana Test Case

| Kode | Kondisi yang Diuji | Input Contoh | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Persegi normal | Sisi = 4 | Luas 16 dan keliling 16 |
| TC02 | Persegi panjang normal | Panjang = 8, lebar = 5 | Luas 40 dan keliling 26 |
| TC03 | Segitiga normal | Alas = 6, tinggi = 4, sisi = 5, 5, 6 | Luas 12 dan keliling 16 |
| TC04 | Lingkaran normal | Jari-jari = 7 | Luas sekitar 153,94 dan keliling sekitar 43,98 |
| TC05 | Ukuran nol | Sisi = 0 | Program menolak ukuran |
| TC06 | Ukuran negatif | Jari-jari = -3 | Program menolak ukuran |
| TC07 | Input bukan angka | Sisi = abc | Program menampilkan pesan kesalahan |
| TC08 | Sisi segitiga tidak valid | Sisi = 1, 2, 5 | Program menolak segitiga |
| TC09 | Pilihan menu tidak tersedia | Pilihan = 9 | Program menampilkan pesan pilihan tidak valid |
| TC10 | Keluar dari program | Pilihan = 0 | Program berhenti dengan baik |

Catatan: TC01–TC10 merupakan rencana pengujian. Status keberhasilan baru dicatat setelah masing-masing kasus dijalankan pada program.

### 13. Pembagian Tugas dan Jadwal

Proyek ini dikerjakan secara individu. Pembagian peran berikut merupakan pembagian tahapan pekerjaan, bukan pembagian kepada anggota kelompok.

- Perancang: menentukan masalah, tujuan, dan ruang lingkup.
- Analis: menyusun IPO, rumus, dan pseudocode.
- Programmer: menyiapkan struktur modul dan implementasi.
- Tester: menyusun serta menjalankan test case.
- Dokumentator: menyusun README dan mencatat hasil pengujian.

**Jadwal pengerjaan:**

- Pertemuan 14: menyusun proposal, pseudocode, struktur folder, dan rencana test case.
- Antara Pertemuan 14 dan 15: menyiapkan kebutuhan implementasi.
- Pertemuan 15: mengimplementasikan program, melakukan pengujian, debugging, dan melengkapi dokumentasi.
- Pertemuan 16: menyiapkan demonstrasi dan evaluasi proyek sesuai arahan dosen.

### 14. Rencana Repositori

Nama repositori GitHub:

`Pertemuan_15_Proyek_2225250219`

Repositori digunakan untuk menyimpan proposal, struktur program, README, dan riwayat perubahan menggunakan Git.

URL repositori: https://github.com/Kesyaapril13/Pertemuan_15_Proyek_2225250219

### 15. Penutup

Rancangan proyek Kalkulator Geometri Bangun Datar disusun sebagai dasar pembuatan program matematika sederhana menggunakan Python. Rancangan ini mencakup kebutuhan pengguna, fitur, rumus, IPO, pseudocode, struktur program, dan rencana pengujian. Seluruh bagian tersebut akan menjadi acuan pada tahap implementasi, pengujian, dan dokumentasi berikutnya.
