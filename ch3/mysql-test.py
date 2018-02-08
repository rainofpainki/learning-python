# 라이브러리 읽어 들이기
# 책에는 mysqlclient를 사용하지만 여기서는 pymysql을 사용해본다.
import pymysql

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'myRosa#@!'
DB_CONNDB = 'test'

conn = pymysql.connect(
    user=DB_USER,
    passwd=DB_PASSWORD,
    host=DB_HOST,
    db=DB_CONNDB
)

cur = conn.cursor()

# 테이블 생성하기
cur.execute('''
    CREATE TABLE IF NOT EXISTS items (
      item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
      name  TEXT,
      price INTEGER
    )
''')

# 데이터 추가하기
data = [
    ('Banana', 300),
    ('Mango', 640),
    ('Kiwi', 280)
]
for i in data:
    cur.execute("INSERT INTO items(name, price) VALUES(%s, %s)", i)

# 데이터 추출하기
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)