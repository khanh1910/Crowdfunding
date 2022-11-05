document.getElementById("next1").onclick = function(){
	document.getElementById("form1").style.left = "-1000px";
	document.getElementById("form2").style.left = "20px";
	document.getElementById("form3").style.left = "450px"
	document.getElementById("process").style.width = "200px";
}

document.getElementById("back2").onclick = function(){
	document.getElementById("form1").style.left = "20px";
	document.getElementById("form2").style.left = "450px";
	document.getElementById("process").style.width = "100px";
}

document.getElementById("next2").onclick = function(){
	document.getElementById("form1").style.left = "-450px";
	document.getElementById("form2").style.left = "-450px";
	document.getElementById("form3").style.left = "20px"
	document.getElementById("process").style.width = "290px";
}

document.getElementById("back3").onclick = function(){
	document.getElementById("form1").style.left = "-450px";
	document.getElementById("form2").style.left = "20px";
	document.getElementById("form3").style.left = "450px"
	document.getElementById("process").style.width = "200px";
}

// document.getElementById("submit").onclick = function(){
// 	location.assign("{% url 'poster' %}");
// }