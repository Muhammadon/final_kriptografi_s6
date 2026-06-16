
"""
Sandi Vigenere adalah salah satu sandi paling sederhana yang menggunakan bentuk substitusi polialfabetik (setiap huruf diberi lebih dari satu pengganti).
Sandi ini pertama kali dijelaskan pada tahun 1553, tetapi membutuhkan waktu hingga tiga abad penuh untuk dapat dipecahkan pada tahun 1863.
Kelemahan: Jika seseorang berhasil menemukan panjang kunci, maka sandi ini dapat dipecahkan.
Diprogram oleh Aladdin Persson <aladdin.persson at hotmail dot com>

* 07-11-2019 Pemrograman awal
"""

# Referecence : https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py

# Menentukan daftar karakter alfabet yang didukung, termasuk karakter spasi di akhir string
alfabet = "abcdefghijklmnopqrstuvwxyz "

# Membuat dictionary untuk memetakan setiap huruf ke indeks angka (a:0, b:1, c:2, dst)
huruf_ke_indeks = dict(zip(alfabet, range(len(alfabet))))
# Membuat dictionary kebalikannya untuk memetakan indeks angka ke huruf kembali (0:a, 1:b, 2:c, dst)
indeks_ke_huruf = dict(zip(range(len(alfabet)), alfabet))


# Fungsi untuk mengubah teks biasa menjadi teks rahasia (enkripsi)
def enkripsi(pesan, kunci):
    # Menyiapkan variabel string kosong untuk menampung hasil enkripsi
    terenkripsi = ""
    # Memotong teks input menjadi beberapa bagian sepanjang ukuran string kunci
    potongan_pesan = [
        pesan[i: i + len(kunci)] for i in range(0, len(pesan), len(kunci))
    ]

    # Melakukan perulangan untuk setiap potongan teks yang sudah dibagi
    for setiap_potongan in potongan_pesan:
        # Menginisialisasi ulang indeks penunjuk karakter kunci dari angka 0
        i = 0
        # Melakukan perulangan untuk mengambil setiap huruf di dalam satu potongan teks
        for huruf in setiap_potongan:
            # Rumus matematika enkripsi Vigenere: (Indeks Huruf Pesan + Indeks Huruf Kunci) % 27
            angka = (huruf_ke_indeks[huruf] +
                     huruf_ke_indeks[kunci[i]]) % len(alfabet)
            # Mengubah angka hasil rumus kembali menjadi huruf dan menambahkannya ke variabel hasil
            terenkripsi += indeks_ke_huruf[angka]
            # Menaikkan indeks penunjuk karakter kunci agar bergeser ke huruf kunci berikutnya
            i += 1

    # Mengembalikan string teks rahasia utuh hasil enkripsi ke pemanggil fungsi
    return terenkripsi


# Fungsi untuk mengubah teks rahasia kembali menjadi teks asli (dekripsi)
def dekripsi(sandi, kunci):
    # Menyiapkan variabel string kosong untuk menampung hasil dekripsi
    terdekripsi = ""
    # Memotong teks rahasia menjadi beberapa bagian sepanjang ukuran string kunci
    potongan_sandi = [
        sandi[i: i + len(kunci)] for i in range(0, len(sandi), len(kunci))
    ]

    # Melakukan perulangan untuk setiap potongan teks rahasia yang sudah dibagi
    for setiap_potongan in potongan_sandi:
        # Menginisialisasi ulang indeks penunjuk karakter kunci dari angka 0
        i = 0
        # Melakukan perulangan untuk mengambil setiap huruf di dalam satu potongan teks rahasia
        for huruf in setiap_potongan:
            # Rumus matematika dekripsi Vigenere: (Indeks Huruf Cipher - Indeks Huruf Kunci) % 27
            angka = (huruf_ke_indeks[huruf] -
                     huruf_ke_indeks[kunci[i]]) % len(alfabet)
            # Mengubah angka hasil rumus kembali menjadi huruf teks asli dan menambahkannya ke variabel hasil
            terdekripsi += indeks_ke_huruf[angka]
            # Menaikkan indeks penunjuk karakter kunci agar bergeser ke huruf kunci berikutnya
            i += 1

    # Mengembalikan string teks asli utuh hasil dekripsi ke pemanggil fungsi
    return terdekripsi


# Fungsi utama untuk menjalankan alur program simulasi
def main():
    # Menentukan string kalimat asli yang ingin dienkripsi
    pesan = "i loove peanuts"
    # Menentukan kata kunci pengunci sandi
    kunci = "banana"
    # Memanggil fungsi enkripsi untuk memproses pesan asli menggunakan kunci
    pesan_terenkripsi = enkripsi(pesan, kunci)
    # Memanggil fungsi dekripsi untuk memproses teks rahasia menggunakan kunci yang sama
    pesan_terdekripsi = dekripsi(pesan_terenkripsi, kunci)

    # Menampilkan string pesan asli ke layar konsol
    print("Pesan asli: " + pesan)
    # Menampilkan string hasil enkripsi ke layar konsol
    print("Pesan terenkripsi: " + pesan_terenkripsi)
    # Menampilkan string hasil dekripsi ke layar konsol
    print("Pesan terdekripsi: " + pesan_terdekripsi)


if __name__ == "__main__":

    # Memanggil fungsi utama untuk mengeksekusi script program
    main()
