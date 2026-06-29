#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ============================================================
# brute_force_attack.py – Exhaustive Attack Caesar Cipher
# Tugas Besar Kriptografi – Minggu 2
# ============================================================

import sys
import os

# Memetakan path ke folder minggu_1 agar kelas SandiCaesar bisa diimpor
# Mengasumsikan struktur root/minggu_1 dan root/minggu_2 sejajar
path_minggu_1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'minggu_1'))
sys.path.append(path_minggu_1)

try:
    from caesar_cipher import SandiCaesar
except ImportError:
    print("Error: Gagal mengimpor. Pastikan 'caesar_cipher.py' ada di folder 'minggu_1'.")
    sys.exit(1)

class SeranganBruteForceCaesar:
    def __init__(self, cipherteks: str):
        self.cipherteks = cipherteks
        
        # Kumpulan kata umum untuk deteksi plainteks otomatis
        kata_id = ['DAN', 'YANG', 'INI', 'ITU', 'ATAU', 'ADA', 'UNTUK', 'DARI', 'KE', 'DI', 'DENGAN', 'PADA', 'BELAJAR', 'KITA']
        kata_en = ['THE', 'AND', 'IS', 'IN', 'OF', 'TO', 'A', 'THAT', 'IT', 'FOR', 'THIS', 'WITH', 'HELLO', 'WORLD']
        
        # Menggunakan set untuk pencarian yang lebih cepat
        self.kamus_kata = set(kata_id + kata_en)
        self.kandidat_terbaik = []

    def hitung_skor(self, teks: str) -> int:
        """Menghitung jumlah kata bermakna yang ditemukan dalam teks hasil dekripsi."""
        kata_kata = teks.upper().split()
        return sum(1 for kata in kata_kata if kata in self.kamus_kata)

    def eksekusi_serangan(self):
        """Mengeksekusi exhaustive attack untuk ke-25 kemungkinan kunci Caesar."""
        print(f"{'Kunci':>6} | {'Hasil Dekripsi':<38} | Skor")
        print('-' * 62)
        
        # Mencoba semua 25 probabilitas pergeseran kunci
        for kunci in range(1, 26):
            # Instansiasi objek dari class SandiCaesar (Minggu 1)
            # Kita set cipherteks sebagai input pesan, lalu memanggil metode dekripsi()
            sandi = SandiCaesar(pesan=self.cipherteks, kunci=kunci)
            hasil_dekripsi = sandi.dekripsi()
            
            # Hitung skor kemiripan bahasa
            skor = self.hitung_skor(hasil_dekripsi)
            pratinjau = hasil_dekripsi[:38]
            tanda = ' <-- kandidat!' if skor > 0 else ''
            
            print(f'{kunci:>6} | {pratinjau:<38} | {skor}{tanda}')
            
            if skor > 0:
                self.kandidat_terbaik.append((skor, kunci, hasil_dekripsi))
        
        print()
        self._tampilkan_kandidat_teratas()

    def _tampilkan_kandidat_teratas(self):
        """Metode internal untuk menyortir dan menampilkan hasil dengan skor tertinggi."""
        if self.kandidat_terbaik:
            # Sortir berdasarkan skor tertinggi (indeks 0 dari tuple)
            self.kandidat_terbaik.sort(reverse=True)
            skor_tertinggi, kunci_terbaik, teks_asli = self.kandidat_terbaik[0]
            
            print(f'>>> Kunci terbaik : k = {kunci_terbaik}')
            print(f'>>> Plainteks     : {teks_asli}')
            print(f'>>> Skor          : {skor_tertinggi} kata umum terdeteksi')
        else:
            print('>>> Tidak ada kata umum terdeteksi. Periksa manual.')


# ──────── PENGUJIAN ────────
def main():
    # Menjadikan input dinamis dari terminal, fallback ke teks uji modul jika kosong
    if len(sys.argv) > 1:
        ciphertext_uji = sys.argv[1]
    else:
        # Cipherteks uji 1 sesuai modul praktikum
        ciphertext_uji = 'KHOOR ZRUOG WKLV LV FUBSWR FODVV'
        
    print(f'Cipherteks : {ciphertext_uji}')
    print('Mencoba 25 kemungkinan kunci...\n')
    
    # Instansiasi objek penyerang dan eksekusi
    penyerang = SeranganBruteForceCaesar(ciphertext_uji)
    penyerang.eksekusi_serangan()

if __name__ == '__main__':
    main()

# 1 # ============================================================
# 2 # brute_force_attack.py – Exhaustive Attack Caesar Cipher
# 3 # Tugas Besar Kriptografi – Minggu 2
# 4 # ============================================================

# import sys
# import os

# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# )

# from minggu_1.caesar_cipher import decrypt_caesar

# # Kata-kata umum sebagai referensi deteksi plainteks bermakna
# KATA_UMUM_ID = ['DAN','YANG','INI','ITU','ATAU','ADA','UNTUK','DARI','KE','DI','DENGAN','PADA','BELAJAR','KITA']

# KATA_UMUM_EN = ['THE','AND','IS','IN','OF','TO','A','THAT','IT','FOR','THIS','WITH','HELLO','WORLD']

# SEMUA_KATA = set(KATA_UMUM_ID + KATA_UMUM_EN)

# def skor_teks(teks: str) -> int:
#     """Hitung skor: berapa kata umum ditemukan dalam teks."""
#     kata_kata = teks.upper().split()
#     return sum(1 for w in kata_kata if w in SEMUA_KATA)

# def brute_force_caesar(ciphertext: str) -> None:
#     """Coba semua 25 kemungkinan kunci Caesar Cipher."""
#     print(f"{'Kunci':>6} | {'Hasil Dekripsi':<38} | Skor")
#     print('-' * 62)
#     kandidat_terbaik = []
#     for kunci in range(1, 26):
#         hasil = decrypt_caesar(ciphertext, kunci)
#         skor = skor_teks(hasil)
#         pratinjau = hasil[:38]
#         tanda = ' <-- kandidat!' if skor > 0 else ''
#         print(f'{kunci:>6} | {pratinjau:<38} | {skor}{tanda}')
#         if skor > 0:
#             kandidat_terbaik.append((skor, kunci, hasil))
#     print()
#     if kandidat_terbaik:
#         kandidat_terbaik.sort(reverse=True)
#         skor, k, teks = kandidat_terbaik[0]
#         print(f'>>> Kunci terbaik : k = {k}')
#         print(f'>>> Plainteks : {teks}')
#         print(f'>>> Skor : {skor} kata umum terdeteksi')
#     else:
#         print('>>> Tidak ada kata umum terdeteksi. Periksa manual.')

# # ──────── PENGUJIAN ────────
# if __name__ == '__main__':
#     ciphertext = 'KHOOR ZRUOG WKLV LV FUBSWR FODVV'
#     print(f'Cipherteks : {ciphertext}')
#     print(f'Mencoba 25 kemungkinan kunci...\n')
#     brute_force_caesar(ciphertext)