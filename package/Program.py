import random
import sqlite3

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


from Training import Training
from Word import Word
from colorama import Fore, Style


class Program:
    def __init__(self):
        self.training = Training(self.get_data_from_database())
    def print_collor(self, color, text):
        print(color + text + Style.RESET_ALL)

    def run(self):
        print("Добро пожаловать в программу для изучения английских слов!")
        print("Введите перевод слова на английском языке.")
        print("Для выхода из программы введите '123'.")
        print(
            "Выберите режим тренировки. 1 - все слова кроме изученных, 2 - уже взятые на изучение, 3 - повторение изученных слов, 4 - собственный набор слов")
        inp = input()
        print("Введите количество слов, которые будут по-кругу изучаться (если не натуральное число, то ограничений нет")
        num =input()
        temp = []
        if num.isdigit():
            num = int(num)
            if num<=0:
                num = 0
        else:
            num = 0

        if inp=="1":
            while len(temp)!= num:
                word = self.training.generate_word()
                if word.getStatus() == "изучено":
                    continue
                temp.append(word)
        if inp=="2":
            while len(temp)!= num:
                word = self.training.generate_word()
                if word.getStatus() == "не изучено" or word.getStatus() == "изучено":
                    continue
                temp.append(word)
        if inp == "3":
            while len(temp) != num:
                word = self.training.generate_word()
                if word.getStatus() == "не изучено" or word.getStatus() == "на изучении":
                    continue
                temp.append(word)
        if inp=="4":
            while len(temp)!= num:
                text = input("Введите слово на англ: ")

                word = self.training.find_word(text)
                if isinstance(word, Word):
                    temp.append(word)
                    print("Слово добавлено")
                else:
                    print("Слово не было найдено")


        check = True

        while True:
            if len(temp)>0 and check:
                word = random.choice(temp)
            else:
                if check:
                    word = self.training.generate_word()

                if inp == "1":
                    if word.getStatus() == "изучено":
                        continue
                elif inp == "2":
                    if word.getStatus() == "не изучено" or word.getStatus() == "изучено":
                        continue
                elif inp == "3":
                    if word.getStatus() == "не изучено" or word.getStatus() == "на изучении":
                        continue
                else:
                    break

            print("Текущий уровень: {} из  {}, текущий шаг на уровне: {} из {}.".format(word.getCurrentLvl(),
                                                                                        word.getAllLevel(),
                                                                                        word.getCurrentStepInLvl(),
                                                                                        word.getStepLvl()))
            print("Слово на русском: ", end="")
            self.print_collor(Fore.YELLOW, word.getRussian())
            print("Слово на английском: ", end="")
            self.print_collor(Fore.YELLOW, word.getEnglishTraining())
            answer = input("Ваш ответ: ")

            if answer.lower() == "123":
                break

            check = self.training.check_answer(word, answer)


        print("Программа завершена.")
        self.write_data_to_database(self.training.words)

    def get_data_from_database(self):
        conn = sqlite3.connect('EngRus.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM merged_engrus')  # Используйте имя вашей таблицы
        rows = cur.fetchall()
        words = [Word(*row) for row in rows]
        conn.close()
        return words

    # Функция для записи данных в базу данных
    def write_data_to_database(self, words):
        conn = sqlite3.connect('EngRus.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS merged_engrus')  # Удаляем старую таблицу
        cur.execute(
            'CREATE TABLE IF NOT EXISTS merged_engrus (currentLvl INTEGER, currentStepInLvl INTEGER, stepLvl INTEGER, status TEXT, english TEXT, russian TEXT, type TEXT)')  # Создаем новую таблицу
        data_to_insert = [
            (word.currentLvl, word.currentStepInLvl, word.stepLvl, word.status, word.english, word.russian, word.type) for word
            in words]
        cur.executemany('INSERT INTO merged_engrus VALUES (?, ?, ?, ?, ?, ?, ?)', data_to_insert)
        conn.commit()
        conn.close()


program = Program()
program.run()
