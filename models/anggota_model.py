
from config.database import Database


class AnggotaModel:
    def __init__(self, connection=None):
        self.db = Database()

        if connection is not None:
            self.conn = connection
        else:
            self.conn = self.db.get_connection()

        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)

            try:
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                return result

            finally:
                cursor.close()

        return []

    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                query = f"""
                    INSERT INTO {self.table_name}
                    (nama, alamat)
                    VALUES (%s, %s)
                """

                cursor.execute(query, (nama, alamat))
                self.conn.commit()

                return True

            except Exception:
                self.conn.rollback()
                raise

            finally:
                cursor.close()

        return False
