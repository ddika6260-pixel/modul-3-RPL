
import os
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.db_name = os.getenv("DB_NAME", "perpustakaan")
        self.username = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")

    def get_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.db_name,
                user=self.username,
                password=self.password
            )
            return conn

        except Error as e:
            raise Exception(f"Koneksi database gagal: {e}")
