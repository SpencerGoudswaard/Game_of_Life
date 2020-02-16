# Spencer Goudswaard
# 
# Quests will contain a description, a list of tasks, and a list of rewards.
#
# Quests should have the option to repeat over a period of time.
# Quests should have the option to have a time limit set.
# Quests should have the option to have tiers for consecutive completions.
# Quests should have the option to give feats, exp, and buffs as rewards.

import Character
import Task

class Quest:
    
    def __init__(self, character):
        self.character = character
        print("Enter a description of this quest:")
        self.description = input()
        self.tasks = []
    
    def addTask(self):
        print("Add task by entering description:")
        task_desc = input()
        self.tasks.append(Task.Task(task_desc))
        
    def addReward(self):
        print("Add reward for completing the quest.")
        print("Strength Exp:")
        self.str_exp = input()
        print("Dexterity Exp:")
        self.dex_exp = input()
        print("Constitution Exp:")
        self.con_exp = input()
        print("Intelligence Exp:")
        self.int_exp = input()
        print("Wisdom Exp:")
        self.wis_exp = input()
        print("Charisma Exp:")
        self.cha_exp = input()
        
    
    def completeTask(self, taskNum):
        self.tasks[taskNum - 1].complete()
        
    def showTasks(self):
        for i,task in enumerate(self.tasks):
            if(task.isCompleted()):
                print("{i} ".format(i = i) + "Completed: " + task.description)
            else:
                print("{i} ".format(i = i) + task.description)
    
    def completeQuest(self):
        completedTasks = 0
        numberOfTasks = 0
        for i,task in enumerate(self.tasks):
            numberOfTasks += 1
            if(task.isCompleted()):
                completedTasks += 1
                
        if (completedTasks == numberOfTasks):
            print(self.description)
            print("Congratulations you've completed this quest!")
            if (int(self.str_exp) > 0):
                print("Strength Experience Gained: " + "{str}xp".format(str = self.str_exp))
                self.character.incStr(int(self.str_exp))
            
            if (int(self.dex_exp) > 0):
                print("Dexterity Experience Gained: " + "{dex}xp".format(dex = self.dex_exp))
                self.character.incDex(int(self.dex_exp))
                
            if (int(self.con_exp) > 0):
                print("Constitution Experience Gained: " + "{con}xp".format(con = self.con_exp))
                self.character.incCon(int(self.con_exp))
                
            if (int(self.int_exp) > 0):
                print("Intelligence Experience Gained: " + "{int}xp".format(int = self.int_exp))
                self.character.incInt(int(self.int_exp))
                
            if (int(self.wis_exp) > 0):
                print("Wisdom Experience Gained: " + "{wis}xp".format(wis = self.wis_exp))
                self.character.incWis(int(self.wis_exp))
                
            if (int(self.cha_exp) > 0):
                print("Charisma Experience Gained: " + "{cha}xp".format(cha = self.cha_exp))
                self.character.incCha(int(self.cha_exp))
        else:
            print("Complete all tasks to complete the Quest.")
