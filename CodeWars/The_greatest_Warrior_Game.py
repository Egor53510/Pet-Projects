class Warrior:
    RANG = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    exp_to_level_up = 200
    def __init__(self):
        self.level = 1
        self.rang = Warrior.RANG[0]
        self.experience = 100

    def rang_up(self):
        if self.level == 10:
            self.rang = Warrior.RANG[self.level // 10]
    
    def level_up(self):
        if self.experience == self.exp_to_level_up and self.level <= 100:
            self.level += 1
            self.experience -= 100
            self.rang_up()

bruce_lee = Warrior()
print(bruce_lee.level)
print(bruce_lee.rang)

