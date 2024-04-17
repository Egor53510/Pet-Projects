class Warrior:
    RANK = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    def __init__(self):
        self.level = 1
        self.rank = Warrior.RANK[0]
        self.experience = self.level * 100
        self.achievements = []

    def rank_up(self):
        self.rank = Warrior.RANK[self.level // 10]
    
    def level_up(self):
        if self.level <= 100:
            self.level = self.experience // 100
        if self.level >= 100:
            if self.experience >= 10000:
                self.experience = 10000
                self.level = 100
        print(self.level)
        print(self.rank)
        self.rank_up()
    def training(self, trainer):
        if self.level >= trainer[2]:
            self.achievements.append(trainer[0])
            self.experience += trainer[1]
            self.level_up()
            return trainer[0]
        else:
            return "Not strong enough"
        
    def battle(self, level_boss):
        if 0 < level_boss <= 100:
            rang_boss = Warrior.RANK[level_boss // 10]
            if (Warrior.RANK.index(self.rank) - Warrior.RANK.index(rang_boss) <= -1) and (self.level + 5 <= level_boss):
                return "You've been defeated"
            else:
                d = self.level - level_boss
                d1 = abs(level_boss - self.level)
                if level_boss == self.level:
                    self.experience += 10
                    self.level_up()
                    return "A good fight"
                elif d == 1:
                    self.experience += 5
                    self.level_up()
                    return "A good fight"
                elif d >= 2:
                    self.experience += 0
                    self.level_up()
                    return "Easy fight"
                elif d1 >= 1:
                    self.experience += 20 * d1 * d1
                    self.level_up()
                    return "An intense fight"
        else:
            return "Invalid level" 

bruce_lee = Warrior()
bruce_lee.level = 100
bruce_lee.rank_up()
bruce_lee.training(["Fight Superman to a draw", 11000, 99])
print(bruce_lee.rank)
print(bruce_lee.experience)
print(bruce_lee.level)


