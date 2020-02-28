var numQuests = 0;
var taskNum = new Array();

/* This function creates a new Quest.
 Currently it just changes the html code but the goal is to have it create a new 'quest' object with parameters (description, quest number, number of tasks) with methods to change the description, add/remove tasks, add rewards, complete the quest, and remove the quest.
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

/* This function will eventually be replaced by a method in the Quest object. */
function addTask(questNum){
	taskNum[questNum] += 1;
	var currentTask = document.getElementById("taskList"+ questNum).innerHTML
	currentTask = document.getElementById("taskList"+ questNum).innerHTML = currentTask + "<input type='checkbox' name='task' value='task"+taskNum[questNum]+"'>Task "+taskNum[questNum]+"</input><br>";
}

/* This function will eventually be replaced by a method in the Quest object. */
/* function completeQuest(var questNum) {
	var currentQuest = document.getElementById("").innerHTML
} */



function createCharacter(){
	document.getElementById("Test").innerHTML = "\t<form>\n\tCharacter Name:\n\t<input type='text'></input> Age:\n\t<input type='text'></input>\n\t<input type='submit'></input>\n\t</form>"
}

function loadCharacter(){
	document.getElementById("Test").innerHTML = "Test Load"
}