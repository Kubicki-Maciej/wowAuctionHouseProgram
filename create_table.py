import sqlite3


conn = sqlite3.connect('data_items.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS items (
    id_item integer,
    item_name text,
    picture_url text,
    url text
)""")



