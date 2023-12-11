import sqlite3

from Word import Word


class Database:
    def __init__(self, name_database, table_name):
        self.name_database = name_database
        self.table_name = table_name
    def get_one_random_element_cond(self, condition):
        conn = sqlite3.connect(self.name_database)
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM {} WHERE {} ORDER BY RANDOM() LIMIT 1;'.format(self.table_name, condition))  # Используйте имя вашей таблицы
        word_tuple = cur.fetchone()
        print(word_tuple)
        conn.close()
        try:
            word = Word(*word_tuple)
            return word
        except:
            pass
    def get_one_random_element(self):
        conn = sqlite3.connect(self.name_database)
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM {} ORDER BY RANDOM() LIMIT 1;'.format(self.table_name))  # Используйте имя вашей таблицы
        word_tuple = cur.fetchone()
        print(word_tuple)
        conn.close()
        try:
            word = Word(*word_tuple)
            return word
        except:
            pass

    def find_element(self, column, value):
        conn = sqlite3.connect(self.name_database)
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM {} WHERE {} = '{}' LIMIT 1;".format(self.table_name, column, value))  # Используйте имя вашей таблицы
        word_tuple = cur.fetchone()
        conn.close()
        try:
            word = Word(*word_tuple)
            return word
        except:
            pass

    def write_word(self, word):
        conn = sqlite3.connect(self.name_database)
        cur = conn.cursor()

        cur.execute(
            f"UPDATE {self.table_name} SET currentLvl = ?, currentStepInLvl = ?, stepLvl = ?, status = ?, english = ?, russian = ?, type = ? WHERE english = ?",
            (word.currentLvl, word.currentStepInLvl, word.stepLvl, word.status, word.english, word.russian, word.type,
             word.english)
        )

        conn.commit()
        conn.close()

    def special_request(self, request_sql):
        return
