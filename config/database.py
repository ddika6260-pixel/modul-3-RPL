
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = "localhost"
        self.db_name = "perpustakaan"
        self.username = "root"
        self.password = ""

    def get_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                database=self.db_name,
                user=self.username,
                password=self.password
            )
            return conn

        except Error as e:
            raise Exception(f"Koneksi database gagal: {e}")
