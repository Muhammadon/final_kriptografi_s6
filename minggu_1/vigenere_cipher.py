
"""
Sandi Vigenere adalah salah satu sandi paling sederhana yang menggunakan bentuk substitusi polialfabetik (setiap huruf diberi lebih dari satu pengganti).
Sandi ini pertama kali dijelaskan pada tahun 1553, tetapi membutuhkan waktu hingga tiga abad penuh untuk dapat dipecahkan pada tahun 1863.
Kelemahan: Jika seseorang berhasil menemukan panjang kunci, maka sandi ini dapat dipecahkan.
Diprogram oleh Aladdin Persson <aladdin.persson at hotmail dot com>

* 07-11-2019 Pemrograman awal
"""
import sys


# Reference : https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py 
class VigenereCipher:
    def __init__(self, kunci: str):
        # Inisialisasi properti dasar cipher
        self.kunci = kunci.lower()
        self.alfabet = "abcdefghijklmnopqrstuvwxyz "
        
        # Membuat dictionary mapping menggunakan list comprehension / zip
        self.huruf_ke_indeks = {huruf: indeks for indeks, huruf in enumerate(self.alfabet)}
        self.indeks_ke_huruf = {indeks: huruf for indeks, huruf in enumerate(self.alfabet)}

    def buat_kunci_ulang(self, pesan: str) -> str:
        """Fungsi pembantu untuk mengulang kunci sepanjang teks pesan asli"""
        kunci_ulang = ""
        for i in range(len(pesan)):
            kunci_ulang += self.kunci[i % len(self.kunci)]
        return kunci_ulang

    def enkripsi(self, pesan: str) -> str:
        pesan = pesan.lower()
        terenkripsi = ""
        
        # Memotong pesan berdasarkan panjang kunci
        potongan_pesan = [
            pesan[i: i + len(self.kunci)] for i in range(0, len(pesan), len(self.kunci))
        ]

        for setiap_potongan in potongan_pesan:
            for i, huruf in enumerate(setiap_potongan):
                if huruf in self.huruf_ke_indeks:
                    # Rumus Enkripsi: (P + K) % mod
                    angka = (self.huruf_ke_indeks[huruf] + self.huruf_ke_indeks[self.kunci[i]]) % len(self.alfabet)
                    terenkripsi += self.indeks_ke_huruf[angka]
                else:
                    terenkripsi += huruf

        return terenkripsi

    def dekripsi(self, sandi: str) -> str:
        sandi = sandi.lower()
        terdekripsi = ""
        
        potongan_sandi = [
            sandi[i: i + len(self.kunci)] for i in range(0, len(sandi), len(self.kunci))
        ]

        for setiap_potongan in potongan_sandi:
            for i, huruf in enumerate(setiap_potongan):
                if huruf in self.huruf_ke_indeks:
                    # Rumus Dekripsi: (C - K) % mod
                    angka = (self.huruf_ke_indeks[huruf] - self.huruf_ke_indeks[self.kunci[i]]) % len(self.alfabet)
                    terdekripsi += self.indeks_ke_huruf[angka]
                else:
                    terdekripsi += huruf

        return terdekripsi


# Fungsi utama untuk menjalankan simulasi objek
def main():
    pesan = "SELAMAT PAGI"
    kunci = "UIN"
    
    # 1. Instansiasi Objek Cipher dengan menyuntikkan Kunci
    cipher = VigenereCipher(kunci)
    
    # 2. Memanggil metode-metode objek
    kunci_berulang = cipher.buat_kunci_ulang(pesan)
    pesan_terenkripsi = cipher.enkripsi(pesan)
    pesan_terdekripsi = cipher.dekripsi(pesan_terenkripsi)
    
    # Validasi kecocokan
    is_match = pesan_terdekripsi.upper() == pesan.upper()

    # Menampilkan output
    print(f"Plainteks   : {pesan.upper()}")
    print(f"Kunci       : {kunci.upper()}")
    print(f"Kunci ulang : {kunci_berulang.upper()}")
    print(f"Cipherteks  : {pesan_terenkripsi.upper()}")
    print(f"Dekripsi    : {pesan_terdekripsi.upper()}")
    print(f"Match       : {is_match}")


if __name__ == "__main__":
    main()
