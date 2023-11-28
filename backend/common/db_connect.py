import psycopg2
from psycopg2.extras import LoggingConnection
import logging
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz

load_dotenv()


class DBConnect():
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        DATABASE_URL = os.getenv('DATABASE_URL', None)
        self.conn = psycopg2.connect(
            DATABASE_URL, connection_factory=LoggingConnection)
        self.conn.initialize(logger)
        self.cur = self.conn.cursor()

    def register(self,name, password):
        sql = """CREATE EXTENSION IF NOT EXISTS pgcrypto;
            SET TIMEZONE = 'Asia/taipei'; 
            INSERT INTO public.users(
            user_name, createdtime, password)
            VALUES (%s, (now()+ interval '8 hour'), crypt(%s, gen_salt('bf')));
        """
        self.cur.execute(sql,[name, password])
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return 'OK'
    



if __name__ == "__main__":
    password = 'haha12345'
    name = 'emma'
    DBConnect().register(name, password)
