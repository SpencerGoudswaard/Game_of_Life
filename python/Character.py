# Spencer Goudswaard
#
# Based on D&D stats
# Stats 
# Level
# Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
# Characters should be able to gain feats or traits via quests.
# Characters should be able to have time sensitive buffs and debuffs.
# Characters could have an inventory option that shows assets and capital.

class Character:
    
    def __init__(self, name, age, strExp, dexExp, conExp, intExp, wisExp, chaExp):
        self.name = name
        self.age = age
        self.Level = 1
        self.Strength = 1
        self.Dexterity = 1
        self.Constitution = 1
        self.Intelligence = 1
        self.Wisdom = 1
        self.Charisma = 1
        self.strExp = strExp
        self.dexExp = dexExp
        self.conExp = conExp
        self.intExp = intExp
        self.wisExp = wisExp
        self.chaExp = chaExp
    
    def stats(self):
        print("Name: {name}\nAge: {age} \nLevel: {Level} \nStrength: {Str} \nDexterity: {Dex} \nConstitution: {Con} \nIntelligence: {Int} \nWisdom: {Wis} \nCharisma: {Cha}".format(name = self.name, age = self.age, Level = self.Level, Str = self.Strength, Dex = self.Dexterity, Con = self.Constitution, Int = self.Intelligence, Wis = self.Wisdom, Cha = self.Charisma))
    
    def incStr(self, value):
        self.strExp += value
        while (self.strExp >= 100*(2**self.Strength)):
            self.Strength += 1
            self.Level += 1
    
    def expToLvlStr(self):
        expToLvl = 100*(2**self.Strength) - self.strExp
        print(expToLvl)
    
    def incDex(self, value):
        self.dexExp += value
        while (self.dexExp >= 100*(2**self.Dexterity)):
            self.Dexterity += 1
            self.Level += 1
            
    def expToLvlDex(self):
        expToLvl = 100*(2**self.Dexterity) - self.dexExp
        print(expToLvl)
     
    def incCon(self, value):
        self.conExp += value
        while (self.conExp >= 100*(2**self.Constitution)):
            self.Constitution += 1
            self.Level += 1
            
    def expToLvlCon(self):
        expToLvl = 100*(2**self.Constitution) - self.conExp
        print(expToLvl)
        
    def incInt(self, value):
        self.intExp += value
        while (self.intExp >= 100*(2**self.Intelligence)):
            self.Intelligence += 1
            self.Level += 1
            
    def expToLvlInt(self):
        expToLvl = 100*(2**self.Intelligence) - self.intExp
        print(expToLvl)

    def incWis(self, value):
        self.wisExp += value
        while (self.wisExp >= 100*(2**self.Wisdom)):
            self.Wisdom += 1
            self.Level += 1
            
    def expToLvlWis(self):
        expToLvl = 100*(2**self.Wisdom) - self.wisExp
        print(expToLvl)

    def incCha(self, value):
        self.chaExp += value
        while (self.chaExp >= 100*(2**self.Charisma)):
            self.Charisma += 1
            self.Level += 1
            
    def expToLvlCha(self):
        expToLvl = 100*(2**self.Charisma) - self.chaExp
        print(expToLvl)
