
from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_get_all_buku():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchall.return_value = [
        {
            "id_buku": 1,
            "judul": "Pemrograman Python",
            "penulis": "Guido van Rossum",
            "tahun_terbit": 2024
        }
    ]

    mock_conn.cursor.return_value = mock_cursor

    model = BukuModel(connection=mock_conn)

    hasil = model.get_all_buku()

    assert len(hasil) == 1
    assert hasil[0]["judul"] == "Pemrograman Python"


def test_update_buku():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value = mock_cursor

    model = BukuModel(connection=mock_conn)

    model.update_buku(
        9,
        "Pemrograman Python MVC Update",
        "Guido van Rossum",
        2024
    )

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()


def test_delete_buku():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value = mock_cursor

    model = BukuModel(connection=mock_conn)

    model.delete_buku(9)

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
