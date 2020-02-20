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
#
# GUI
# At some point I want to implement a GUI for this code but for now it is just via command line
# in a bash shell. I'd like the GUI to have the look of a scroll, have tabs for character,
# quests, and maybe other things like a map, inventory, and motivational quotes.

# Errors to deal with:
# Integer inputs not being integers.
# Trying to complete a task that's already complete.
# Trying to complete a quest that's already complete. (Done)
# Trying to complete a task that doesn't exist.
# Trying to complete a quest that doesn't exist.

import Character
import Quest

def createQuest(C1, counterGL1):
    
    # Needs to edit the Questlog.html file to display this quest.
    
    QuestList.append(Quest.Quest(C1))
    print("How many tasks in this quest?")
    TNum = input()
    TNum = int(TNum)
    for i in range(TNum):
        QuestList[counterGL1].addTask()
    QuestList[counterGL1].addReward()
    counterGL1 += 1
    return counterGL1

print('Welcome to the Game of Life')
print("Type 'Create' to create a character or 'Load' to load a character")
QuestList = []
loop_varGL1 = 0
while(loop_varGL1 == 0):
    option1 = input()
    if (option1 == 'Create'):
        print("Name: ")
        name = input()
        print("Age: ")
        age = input()
        C1 = Character.Character(name, age, 0, 0, 0, 0, 0, 0)
        loop_varGL1 = 1
    elif (option1 == 'Load'):
        print("Load Character")
        loop_varGL1 = 1
    else:
        print("Unrecognized command. Please type 'Create' or 'Load'")

loop_varGL2 = 0
counterGL1 = 0
while(loop_varGL2 == 0):
    print("\nWhat would you like to do?\n'1. Create Quest', '2. Show Quests', '3. Complete Quest Task', '4. Complete Quest', '5. Save', '6 .Exit'")
    print("'7. Show Stats', '8. Show Completed Quests'")
    option2 = input()
    if (option2 == 'Exit' or option2 == '6'):
        loop_varGL2 = 1
    elif (option2 == 'Create Quest' or option2 == '1'):
        counterGL1 = createQuest(C1, counterGL1);
        
    elif (option2 == 'Show Quests' or option2 == '2'):
        print("")
        for i,quest in enumerate(QuestList):
            if (not quest.isCompleted()):
                print("{i} ".format(i=i + 1) + quest.questDescription())
                quest.showTasks()
    elif (option2 == 'Complete Quest Task' or option2 == '3'):
        print("Enter Quest Number:")
        QNum = input()
        QNum = int(QNum) - 1
        print("Enter Task Number")
        TNum = input()
        TNum = int(TNum)
        QuestList[QNum].completeTask(TNum)
    elif (option2 == 'Complete Quest' or option2 == '4'):
        print("Enter Quest Number")
        QNum = input()
        QNum = int(QNum) - 1
        QuestList[QNum].completeQuest()
    elif (option2 == 'Show Stats' or option2 == '7'):
        C1.stats()
    elif (option2 == 'Show Completed Quests' or option2 == '8'):
        for i,quest in enumerate(QuestList):
            if (quest.isCompleted()):
                print("{i} ".format(i=i + 1) + quest.questDescription())
                quest.showTasks()
    elif (option2 == 'Save' or option2 == '5'):
        print("Not implemented yet.")
        #savefile = open("")
    else:
        print("Unrecognized command.")
    
    
