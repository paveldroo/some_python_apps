import sqlite3


def create():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()


# insert('Water Glass', 10, 6.5)
# insert('Wine Glass', 8, 5.5)
# insert('Coffee Cup', 15, 2.3)

# delete('Wine Glass')
update(222, 1.8, 'Coffee Cup')

print(view())
