
from unittest.mock import MagicMock
from models.anggota_model import AnggotaModel


def test_create_anggota():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value = mock_cursor

    model = AnggotaModel(connection=mock_conn)

    hasil = model.create_anggota(
        "Wayan Andika",
        "Palu"
    )

    assert hasil is True
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_get_all_anggota():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchall.return_value = [
        {
            "id_anggota": 1,
            "nama": "Wayan Andika",
            "alamat": "Palu"
        }
    ]

    mock_conn.cursor.return_value = mock_cursor

    model = AnggotaModel(connection=mock_conn)

    hasil = model.get_all_anggota()

    assert len(hasil) == 1
    assert hasil[0]["nama"] == "Wayan Andika"
    assert hasil[0]["alamat"] == "Palu"
    mock_cursor.close.assert_called_once()
