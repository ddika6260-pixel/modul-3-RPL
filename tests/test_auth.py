
from unittest.mock import MagicMock
from models.user_model import UserModel


def test_hash_password_konsisten():
    password_asli = "admin123"

    hash_1 = UserModel.hash_password(password_asli)
    hash_2 = UserModel.hash_password(password_asli)

    assert hash_1 != password_asli
    assert hash_1 == hash_2
    assert len(hash_1) == 64


def test_autentikasi_pengguna_berhasil():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchone.return_value = {
        "id_user": 1,
        "username": "petugas",
        "role": "admin"
    }

    mock_conn.cursor.return_value = mock_cursor

    model = UserModel(connection=mock_conn)

    hasil = model.autentikasi("petugas", "admin123")

    assert hasil is not None
    assert hasil["username"] == "petugas"
    assert hasil["role"] == "admin"

    mock_conn.cursor.assert_called_once_with(dictionary=True)
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()
