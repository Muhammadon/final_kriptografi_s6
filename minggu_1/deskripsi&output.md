=========================================
# Daftar Output yang Wajib Disiapkan:
=========================================

====================================================================
### Harus menghasilkan empat komponen utama di akhir minggu pertama:
====================================================================

## 1. Source Code: Dua file program Python, yaitu caesar_cipher.py dan vigenere_cipher.py.  
## 2. Flowchart: Diagram alur (dalam format PDF atau gambar) untuk minimal satu fungsi enkripsi, contohnya algoritma Caesar Cipher.
## 3. Screenshot Pengujian: Bukti tangkapan layar dari terminal atau console yang menunjukkan bahwa program berhasil menjalankan 4 kasus uji wajib secara tepat.
## 4. Analisis Tertulis: Penjelasan singkat (sekitar setengah halaman) yang menguraikan bagaimana konsep aritmetika modulo diterapkan di dalam kode program. 

(Catatan: Draf untuk teks ini sudah saya siapkan di dokumen panduan pada poin 4).

=========================
# 1. Landasan Teori & Konsep Dasar Matematika
=========================

Memahami aspek matematika di balik algoritma kriptografi klasik sangat krusial agar tidak terjadi logical error saat proses coding.

=========================

## Aritmetika Modulo (Clock Arithmetic)

Inti dari kriptografi klasik adalah operasi modulo. Dalam alfabet 26 huruf (A-Z), posisi huruf dipetakan menjadi nilai numerik 0-25. Rumus dasar modulo dalam enkripsi menggeser nilai karakter, lalu membaginya dengan 26 dan mengambil sisa pembagiannya. Hal ini memastikan pergeseran bersifat siklikal (kembali ke 'A' setelah 'Z').

==========================

## Sifat Invers Modulo untuk Dekripsi

Dekripsi merupakan proses kebalikan. Jika enkripsi Caesar adalah C = (P + k) mod 26, maka untuk
mengembalikan cipherteks menjadi plainteks, kita menggesernya ke arah sebaliknya. Untuk mencegah
nilai negatif di Python, kita menambahkan kelipatan 26, sehingga rumusnya menjadi P = (C - k + 26)
mod 26.

=========================
# 2. Bedah Logika & Referensi Kode Python
=========================

Sesuai instruksi, kita harus membuat kode modular. Berikut adalah arsitektur bersih untuk file yang
ditagihkan di Minggu 1.

=======================
# A. Caesar Cipher (caesar_cipher.py)

Sesuai instruksi, kita harus membuat kode modular. Berikut adalah arsitektur bersih untuk file yang
ditagihkan di Minggu 1.

# B. Vigenere Cipher (vigenere_cipher.py)

Vigenere membutuhkan fungsi tambahan untuk mengulang (wrapping) kata kunci agar sejajar dengan
panjang huruf di plainteks, dengan tetap mengabaikan spasi.

# 3. Matriks Hasil Kasus Uji Wajib

Berikut adalah target keluaran (expected output) untuk 4 kasus uji yang diwajibkan oleh modul untuk
pengujian QA dan screenshot:

No Plainteks Algoritma Kunci Cipherteks Diharapkan

1 KRIPTOGRAFI     Caesar Cipher 3 NULSWRJUDIL
2 HELLO WORLD     Caesar Cipher 7 OLSSV DVYSK
3 HALO DUNIA      Vigenere Cipher KUNCI RUNY XIIIA
4 SELAMAT PAGI    Vigenere Cipher UIN MMYUUNN XNAQ

===============
# 4. Draf Analisis Modulo (Untuk Laporan Akhir)
===============


Aritmetika modulo merupakan fondasi utama yang menjamin keandalan fungsional sistem kriptografi
klasik. Ruang karakter alfabet dibatasi secara sirkular pada 26 elemen (indeks 0 hingga 25). Operasi
modulo (seperti pembagian sisa % di Python) menormalisasi hasil penjumlahan antara nilai plainteks
dan kunci untuk mencegah terjadinya overflow yang menghasilkan karakter di luar set alfabet.
Sifat deterministik matematika modulo memungkinkan operasi ini diputar balik dengan sempurna
(inversi). Defleksi akibat pengurangan kunci yang berujung pada nilai negatif dapat diatasi secara
matematis dengan menjumlahkan rentang modulus (ditambah 26) sebelum operasi sisa, sehingga (C - k
+ 26) mod 26 memastikan nilai selalu positif. Logika aljabar linier pada ring (gelanggang) bilangan bulat
inilah yang memungkinkan integritas properti D(E(P)) = P selalu terbukti benar di setiap iterasi.