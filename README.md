Panduan Penggunaan EDOM Auto-Filler (Semi-Otomatis)
Program ini didesain untuk membantu pengisian kuesioner EDOM secara semi-otomatis dengan kontrol penuh dari pengguna.

Cara Menggunakan
1. Persiapan: Pastikan selenium sudah terinstall (pip install selenium).

2. Jalankan Program: Buka terminal di folder tempat file disimpan, ketik python auto_edom.py.

3. Login: Browser akan terbuka. Lakukan login manual ke i-GRACIAS dan navigasi hingga halaman kuesioner Part 1 muncul di layar.

4. Eksekusi: Kembali ke terminal, tekan ENTER. Program akan otomatis mengisi seluruh pilihan ganda dan kolom komentar di halaman tersebut.

5. Navigasi Part: * Setelah Part selesai diisi, pindah ke Part berikutnya di halaman browser secara manual (klik tombol 'Update' atau 'Part' selanjutnya).

5. Kembali ke terminal, pilih [1] untuk lanjut mengisi Part baru, atau [2] jika kuesioner sudah selesai.

⚠️ PERINGATAN PENTING (BACA INI)
Program ini hanya berfungsi untuk kuesioner yang menggunakan format template standar.

Apa itu Template Standar? Program ini mencari elemen HTML bertipe radio (untuk pilihan ganda) dan textarea (untuk komentar).

Keterbatasan: Jika kuesioner memiliki tipe soal yang berbeda (seperti checkbox, slider, rating star, atau menu dropdown), program tidak akan bisa mendeteksi soal tersebut dan akan melewatinya.

Pengecekan Manual: Karena ini bersifat semi-otomatis, sangat disarankan untuk melakukan review singkat pada hasil isian sebelum menekan tombol Submit/Simpan terakhir di portal i-GRACIAS.
