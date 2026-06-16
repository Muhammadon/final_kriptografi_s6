
"""
Sandi Vigenere adalah salah satu sandi paling sederhana yang menggunakan bentuk substitusi polialfabetik (setiap huruf diberi lebih dari satu pengganti).
Sandi ini pertama kali dijelaskan pada tahun 1553, tetapi membutuhkan waktu hingga tiga abad penuh untuk dapat dipecahkan pada tahun 1863.
Kelemahan: Jika seseorang berhasil menemukan panjang kunci, maka sandi ini dapat dipecahkan.
Diprogram oleh Aladdin Persson <aladdin.persson at hotmail dot com>

* 07-11-2019 Pemrograman awal
"""
import sys

# Karakter alfabet menyertakan spasi di ujungnya sesuai kode Anda
alfabet = "abcdefghijklmnopqrstuvwxyz "

# Membuat dictionary untuk memetakan setiap huruf ke indeks angka (a:0, b:1, dst)
huruf_ke_indeks = dict(zip(alfabet, range(len(alfabet))))
# Membuat dictionary kebalikannya untuk memetakan indeks angka ke huruf kembali
indeks_ke_huruf = dict(zip(range(len(alfabet)), alfabet))


def buat_kunci_ulang(pesan, kunci):
    """Fungsi pembantu untuk mengulang kunci sepanjang teks pesan asli"""
    kunci_ulang = ""
    index_kunci = 0
    for karakter in pesan:
        # Mengambil karakter kunci secara berulang (kondisional perulangan muter)
        kunci_ulang += kunci[index_kunci % len(kunci)]
        index_kunci += 1
    return kunci_ulang


def enkripsi(pesan, kunci):
    # Menghindari error case (diubah ke lowercase agar cocok dengan dict alfabet)
    pesan = pesan.lower()
    kunci = kunci.lower()
    
    terenkripsi = ""
    potongan_pesan = [
        pesan[i: i + len(kunci)] for i in range(0, len(pesan), len(kunci))
    ]

    for setiap_potongan in potongan_pesan:
        i = 0
        for huruf in setiap_potongan:
            if huruf in huruf_ke_indeks:
                angka = (huruf_ke_indeks[huruf] + huruf_ke_indeks[kunci[i]]) % len(alfabet)
                terenkripsi += indeks_ke_huruf[angka]
            else:
                # Jika karakter tidak terdaftar di alfabet, biarkan utuh
                terenkripsi += huruf
            i += 1

    return terenkripsi


def dekripsi(sandi, kunci):
    sandi = sandi.lower()
    kunci = kunci.lower()
    
    terdekripsi = ""
    potongan_sandi = [
        sandi[i: i + len(kunci)] for i in range(0, len(sandi), len(kunci))
    ]

    for setiap_potongan in potongan_sandi:
        i = 0
        for huruf in setiap_potongan:
            if huruf in huruf_ke_indeks:
                angka = (huruf_ke_indeks[huruf] - huruf_ke_indeks[kunci[i]]) % len(alfabet)
                terdekripsi += indeks_ke_huruf[angka]
            else:
                terdekripsi += huruf
            i += 1

    return terdekripsi


# Fungsi utama untuk menjalankan alur program simulasi
def main():
    # Menentukan string kalimat asli dan kunci sesuai contoh output permintaan Anda
    pesan = "HALO DUNIA KRIPTOGRAFI"
    kunci = "KUNCI"
    
    # Membuat representasi kunci berulang
    kunci_berulang = buat_kunci_ulang(pesan, kunci)
    
    # Memproses Enkripsi & Dekripsi
    pesan_terenkripsi = enkripsi(pesan, kunci)
    pesan_terdekripsi = dekripsi(pesan_terenkripsi, kunci)
    
    # Validasi Kecocokan (Case-Insensitive untuk berjaga-jaga)
    is_match = pesan_terdekripsi.upper() == pesan.upper()

    # Menampilkan output dengan format persis seperti yang Anda minta
    print(f"Plainteks   : {pesan.upper()}")
    print(f"Kunci       : {kunci.upper()}")
    print(f"Kunci ulang : {kunci_berulang.upper()}")
    print(f"Cipherteks  : {pesan_terenkripsi.upper()}")
    print(f"Dekripsi    : {pesan_terdekripsi.upper()}")
    print(f"Match       : {is_match}")


if __name__ == "__main__":
    main()
