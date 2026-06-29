#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ============================================================
# frequency_analysis.py – Analisis Frekuensi (Analytical Attack)
# Tugas Besar Kriptografi – Minggu 2
# ============================================================

import sys
import os
from collections import Counter

# Memetakan path ke folder minggu_1 agar kelas SandiCaesar bisa diimpor
path_minggu_1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'minggu_1'))
sys.path.append(path_minggu_1)

try:
    from caesar_cipher import SandiCaesar
except ImportError:
    print("Error: Gagal mengimpor. Pastikan 'caesar_cipher.py' ada di folder 'minggu_1'.")
    sys.exit(1)


class AnalisisFrekuensiCaesar:
    def __init__(self, cipherteks: str):
        self.cipherteks = cipherteks
        self.frekuensi_huruf = {}
        # Huruf paling sering dalam bahasa Inggris (urutan frekuensi)
        self.frekuensi_en = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

    def hitung_frekuensi(self) -> None:
        """Menghitung persentase kemunculan setiap huruf dalam teks."""
        huruf_huruf = [c for c in self.cipherteks.upper() if c.isalpha()]
        total = len(huruf_huruf)
        
        if total == 0:
            self.frekuensi_huruf = {}
            return
            
        counter = Counter(huruf_huruf)
        self.frekuensi_huruf = {h: (n / total * 100) for h, n in counter.most_common()}

    def tampilkan_grafik_frekuensi(self) -> None:
        """Menampilkan grafik batang sederhana di terminal."""
        print('Distribusi Frekuensi Huruf Cipherteks:')
        print('-' * 45)
        # Menampilkan top 10 huruf teratas
        for huruf, pct in list(self.frekuensi_huruf.items())[:10]:
            bar = '█' * int(pct * 1.5)  # skala visual batang
            print(f' {huruf}: {pct:5.1f}% {bar}')
            print('-' * 45)
        print()

    def eksekusi_serangan(self, top_n: int = 3) -> None:
        """
        Mengeksekusi serangan analisis frekuensi.
        Asumsi: huruf paling sering dalam cipherteks ≈ huruf 'E' di plainteks.
        """
        self.hitung_frekuensi()
        
        if not self.frekuensi_huruf:
            print("Teks tidak mengandung karakter alfabet yang valid.")
            return

        self.tampilkan_grafik_frekuensi()
        
        huruf_terbanyak = list(self.frekuensi_huruf.keys())[:top_n]
        print(f'Top {top_n} huruf kandidat: {huruf_terbanyak}')
        print('Mencoba setiap huruf sebagai padanan E...')
        print('-' * 55)
        
        for cipher_char in huruf_terbanyak:
            # k = (posisi huruf cipher - posisi E + 26) mod 26
            k = (ord(cipher_char) - ord('E') + 26) % 26
            
            # Memanggil objek dari class minggu 1
            sandi = SandiCaesar(pesan=self.cipherteks, kunci=k)
            hasil = sandi.dekripsi()
            
            # Indentasi ini sudah diperbaiki (masuk ke dalam loop)
            print(f' Jika {cipher_char} = E --> k={k:<2} --> {hasil[:42]}...')


# ──────── PENGUJIAN ────────
def main():
    # Mendukung input teks dinamis dari argumen terminal
    if len(sys.argv) > 1:
        ciphertext_uji = sys.argv[1]
    else:
        # Cipherteks uji 1 sesuai modul
        ciphertext_uji = ('KHOOR ZRUOG WKLV LV FUBSWR FODVV '
                          'ZH DUH OHDUQLQJ DERXW FUBSWRJUDSKB')
        
    print(f'Cipherteks:\n{ciphertext_uji}\n')
    
    # Instansiasi objek analisis dan eksekusi
    analis = AnalisisFrekuensiCaesar(ciphertext_uji)
    analis.eksekusi_serangan()

if __name__ == '__main__':
    main()