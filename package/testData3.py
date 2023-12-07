import sqlite3

conn = sqlite3.connect('EngRus.db')
cur = conn.cursor()

# Пример: Удаляем строки, где статус равен "не изучено"
status_to_delete = ""
cur.execute('DELETE FROM merged_engrus WHERE english = ?', (status_to_delete,))

# Выводим результат после удаления
cur.execute('SELECT * FROM merged_engrus')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()