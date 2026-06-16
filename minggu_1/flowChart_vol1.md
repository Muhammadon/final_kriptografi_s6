 ˜˜˜bash
 ┌───────────────┐
 │  MULAI (Start)│
 └───────┬───────┘
         │
 ┌───────▼───────────────────────────┐
 │ INPUT Plainteks & Kunci (Integer) │
 └───────┬───────────────────────────┘
         │
 ┌───────▼───────────────────────────┐
 │ PROSES: key = key % 26            │
 │         result = []               │
 └───────┬───────────────────────────┘
         │
 ┌───────▼───────────────────────────┐
 │ LOOP: Untuk setiap 'char' di      │◄──────────┐
 │       teks (diubah ke uppercase)  │           │
 └───────┬───────────────────────────┘           │
         │                                       │
         ├──────────────────► [Jika LOOP Selesai]│
         │                                       │
 ┌───────▼───────────────────────────┐           │
 │ DECISION: Apakah 'char' itu       │           │
 │ huruf alfabet? (char.isalpha())   │           │
 └───────┬───────────────────────────┘           │
         │                                       │
   ┌─────┴─────┐                                 │
   │ YA        │ TIDAK                           │
 ┌─▼─┐       ┌─▼─┐                               │
 │   │       │   │                               │
 │ P │       │ P │                               │
 │ R │       │ R │                               │
 │ O │       │ O │                               │
 │ S │       │ S │                               │
 │ E │       │ E │                               │
 │ S │       │ S │                               │
 │   │       │   │                               │
 │ 1 │       │ 2 │                               │
 └─┬─┘       └─┬─┘                               │
   │           │                                 │
   └─────┬─────┘                                 │
         │                                       │
         └───────────────────────────────────────┘
 
 *Penjelasan Blok Cabang (Decision):
 [PROSES 1 - JIKA YA]:
 - p = posisi huruf ke angka (0-25)
 - c = (p + key) % 26
 - Ubah c kembali ke huruf
 - Simpan huruf ke dalam 'result'

 [PROSES 2 - JIKA TIDAK]:
 - Simpan 'char' asli ke dalam 'result' tanpa diubah (misal spasi/tanda baca)

 ====================================================
 (Setelah LOOP Selesai)
         │
 ┌───────▼───────────────────────────┐
 │ OUTPUT: Gabungkan isi 'result'    │
 │         menjadi satu string       │
 └───────┬───────────────────────────┘
         │
 ┌───────▼───────┐
 │    SELESAI    │
 └───────────────┘
 ˜˜˜