from sqlite3 import OperationalError

from .database_settings import DBConnection


class QueriesToDB:
    def __init__(self, sender_email_address=None, receiver_email_address=None):
        self.sender_email_address = sender_email_address
        self.receiver_email_address = receiver_email_address

    @staticmethod
    def connection(query):
        with DBConnection("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query)

    def create_db(self):
        query = f"""CREATE TABLE IF NOT EXISTS saved_data
            (id INTEGER PRIMARY KEY, sender_email_address TEXT, receiver_mail_address TEXT)"""
        self.connection(query)

    def save_to_db(self):
        self.create_db()

        # to have only one record in database check if anything exists and if so update data
        data = self.load_from_db()
        if data:
            self.update_db()
        else:
            query = f"""INSERT INTO saved_data (sender_email_address, receiver_mail_address) VALUES
             ('{self.sender_email_address}', '{self.receiver_email_address}')"""
            self.connection(query)

    @staticmethod
    def load_from_db():
        query = """SELECT sender_email_address, receiver_mail_address from saved_data"""
        with DBConnection("data.db") as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except OperationalError:
                return False
            data = cursor.fetchone()
            # there is always only one record in DB
        return data

    def update_db(self):
        query = f"""UPDATE saved_data SET sender_email_address='{self.sender_email_address}', 
        receiver_mail_address='{self.receiver_email_address}' WHERE ID=1"""
        self.connection(query)
