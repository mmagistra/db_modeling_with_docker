import psycopg
import pprint

# Подключение к базе данных postgres
conn = psycopg.connect(
    dbname="db",
    user="mmagistr",
    password="N3v3rTryT0HackM3",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

with open('hw1-queries/4.txt') as f:
    query = f.read().strip()
print(f'Query: {query}')

cur.execute(query)
pprint.pprint(cur.fetchall())
# conn.commit()

# Закрытие курсора и соединения
cur.close()
conn.close()
