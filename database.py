import psycopg2, traceback
from psycopg2.extensions import register_type, UNICODE


CONN_STR = "host='tyke.db.elephantsql.com' port='5432' dbname='zraipbcj' user='zraipbcj' password='UKhLBec43xcfm_dKAqwAGyRN-WVUBR-V'"

def connection_db():
    global cur, conn
    try:
        register_type(UNICODE)
        conn = psycopg2.connect(CONN_STR)
        cur = conn.cursor()
    except:
        print(traceback.format_exc())

def close_connection():
    cur.close()
    conn.close()


class Database:
    def __init__(self):
        self.AUTH = False
        self.user_data = 'Unknown user'

    def authentificate_user(self, login, password):
        connection_db()
        cur.execute("SELECT * FROM demo_01.select_user(%s, %s)", (login, password))
        print(cur.description)
        self.user_data = cur.fetchone()
        print(self.user_data)
        if self.user_data:
            self.AUTH = True
            close_connection()
        else:
            self.AUTH = False
            close_connection()

    def registration(self, login, password, role, name):
        connection_db()
        cur.callproc("add_user", (login, password, role, name))
        conn.commit()
        close_connection()

    def print_table(self, table_name):
        connection_db()
        cur.execute(f"select * from demoexam.{table_name} limit 0")
        headers = [desc[0] for desc in cur.description]
        cur.execute(f"select * from demoexam.{table_name}")
        table = cur.fetchall()
        close_connection()
        return headers, table
    
    def order_product(self, product_name, width, height, note, cloth, fitting):
        try:
            connection_db()
            cur.execute("insert into demoexam.product values(%s, %s, %s, 13123, %s)", (product_name, width, height, note))
            conn.commit()
            cur.execute("insert into demoexam.product_clothes values (%s, %s)", (cloth, product_name))
            conn.commit()
            cur.execute("insert into demoexam.product_fittings values (%s, %s, 'расположение',1, 1, 1, 1)", (fitting, product_name))
            conn.commit()
            close_connection()
            print("Успешно!")
        except:
            print(traceback.format_exc())
        