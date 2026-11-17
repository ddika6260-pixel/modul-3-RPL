
import hashlib
import mysql.connector
from config.database import Database


class UserModel:

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    def autentikasi(self, username, password):
        try:
            cursor = self.conn.cursor(dictionary=True)

            password_hash = self.hash_password(password)

            query = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s AND password = %s
            """

            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()

            cursor.close()

            return user

        except mysql.connector.Error as error:
            print("Error login:", error)
            return None

    def register_user(self, username, password, role):
        try:
            cursor = self.conn.cursor()

            password_hash = self.hash_password(password)

            query = """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (username, password_hash, role)
            )

            self.conn.commit()
            cursor.close()

            return True

        except mysql.connector.Error as error:
            print("Registrasi gagal:", error)
            self.conn.rollback()
            return False
