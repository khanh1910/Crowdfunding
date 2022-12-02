document.getElementById("conect_bank").onclick = function(){
	document.getElementById("popup").style.opacity = "100%";
	document.getElementById("popup").style.pointerEvents = "all";
}

document.getElementById("close_popup").onclick = function(){
	document.getElementById("popup").style.opacity = "0";
	document.getElementById("popup").style.pointerEvents = "none";
}