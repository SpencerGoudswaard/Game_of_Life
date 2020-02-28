var numQuests = 0;
var taskNum = new Array();
var Quests = new Array();

/* This function creates a new Quest.
 Currently it just changes the html code but the goal is to have it create a new 'quest' object with parameters (description, quest number, number of tasks, rewards) with methods to change the description, add/remove tasks, add rewards, complete the quest, and remove the quest.
 The parameters should be originally set by a form that the opens on a button click and the user fills in and submits.
*/
function createQuest(){
	numQuests += 1;
	taskNum[numQuests] = 1;
	var currentList = document.getElementById("QuestList").innerHTML
	document.getElementById("QuestList").innerHTML = currentList + "<li id=Quest"+ numQuests +">Quest "+ numQuests +"</li>";
	var currentQuest = document.getElementById("Quest"+ numQuests).innerHTML
	document.getElementById("Quest"+ numQuests).innerHTML = currentQuest + "\n<ul id = taskList"+ numQuests +">\n<input type='checkbox' name='task' value='task1'>Task 1</input><br></ul>\n<button type='button' onclick='addTask("+numQuests+")' id='AddTask"+ numQuests +"'>Add Task</button>\n<p class='CompleteQuest'>Complete Quest</p>\n";
	
}

/* Creating a Quest object. */
function Quest(description, questNum, numTasks, FitExp = 0, ConExp = 0, WisExp = 0, IntExp = 0, ChaExp = 0, ExplExp = 0, InspExp = 0){
	this.description = description;
	this.questNum = questNum;
	this.numTasks = numTasks;
	this.FitExp = FitExp;
	this.ConExp = ConExp;
	this.WisExp = WisExp;
	this.IntExp = IntExp;
	this.ChaExp = ChaExp;
	this.ExplExp = ExplExp;
	this.InspExp = InspExp;
}

/* This function will eventually be replaced by a method in the Quest object. */
function addTask(questNum){
	taskNum[questNum] += 1;
	var currentTask = document.getElementById("taskList"+ questNum).innerHTML
	currentTask = document.getElementById("taskList"+ questNum).innerHTML = currentTask + "<input type='checkbox' name='task' value='task"+taskNum[questNum]+"'>Task "+taskNum[questNum]+"</input><br>";
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