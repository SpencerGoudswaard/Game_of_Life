function createQuest() {
	var currentList = document.getElementById("QuestList").innerHTML
	document.getElementById("QuestList").innerHTML = currentList + "\t\t<li>Quest 1</li>\n\t\t<ul>\n\t\t\t<li>Task 1</li>\n\t\t</ul>\n\t\t<p class='CompleteQuest'>Complete Quest</p>\n";
}

/* function completeQuest(var questNum) {
	var currentQuest = document.getElementById("").innerHTML
} */

function createCharacter() {
	document.getElementById("Test").innerHTML = "\t<form>\n\tCharacter Name:\n\t<input type='text'></input> Age:\n\t<input type='text'></input>\n\t<input type='submit'></input>\n\t</form>"
}

function loadCharacter(){
	document.getElementById("Test").innerHTML = "Test Load"
}