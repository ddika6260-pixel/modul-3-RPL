
# Aplikasi Sistem Informasi Perpustakaan

## Deskripsi Aplikasi

Aplikasi Sistem Informasi Perpustakaan merupakan aplikasi desktop berbasis Python yang dibuat untuk membantu pengelolaan data buku pada perpustakaan. Aplikasi ini menggunakan arsitektur Model-View-Controller (MVC) dan database MySQL sebagai tempat penyimpanan data.

Aplikasi menyediakan fitur login pengguna, pengelolaan data buku, serta pembatasan hak akses berdasarkan role pengguna. Admin atau petugas dapat menambah, mengubah, menghapus, dan melihat data buku. Sementara itu, anggota hanya dapat melihat data buku.

## Struktur Direktori MVC

```text
kodingan-rpl/
│
├── config/
│   └── database.py
│
├── controllers/
│   ├── auth_controller.py
│   └── buku_controller.py
│
├── models/
│   ├── user_model.py
│   └── buku_model.py
│
├── views/
│   ├── login_view.py
│   └── buku_view.py
│
├── tests/
│   └── test_auth.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Teknologi yang Digunakan

- Python
- CustomTkinter
- MySQL
- mysql-connector-python
- Pytest
- Flake8
- GitHub Actions
- PyInstaller

## Instalasi dan Konfigurasi Database MySQL

1. Pastikan Python, Visual Studio Code, dan Laragon telah terpasang.
2. Jalankan Laragon dan aktifkan layanan MySQL.
3. Buat database dengan nama `perpustakaan`.
4. Siapkan tabel `buku` dan `users` sesuai struktur database aplikasi.
5. Pastikan konfigurasi koneksi database pada `config/database.py` sesuai dengan pengaturan MySQL lokal.

Contoh konfigurasi database:

```python
host = "localhost"
user = "root"
password = ""
database = "perpustakaan"
```

Sesuaikan nilai konfigurasi tersebut dengan pengaturan MySQL yang digunakan.

## Cara Menjalankan Aplikasi

1. Buka folder proyek melalui Visual Studio Code.
2. Aktifkan virtual environment.
3. Instal seluruh dependensi:

```bash
pip install -r requirements.txt
```

4. Pastikan MySQL pada Laragon sudah berjalan.
5. Jalankan aplikasi melalui terminal:

```bash
python main.py
```

6. Masuk menggunakan akun yang sudah terdaftar pada tabel `users`.

## Pengujian Otomatis

Pengujian dilakukan menggunakan Pytest. Jalankan perintah:

```bash
pytest -v
```

Pemeriksaan kualitas kode dilakukan menggunakan Flake8:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

GitHub Actions menjalankan pemeriksaan kode dan unit test secara otomatis ketika terdapat push atau pull request ke branch `main`.

## Pemaketan Aplikasi

Aplikasi dikemas menggunakan PyInstaller dengan perintah:

```bash
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

File aplikasi hasil pemaketan akan tersedia pada folder `dist/` dengan nama `AplikasiPerpustakaan.exe`.
