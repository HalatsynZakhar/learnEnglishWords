class UniversalWord():
    def __init__(self, english, russian):
        self.english = english
        self.current_lvl = 0
        self.all_level = len(english)
        self.level_difficulty = 100
        self.russian = russian
