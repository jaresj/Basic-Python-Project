

import sqlite3

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_txtFiles TEXT \
    )")
    conn.commit()
conn.close()

conn = sqlite3.connect('drill.db')
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    for items in fileList:
        if items.endswith('.txt'):
            cur.execute('INSERT INTO tbl_files(col_txtFiles) VALUES (?)', \
                        (items,))
    conn.commit
conn.close()


conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files")
    varFiles = cur.fetchall()
    for item in varFiles:
        print(item)
