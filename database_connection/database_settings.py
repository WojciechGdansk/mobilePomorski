import sqlite3


class DBConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
