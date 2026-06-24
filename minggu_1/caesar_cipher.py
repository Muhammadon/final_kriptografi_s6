#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mengimport modul sys untuk mengambil argumen dari command line
import sys  # Output: (Menyediakan fungsi sistem)

# Membuat kelas bernama Caesar untuk enkripsi dan dekripsi


# Reference : https://github.com/juliogarciape/caesar-cipher/blob/main/caesar.py
import sys

class SandiCaesar():
    # Inisialisasi objek baru dan menyiapkan variabel awal
    def __init__(self, pesan, kunci=3):
        # Mengubah semua huruf teks input menjadi huruf kecil untuk proses internal
        self.pesan_input = pesan.lower()
        self.original_raw = pesan # Menyimpan bentuk asli (untuk case matching jika perlu)

        # Menyimpan daftar susunan huruf alfabet dari a sampai z
        self.alfabet_asli = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Menentukan jarak pergeseran huruf (kunci Caesar)
        self.pergeseran_caesar = kunci

    def enkripsi(self):
        """ Fungsi untuk menyandikan / mengenkripsi teks """
        pesan_output = ""
        # Melakukan perulangan untuk setiap karakter dalam teks input
        for karakter in self.pesan_input:
            if karakter in self.alfabet_asli:
                posisi = self.alfabet_asli.index(karakter)
                # Menambahkan indeks dengan nilai geser untuk enkripsi
                pesan_output += self.alfabet_asli[(posisi + self.pergeseran_caesar) % 26]
            else:
                pesan_output += karakter
        return pesan_output.upper()

    def dekripsi(self, cipher_text=None):
        """Fungsi untuk memecahkan sandi / mendekripsi teks """
        # Jika ada cipher_text eksternal yang dimasukkan (untuk verifikasi)
        teks_sumber = cipher_text.lower() if cipher_text else self.pesan_input
        
        pesan_output = ""
        for karakter in teks_sumber:
            if karakter in self.alfabet_asli:
                posisi = self.alfabet_asli.index(karakter)
                # Mengurangi indeks dengan nilai geser untuk dekripsi
                pesan_output += self.alfabet_asli[(posisi - self.pergeseran_caesar) % 26]
            else:
                pesan_output += karakter
        return pesan_output.upper()
    
    def verif(self, plaintext: str) -> bool: 
        """ Memverifikasi apakah hasil dekripsi dari cipherteks kembali ke plainteks semula """
        cipher = self.enkripsi()
        decrypted = self.dekripsi(cipher)
        return decrypted.upper() == plaintext.upper()


# ============================================================
#                --- START FUNGSI JEBATAN ---
# ============================================================
def decrypt_caesar(ciphertext: str, key: int) -> str:
    """ Wrapper untuk menyambungkan brute_force_attack.py ke OOP SandiCaesar """
    # Instansiasi objek menggunakan teks sandi dan kunci
    sandi_obj = SandiCaesar(pesan=ciphertext, kunci=key)
    # Panggil method dekripsi dari class Anda
    return sandi_obj.dekripsi()
# ============================================================
#                --- END FUNGSI JEBATAN ---
# ============================================================

# Fungsi utama untuk mengatur alur jalannya program
def main():
    # Memulai blok penanganan error untuk mengantisipasi kesalahan input
    try:
        # Mengambil argumen dari terminal
        # Penggunaan: python nama_file.py "PESAN" [kunci]
        # Contoh: python nama_file.py "KRIPTOGRAFI" 3
        # Contoh: python nama_file.py "HELLO WORLD" 7
        
        pesan = sys.argv[1]
        
        # Jika kunci tidak diberikan di terminal, defaultnya adalah 3
        kunci = int(sys.argv[2]) if len(sys.argv) > 2 else 3

        # Membuat objek dari kelas SandiCaesar
        sandi = SandiCaesar(pesan, kunci)

        # Proses Enkripsi & Dekripsi untuk Output
        cipherteks = sandi.enkripsi()
        dekripsi_hasil = sandi.dekripsi(cipherteks)
        
        # Verifikasi proses
        is_lulus = sandi.verif(pesan)
        status_verifikasi = "LULUS" if is_lulus else "GAGAL"

        # Output yang rapi dan sesuai permintaan
        print(f"Plainteks   : {pesan.upper()}")
        print(f"Kunci       : {kunci}")
        print(f"Cipherteks  : {cipherteks}")
        print(f"Dekripsi    : {dekripsi_hasil}")
        print(f"Verifikasi  : {status_verifikasi}")
        print("--------------------------------------------------")

    # Blok yang akan berjalan jika terjadi error (misal kekurangan argumen input)
    except IndexError:
        print("-> Argumen kurang. Penggunaan: python nama_file.py \"PESAN\" [KUNCI]")
    except ValueError:
        print("-> Kunci harus berupa angka/integer!")

# Memastikan fungsi utama hanya berjalan jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()   
