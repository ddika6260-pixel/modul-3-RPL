
from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_get_all_buku():
    # Data contoh untuk pengujian
    data_contoh = [
        {
            "id_buku": 1,
            "judul": "Laskar Pelangi",
            "penulis": "Andrea Hirata",
            "tahun_terbit": 2008
        },
        {
            "id_buku": 2,
            "judul": "Pemrograman Python MVC",
            "penulis": "Guido van Rossum",
            "tahun_terbit": 2023
        }
    ]

    # Membuat objek BukuModel tanpa koneksi database asli
    model = BukuModel.__new__(BukuModel)

    # Siapkan atribut yang diperlukan model
    model.table_name = "buku"
    model.conn = MagicMock()

    # Siapkan cursor dan hasil query tiruan
    cursor_mock = MagicMock()
    model.conn.cursor.return_value = cursor_mock
    cursor_mock.fetchall.return_value = data_contoh

    # Jalankan fungsi yang diuji
    hasil = model.get_all_buku()

    # Periksa hasil pengujian
    assert hasil == data_contoh
    assert len(hasil) == 2
    assert hasil[0]["judul"] == "Laskar Pelangi"
    assert hasil[1]["judul"] == "Pemrograman Python MVC"

    # Pastikan query dijalankan
    cursor_mock.execute.assert_called_once_with(
        "SELECT * FROM buku"
    )

    cursor_mock.close.assert_called_once()
