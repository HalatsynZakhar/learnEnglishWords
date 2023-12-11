import random
import sqlite3

from colorama import Style, Fore


class Training:
    def __init__(self, words):
        self.words = words
    def print_collor(self, color, text):
        print(color + text + Style.RESET_ALL)
    def generate_word(self):
        return random.choice(self.words)

    def find_word(self, word):
        for i in self.words:
            if i.english==word:
                return i
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