import random
import sqlite3

class Training:
    def __init__(self, words):
        self.words = words

    def generate_word(self):
        return random.choice(self.words)

    def find_word(self, word):
        for i in self.words:
            if i.english==word:
                return i
    def check_answer(self, word, answer):
        if word.getEnglish() == answer:
            word.addStep()
            print("Правильно!")
            print()
        else:
            print("Неправильно. Правильный ответ: ", word.getEnglish())
            print()