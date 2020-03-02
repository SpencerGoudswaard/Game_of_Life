var numQuests = 0;
var taskNum = 0;
var Quests = new Array();

/* This function creates a new Quest.
 Currently it just changes the html code but the goal is to have it create a new 'quest' object with parameters (description, quest number, number of tasks, rewards) with methods to change the description, add/remove tasks, add rewards, complete the quest, and remove the quest.
 The parameters should be originally set by a form that the opens on a button click and the user fills in and submits.
*/
function createQuest(){
	numQuests += 1;
	taskNum[numQuests] = 1;
	var currentList = document.getElementById("QuestList").innerHTML;
	
	/* Gets quest info from user form. */
	var description = document.getElementById("description").value;
	var FitExp = document.getElementById("fitExp").value;
	var ConExp = document.getElementById("conExp").value;
	var WisExp = document.getElementById("wisExp").value;
	var IntExp = document.getElementById("intExp").value;
	var ChaExp = document.getElementById("chaExp").value;
	var ExplExp = document.getElementById("explExp").value;
	var InsExp = document.getElementById("insExp").value;
	
	/* Adds new quest to the Quests array */
	Quests.push(new Quest(description, numQuests, 1, FitExp, ConExp, WisExp, IntExp, ChaExp, ExplExp, InsExp))

	/* Prints the quest to the QuestLog */
	document.getElementById("QuestList").innerHTML = currentList + "<li id=Quest"+ numQuests +">"+ Quests[numQuests-1].description +"</li>";
	
	/* Prints the tasks to the QuestLog */
	var currentQuest = document.getElementById("Quest"+ numQuests).innerHTML
	document.getElementById("Quest"+ numQuests).innerHTML = currentQuest + "\n<ul class ='TaskList' id = TaskList"+ numQuests +">\n</ul><button type='button' class='CompleteQuest'>Complete Quest</button>\n"
	
	/* document.getElementById("Quest"+ numQuests).innerHTML = currentQuest + "\n<ul class ='TaskList' id = TaskList"+ numQuests +">\n<input type='checkbox' name='task' value='task1'>Task 1</input><br></ul>\n<button type='button' onclick='addTask("+numQuests+")' id='AddTask"+ numQuests +"'>Add Task</button>\n<button type='button' class='CompleteQuest'>Complete Quest</button>\n"; */
	document.getElementById("CreateQuestContainer").reset();
	var currentTask = document.getElementById("Tasks").innerHTML = "<div id='break0'></div>";
	taskNum = 0;
	
}

/* Quest object */
function Quest(description, questNum, taskList, FitExp, ConExp, WisExp, IntExp, ChaExp, ExplExp, InsExp){
	this.numTasks = 0;
	this.description = description;
	this.questNum = questNum;
	this.taskList = taskList;
	this.addTask = function (taskDesc){
		taskList.push(taskDesc);
		this.numTasks += 1;
	}
	this.FitExp = FitExp;
	this.ConExp = ConExp;
	this.WisExp = WisExp;
	this.IntExp = IntExp;
	this.ChaExp = ChaExp;
	this.ExplExp = ExplExp;
	this.InsExp = InsExp;
}

/* This function will eventually be replaced by a method in the Quest object. */
function addTask(){
	taskNum += 1;
	var currentTask = document.getElementById("Tasks").innerHTML
	var tempTaskString = "<label for='task"+ taskNum +"'><b>Task "+ taskNum +"</b></label>\n<input type='text' id='task"+ taskNum +"'><br id='break"+ taskNum +"'>"
	document.getElementById("break"+(taskNum-1)).insertAdjacentHTML("afterend", tempTaskString);
}


/* This function will eventually be replaced by a method in the Quest object. */
/* function completeQuest(var questNum) {
	var currentQuest = document.getElementById("").innerHTML;
} */



function createCharacter(){
	document.getElementById("FormSpot").innerHTML = "<form id='CreateCharacter' onsubmit='return false;'>\n\tCharacter Name:\n\t<input type='text' id='username'></input>\n\t<input type='submit' onclick='newCharacter()'></input>\n\t</form>";
}

function newCharacter(){
	var Username = document.getElementById("username").value;
	document.getElementById("User").innerHTML = Username;
}

function loadCharacterIn(){
	var Username = document.getElementById("username").value;
	document.getElementById("User").innerHTML = "Loaded: " + Username;
	
}

function loadCharacter(){
	document.getElementById("FormSpot").innerHTML = "<form id='LoadCharacter' onsubmit='return false;'>\n\tCharacter Name:\n\t<input type='text' id='username'></input>\n\t<input type='submit' onclick='loadCharacterIn()'></input>\n\t</form>";
}

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}