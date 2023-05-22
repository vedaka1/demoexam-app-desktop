import psycopg2, traceback
from psycopg2.extensions import register_type, UNICODE

CONN_STR = "host='tyke.db.elephantsql.com' port='5432' dbname='zraipbcj' user='zraipbcj' password='UKhLBec43xcfm_dKAqwAGyRN-WVUBR-V'"

def connection():
    global cur, conn
    try:
        register_type(UNICODE)
        conn = psycopg2.connect(CONN_STR)
        cur = conn.cursor()
    except:
        print('Connection error')

class Database:
    def print_user(self, result):
        connection()
        cur.execute('select * from demoexam.users')
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    
    def authenticate_user(self, login, password):
        connection()
        cur.execute("select * from demoexam.users WHERE login=%s AND user_password=%s", (login, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            return True
        else:
            return False
        
    def user_register(self, login, password, role, name):
        try:
            connection()
            cur.callproc('demoexam.add_user', [login, password, role, name])
            conn.commit()
            cur.close()
            conn.close()
        except:
            print(traceback.format_exc())
