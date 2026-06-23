1 # ============================================================
2 # brute_force_attack.py – Exhaustive Attack Caesar Cipher
3 # Tugas Besar Kriptografi – Minggu 2
4 # ============================================================
# from minggu_2.caesar_cipher import decrypt_caesar
from minggu_1.caesar_cipher import decrypt_caesar

# Kata-kata umum sebagai referensi deteksi plainteks bermakna
KATA_UMUM_ID = ['DAN','YANG','INI','ITU','ATAU','ADA','UNTUK','DARI','KE','DI','DENGAN','PADA','BELAJAR','KITA']

KATA_UMUM_EN = ['THE','AND','IS','IN','OF','TO','A','THAT','IT','FOR','THIS','WITH','HELLO','WORLD']

SEMUA_KATA = set(KATA_UMUM_ID + KATA_UMUM_EN)

def skor_teks(teks: str) -> int:
    """Hitung skor: berapa kata umum ditemukan dalam teks."""
    kata_kata = teks.upper().split()
    return sum(1 for w in kata_kata if w in SEMUA_KATA)

def brute_force_caesar(ciphertext: str) -> None:
    """Coba semua 25 kemungkinan kunci Caesar Cipher."""
    print(f"{'Kunci':>6} | {'Hasil Dekripsi':<38} | Skor")
    print('-' * 62)
    kandidat_terbaik = []
    for kunci in range(1, 26):
        hasil = decrypt_caesar(ciphertext, kunci)
        skor = skor_teks(hasil)
        pratinjau = hasil[:38]
        tanda = ' <-- kandidat!' if skor > 0 else ''
        print(f'{kunci:>6} | {pratinjau:<38} | {skor}{tanda}')
        if skor > 0:
            kandidat_terbaik.append((skor, kunci, hasil))
    print()
    if kandidat_terbaik:
        kandidat_terbaik.sort(reverse=True)
        skor, k, teks = kandidat_terbaik[0]
        print(f'>>> Kunci terbaik : k = {k}')
        print(f'>>> Plainteks : {teks}')
        print(f'>>> Skor : {skor} kata umum terdeteksi')
    else:
        print('>>> Tidak ada kata umum terdeteksi. Periksa manual.')

# ──────── PENGUJIAN ────────
if __name__ == '__main__':
    ciphertext = 'KHOOR ZRUOG WKLV LV FUBSWR FODVV'
    print(f'Cipherteks : {ciphertext}')
    print(f'Mencoba 25 kemungkinan kunci...\n')
    brute_force_caesar(ciphertext)