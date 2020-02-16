# Spencer Goudswaard
#
# It's often easy to feel like I'm not making progress in life. I often end up playing video games
# so that I can get that feeling of progress. So this program is my way of using the idea of
# levels, stats, and quests to remind me that I am making progress in life and to change mundane
# tasks in to fun exp farming. 
#
# Features:
# Characters
# The main goal of the Game of Life is to improve your character as much as possible. This is
# achieved by completing quests and collecting rewards.
# 
# Quests
# As the main mode of interaction to the game is creating and completing quests, quests should
# have a lot of style, function, and dynamic options.

import Character
import Quest

print('Welcome to the Game of Life')
print("Type 'Create' to create a character or 'Load' to load a character") 
loop_var = 0
while(loop_var == 0):
    option1 = input()
    if (option1 == 'Create'):
        print("Name: ")
        name = input()
        print("Age: ")
        age = input()
        C1 = Character.Character(name, age, 0, 0, 0, 0, 0, 0)
        loop_var = 1
    elif (option1 == 'Load'):
        print("Load Character")
        loop_var = 1
    else:
        print("Unrecognized command. Please type 'Create' or 'Load'")

Q1 = Quest.Quest(C1)
Q1.addTask()
Q1.addTask()
Q1.addReward()
Q1.completeTask(1)
Q1.showTasks()
Q1.completeQuest()
C1.stats()