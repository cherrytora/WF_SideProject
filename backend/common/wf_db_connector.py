import psycopg2
from dotenv import load_dotenv
import os


def register(values: tuple):
    load_dotenv()
    DATABASE_URL = os.getenv('WFDB_URL', None)
    with psycopg2.connect(DATABASE_URL) as conn:
        cur = conn.cursor()
        sql = f"""
        CREATE EXTENSION IF NOT EXISTS pgcrypto;
        INSERT INTO authz (employee, name, department, acct, pwd, auth)
                VALUES {values}
                ON CONFLICT (employee) DO UPDATE
                SET name = EXCLUDED.name,
                    department = EXCLUDED.department,
                    acct = EXCLUDED.acct,
                    pwd = EXCLUDED.pwd,
                    auth = EXCLUDED.auth;"""
        cur.execute(sql)
        # rows = cur.fetchall()
        print(f"Run:\n{sql}")


# if __name__ == "__main__":
#     insert_data = ('A0002', 'Emma', '20', 'A0002', '0000', '40')
#     register(insert_data)
