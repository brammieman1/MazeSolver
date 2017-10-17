document.getElementById("camera").onclick = callPython;
document.getElementById("trash").onclick = callPython;
document.getElementById("edit").onclick = callPython;
document.getElementById("erase").onclick = callPython;
document.getElementById("undo").onclick = callPython;
document.getElementById("redo").onclick = callPython;
document.getElementById("start").onclick = callPython;


function callPython(){
	console.log(this.id);


	if (this.id == "camera"){
		document.getElementById("maze").src = "/video_feed";
	}

	if (this.id == "start"){
		document.getElementById("maze").src = "https://camo.githubusercontent.com/fe94d9aba32c8683e6f5acfeddcf153577fd8051/687474703a2f2f6e756c6c70726f6772616d2e636f6d2f696d672f706174682f6d617a652e676966";
	    //$("#Pimage").show();
	}

	if (this.id == "edit"){
		document.getElementById("maze").src = "/static/image.jpg";

	}

	var dest = '/';
	dest += this.id;

	$.ajax({
		type: "GET",
		url: dest,
	});
}