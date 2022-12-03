document.getElementById("conect_bank").onclick = function(){
	document.getElementById("popup").style.opacity = "100%";
	document.getElementById("popup").style.pointerEvents = "all";
}

document.getElementById("close_popup").onclick = function(){
	document.getElementById("popup").style.opacity = "0";
	document.getElementById("popup").style.pointerEvents = "none";
}

document.getElementById("polices").onclick = function(){
	document.getElementById("frame_polices").style.opacity = "100%";
	document.getElementById("frame_polices").style.pointerEvents = "all";
}

document.getElementById("close_polices").onclick = function(){
	document.getElementById("frame_polices").style.opacity = "0";
	document.getElementById("frame_polices").style.pointerEvents = "none";
}

document.getElementById("facebook_block").onclick = function(){
	alert("Comming soon");
}
document.getElementById("google_block").onclick = function(){
	alert("Comming soon");
}