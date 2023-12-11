import random

from Word import Word
from colorama import Fore, Style
from Database import Database

class Program:
    def __init__(self):
        self.database = Database("EngRus.db", "merged_engrus")
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
                word = self.database.get_one_random_element_cond("status <> 'изучено'")
                temp.append(word)
        if inp=="2":
            while len(temp)!= num:
                word = self.database.get_one_random_element_cond("status = 'на изучении'")
                temp.append(word)
        if inp == "3":
            while len(temp) != num:
                word = self.database.get_one_random_element_cond("status = 'изучено'")
                temp.append(word)
        if inp=="4":
            while len(temp)!= num:
                text = input("Введите слово на англ: ")

                word = self.database.find_element('english', text)
                if isinstance(word, Word):
                    temp.append(word)
                    print("Слово добавлено")
                else:
                    print("Слово не было найдено")


        check = True

        while True:
            if check:
                if len(temp)>0:
                    word = random.choice(temp)
                else:
                    word = self.database.get_one_random_element()

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

            check = self.check_answer(word, answer)
            if check:
                self.database.write_word(word)


        print("Программа завершена.")

    def check_answer(self, word, answer):
        if word.getEnglish() == answer:
            word.addStep()
            self.print_collor(Fore.GREEN, "Правильно!")
            print()
            return True
        else:
            self.print_collor(Fore.RED, "Неправильно. Правильный ответ: " + word.getEnglish())
            print()
            return False


program = Program()
program.run()
