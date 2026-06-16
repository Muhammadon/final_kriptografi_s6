#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mengimport modul sys untuk mengambil argumen dari command line
import sys  # Output: (Menyediakan fungsi sistem)

# Membuat kelas bernama Caesar untuk enkripsi dan dekripsi


# Reference : https://github.com/juliogarciape/caesar-cipher/blob/main/caesar.py

class SandiCaesar():
    # Inisialisasi objek baru dan menyiapkan variabel awal
    def __init__(self, pesan):
        # Mengubah semua huruf teks input menjadi huruf kecil
        self.pesan_input = pesan.lower()

        # Menyimpan daftar susunan huruf alfabet dari a sampai z
        self.alfabet_asli = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Menentukan jarak pergeseran huruf (kunci Caesar) sebesar 3 posisi
        self.pergeseran_caesar = 3

        # Menyiapkan string kosong untuk menampung teks hasil akhir
        self.pesan_output = ""

    def dekripsi(self):
        """Fungsi untuk memecahkan sandi / mendekripsi teks """
        # Melakukan perulangan untuk setiap karakter dalam teks input
        for karakter in self.pesan_input:
            # Memeriksa apakah karakter ada di dalam daftar alfabet asli
            if karakter in self.alfabet_asli:
                # Mencari posisi indeks karakter saat ini di dalam alfabet
                posisi = self.alfabet_asli.index(karakter)
                # Mengurangi indeks dengan nilai geser untuk mengambil huruf sebelumnya (dekripsi)
                self.pesan_output += self.alfabet_asli[(
                    posisi - self.pergeseran_caesar) % 26]
            # Jika karakter berupa angka, spasi, atau simbol, jangan diubah
            else:
                # Memasukkan karakter asli langsung ke teks hasil akhir
                self.pesan_output += karakter

        # Menampilkan teks hasil dekripsi ke layar terminal
        print("> Hasil dekripsi:", self.pesan_output)

    def enkripsi(self):
        """ Fungsi untuk menyandikan / mengenkripsi teks """
        # Melakukan perulangan untuk setiap karakter dalam teks input
        for karakter in self.pesan_input:
            # Memeriksa apakah karakter ada di dalam daftar alfabet asli
            if karakter in self.alfabet_asli:
                # Mencari posisi indeks karakter saat ini di dalam alfabet
                posisi = self.alfabet_asli.index(karakter)
                # Menambahkan indeks dengan nilai geser (+3) untuk mengambil huruf setelahnya (enkripsi)
                self.pesan_output += self.alfabet_asli[(
                    posisi + self.pergeseran_caesar) % 26]
            # Jika karakter berupa angka, spasi, atau simbol, jangan diubah
            else:
                # Memasukkan karakter asli langsung ke teks hasil akhir
                self.pesan_output += karakter

        # Menampilkan teks hasil enkripsi ke layar terminal
        print("> Hasil enkripsi:", self.pesan_output)

# Fungsi utama untuk mengatur alur jalannya program


def main():
    # Memulai blok penanganan error untuk mengantisipasi kesalahan input
    try:
        # Mengambil argumen penanda perintah dari terminal (indeks ke-1)
        penanda = sys.argv[1]

        # Mengambil argumen pesan yang akan diproses dari terminal (indeks ke-2)
        pesan = sys.argv[2]

        # Membuat objek dari kelas SandiCaesar dengan memasukkan variabel pesan
        sandi = SandiCaesar(pesan)

        # Memeriksa apakah penanda bernilai "-c" (artinya perintah enkripsi)
        if penanda == "-c":
            sandi.enkripsi()

        # Memeriksa apakah penanda bernilai "-d" (artinya perintah dekripsi)
        elif penanda == "-d":
            sandi.dekripsi()

        # Jika penanda yang dimasukkan bukan "-c" ataupun "-d"
        else:
            print("> Penanda %s ini tidak valid " % (penanda))

    # Blok yang akan berjalan jika terjadi error (misal kekurangan argumen input)
    except IndexError:
        print(
            "-> Argumen salah / kurang. Penggunaan: python nama_file.py [-c/-d] \"pesan\"")


# Memastikan fungsi utama hanya berjalan jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
