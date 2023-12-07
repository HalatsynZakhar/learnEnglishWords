import sqlite3

conn = sqlite3.connect('EngRus.db')
cur = conn.cursor()

# Выбираем все поля из engrus для объединения
cur.execute('SELECT * FROM engrus ORDER BY english')
rows = cur.fetchall()

# Создаем новую таблицу для результата
cur.execute('CREATE TABLE IF NOT EXISTS merged_engrus (currentLvl INTEGER, currentStepInLvl INTEGER, stepLvl INTEGER, status TEXT, english TEXT, russian_combined TEXT)')

# Группируем и объединяем значения поля `russian` через ", "
grouped_rows = {}
for row in rows:
    english = row[4]  # Поле `english` в пятой колонке (с индексом 4)
    russian = row[5]  # Поле `russian` в шестой колонке (с индексом 5)
    if english not in grouped_rows:
        grouped_rows[english] = {'currentLvl': row[0], 'currentStepInLvl': row[1], 'stepLvl': row[2], 'status': row[3], 'english': english, 'russian_combined': []}
    grouped_rows[english]['russian_combined'].append(russian)

# Вставляем объединенные данные в новую таблицу
for row in grouped_rows.values():
    cur.execute('INSERT INTO merged_engrus VALUES (?, ?, ?, ?, ?, ?)', (row['currentLvl'], row['currentStepInLvl'], row['stepLvl'], row['status'], row['english'], ', '.join(row['russian_combined'])))

# Выводим результат
cur.execute('SELECT * FROM merged_engrus ORDER BY english')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
