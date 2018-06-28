import psycopg2


def create():
    conn = psycopg2.connect("dbname='udemytest' user='paveldruzhinin' password='Isoquiu1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='udemytest' user='paveldruzhinin' password='Isoquiu1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='udemytest' user='paveldruzhinin' password='Isoquiu1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='udemytest' user='paveldruzhinin' password='Isoquiu1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='udemytest' user='paveldruzhinin' password='Isoquiu1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()


# create()
# insert('Water Glass', 10, 6.5)
# insert('Wine Glass', 8, 5.5)
# insert('Coffee Cup', 15, 2.3)

delete('Wine Glass')
update(222, 1.8, 'Coffee Cup')

print(view())
