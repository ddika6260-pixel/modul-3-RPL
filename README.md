# SISTEM MANAJEMEN PERPUSTAKAAN

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang dibuat untuk membantu proses pengelolaan data perpustakaan. Aplikasi ini menggunakan konsep arsitektur Model-View-Controller (MVC) untuk memisahkan bagian pengolahan data, tampilan antarmuka, dan pengendalian sistem.

Aplikasi ini memiliki fitur autentikasi pengguna (login) dan pengelolaan data perpustakaan. Data disimpan menggunakan database MySQL sehingga dapat dikelola secara terstruktur. Aplikasi dikembangkan menggunakan Python dengan antarmuka desktop serta didukung oleh pengujian otomatis menggunakan pytest dan pemeriksaan kualitas kode menggunakan Flake8.

## 2. Struktur Direktori MVC

Struktur direktori proyek Sistem Manajemen Perpustakaan terdiri dari beberapa folder dan file berikut:

```text
modul-3-RPL/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── config/
│   └── database.py
│
├── controllers/
│   ├── auth_controller.py
│   ├── buku_controller.py
│   └── anggota_controller.py
│
├── models/
│   ├── user_model.py
│   ├── buku_model.py
│   └── anggota_model.py
│
├── views/
│   ├── login_view.py
│   ├── buku_view.py
│   └── anggota_view.py
│
├── tests/
│   ├── test_auth.py
│   └── test_buku.py
│
├── main.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Penjelasan Struktur MVC

- **Models:** Bertugas mengelola data dan berinteraksi dengan database MySQL.
- **Views:** Bertugas menampilkan antarmuka aplikasi kepada pengguna.
- **Controllers:** Mengatur proses dan menghubungkan Models dengan Views.
- **Config:** Menyimpan konfigurasi koneksi database.
- **Tests:** Menyimpan file pengujian untuk memastikan fungsi aplikasi berjalan dengan baik.
- **.github/workflows:** Menyimpan konfigurasi GitHub Actions untuk menjalankan CI Pipeline secara otomatis.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki beberapa perangkat lunak berikut:

1. Python versi 3.11.
2. Visual Studio Code.
3. Laragon.
4. MySQL.
5. Git.

### B. Mengunduh Proyek

Clone repositori dari GitHub menggunakan perintah:

```bash
git clone https://github.com/ddika6260-pixel/modul-3-RPL.git
```

Masuk ke direktori proyek:

```bash
cd modul-3-RPL
```

### C. Membuat Virtual Environment

Buat lingkungan virtual Python dengan perintah:

```bash
python -m venv env
```

Aktifkan virtual environment pada Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### D. Instalasi Dependensi

Instal seluruh pustaka yang dibutuhkan aplikasi menggunakan file requirements.txt:

```bash
pip install -r requirements.txt
```

### E. Konfigurasi Database MySQL

1. Buka aplikasi Laragon.
2. Jalankan layanan MySQL.
3. Buka phpMyAdmin atau MySQL client.
4. Buat database dengan nama `perpustakaan`.
5. Pastikan konfigurasi koneksi database pada aplikasi sudah sesuai.

Konfigurasi koneksi database menggunakan informasi berikut:

- Host: localhost
- Port: 3306
- Username: root
- Password: Sesuaikan dengan konfigurasi MySQL.
- Database: perpustakaan

Pastikan nama database, username, password, dan port sesuai dengan pengaturan MySQL pada komputer yang digunakan.

## 4. Cara Menjalankan Aplikasi

Setelah instalasi dan konfigurasi database selesai, ikuti langkah berikut:

1. Pastikan Laragon dan MySQL sudah berjalan.
2. Buka folder proyek melalui Visual Studio Code.
3. Aktifkan virtual environment.
4. Pastikan seluruh dependensi telah terinstal.
5. Jalankan aplikasi menggunakan perintah:

```bash
python main.py
```

Setelah program dijalankan, aplikasi akan menampilkan antarmuka Sistem Manajemen Perpustakaan. Pengguna dapat melakukan login dan menggunakan fitur pengelolaan data sesuai dengan fungsi yang tersedia.

## 5. Pengujian dan Otomasi CI Pipeline

Proyek ini menggunakan pytest untuk menjalankan pengujian otomatis dan Flake8 untuk memeriksa kualitas penulisan kode.

Perintah untuk menjalankan pengujian:

```bash
pytest -v
```

Perintah untuk memeriksa kualitas kode:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

GitHub Actions digunakan untuk menjalankan proses Continuous Integration secara otomatis setiap kali terdapat perubahan kode yang dikirimkan ke repositori GitHub.

Proses ini membantu memastikan bahwa kode aplikasi telah melewati pemeriksaan kualitas dan pengujian sebelum digunakan atau dikembangkan lebih lanjut.

## 6. Teknologi yang Digunakan

- Python 3.11
- MySQL
- Laragon
- CustomTkinter
- mysql-connector-python
- pytest
- Flake8
- Git dan GitHub
- GitHub Actions
- PyInstaller
