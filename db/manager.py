import psycopg2 as psql


class Database:
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
        data = ["update",  "insert", "delete", "alter", "create"]
        if query_type in data:
            db.commit()
            return f"  successful"
        else:
            return cursor.fetchall()
