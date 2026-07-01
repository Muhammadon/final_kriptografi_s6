# ============================================================
# key_space_analysis.py  –  Analisis Ruang Kunci & Kompleksitas
# Tugas Besar Kriptografi – Minggu 3
# ============================================================

import time
import sys
import os
# Memetakan path ke folder minggu_1 agar kelas SandiCaesar bisa diimpor
# Mengasumsikan struktur root/minggu_1 dan root/minggu_3 sejajar
path_minggu_1 = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'minggu_1'))
sys.path.append(path_minggu_1)


try:
    from caesar_cipher import SandiCaesar
except ImportError:
    print("Error: Gagal mengimpor. Pastikan 'caesar_cipher.py' ada di folder 'minggu_1'.")
    sys.exit(1)


class KeySpaceAnalyzer:
    """Kelas untuk menganalisis ruang kunci kriptografi dan mengukur performa brute force."""

    def __init__(self, percobaan_per_detik: float = 1_000_000):
        self.percobaan_per_detik = percobaan_per_detik

    def hitung_ruang_kunci(self, algoritma: str, panjang_kunci: int) -> int:
        """Menghitung total kemungkinan ruang kunci berdasarkan algoritma."""
        if algoritma.lower() == 'caesar':
            return 25
        else:
            return 26 ** panjang_kunci  # 26^L kemungkinan

    def format_estimasi_waktu(self, detik: float) -> str:
        """Mengubah durasi detik menjadi string format waktu yang manusiawi."""
        if detik < 60:
            return f"{detik:.6f} detik"
        elif detik < 3600:
            return f"{detik/60:.2f} menit"
        elif detik < 86400:
            return f"{detik/3600:.2f} jam"
        elif detik < 31_536_000:
            return f"{detik/86400:.2f} hari"
        else:
            return f"{detik/31_536_000:.2e} tahun"

    def analisis_ruang_kunci(self, algoritma: str, panjang_kunci: int) -> None:
        """Menghitung ukuran ruang kunci dan mencetak estimasi waktu brute force."""
        ruang_kunci = self.hitung_ruang_kunci(algoritma, panjang_kunci)
        rata_rata = ruang_kunci / 2
        detik = rata_rata / self.percobaan_per_detik

        print(f'Algoritma          : {algoritma.upper()}')
        print(f'Panjang kunci      : {panjang_kunci} karakter')
        print(f'Ruang kunci        : {ruang_kunci:,} kemungkinan')
        print(f'Rata-rata percobaan: {rata_rata:,.0f}')
        print(f'Estimasi waktu     : {self.format_estimasi_waktu(detik)}')
        print('=' * 52)

    def ukur_waktu_aktual(self, ciphertext: str) -> None:
        """Mengukur waktu nyata yang dibutuhkan untuk brute force Caesar."""
        mulai = time.perf_counter()

        # Looping mencoba kunci dari 1 sampai 25
        for k in range(1, 26):
            # Membuat objek baru untuk setiap kunci baru sesuai kontrak __init__ SandiCaesar
            sandi = SandiCaesar(pesan=ciphertext, kunci=k)
            # Memanggil method dekripsi bawaan dari class SandiCaesar
            _ = sandi.dekripsi()

        selesai = time.perf_counter()

        durasi = selesai - mulai
        kecepatan = 25 / durasi

        print(f'Waktu aktual brute force : {durasi*1000:.4f} ms')
        print(f'Kecepatan aktual         : {kecepatan:,.0f} percobaan/detik')

if __name__ == '__main__':
    # Instansiasi objek analyzer dengan kemampuan 1.000.000 percobaan/detik
    analyzer = KeySpaceAnalyzer(percobaan_per_detik=1_000_000)

    print('ANALISIS RUANG KUNCI & ESTIMASI WAKTU BRUTE FORCE')
    print('=' * 52)

    # Memanggil method analisis dari objek
    analyzer.analisis_ruang_kunci('caesar', 1)
    analyzer.analisis_ruang_kunci('vigenere', 4)
    analyzer.analisis_ruang_kunci('vigenere', 8)
    analyzer.analisis_ruang_kunci('vigenere', 16)

    print('PENGUKURAN WAKTU AKTUAL:')
    analyzer.ukur_waktu_aktual('KHOOR ZRUOG WKLV LV FUBSWR FODVV')
