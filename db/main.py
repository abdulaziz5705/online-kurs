import psycopg2 as psql


class Save:
    @staticmethod
    def connect(query: str, query_type: str) -> str and list:
        db = psql.connect(
            database="kurs",
            user="postgres",
            password="5705",
            host="localhost",
            port="5432"
        )
        cursor = db.cursor()

        cursor.execute(query)
        data = ["update", "insert", "delete", "alter", "create"]
        if query_type in data:
            db.commit()
            return """  
                     sizning ma'lumotlaringiz muvofaqiyatli saqlandi 
                      """
        else:
            return cursor.fetchall()


class Check:
    @staticmethod
    def login_check(username: str, password: str):
        query = f"SELECT * FROM foydalanuvchi WHERE username = '{username}' and password = '{password}'"
        data = Save.connect(query, "select")
        if len(data) == 1:
            return True
        else:
            return False
