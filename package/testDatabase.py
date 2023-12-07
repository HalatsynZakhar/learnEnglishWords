import sqlite3

conn = sqlite3.connect('EngRus.db')
cur = conn.cursor()

try:
    cur.execute(
        'CREATE TABLE engrus (currentLvl INTEGER, currentStepInLvl INTEGER, stepLvl INTEGER, status TEXT, english TEXT, russian TEXT)')
except:
    pass

with open("словарь eng - rus.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        rus_start_index = next((i for i, c in enumerate(line) if ord(c) > 127), None)

        # Проверка наличия русского текста
        if rus_start_index is not None:
            eng = line[:rus_start_index].strip()
            rus = line[rus_start_index:].strip()
        else:
            # Если русский текст не найден, используем всю строку как английский текст
            eng = line
            rus = ""

        # Заменяем двойные кавычки на одинарные и экранируем апострофы внутри строк
        a = 'INSERT INTO engrus VALUES (0, 0, 100, "не изучено", ?, ?)'
        cur.execute(a, (eng, rus))

conn.commit()

cur.execute('SELECT * FROM engrus')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
