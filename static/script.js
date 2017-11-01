document.getElementById("camera").onclick = callPython;
document.getElementById("picture").onclick = callPython;
document.getElementById("convert").onclick = callPython;
document.getElementById("edit").onclick = callPython;
document.getElementById("save").onclick = callPython;
document.getElementById("delete").onclick = callPython;
document.getElementById("start").onclick = callPython;

$("#startMsg").show();
$("#maze").hide();
$("#GameBoardCanvas").hide();
$("#load").hide();


function callPython(){
	console.log(this.id);


	if (this.id == "camera"){
		document.getElementById("maze").src = "/video_feed";
		$("#maze").show();
		$("#GameBoardCanvas").hide();
		$("#load").hide();
		$("#startMsg").hide();
	}

	if (this.id == "picture"){
        document.getElementById("maze").src = "/static/wait.jpg";

	    $("#maze").show();
		$("#GameBoardCanvas").hide();
		$("#load").hide();
		$("#startMsg").hide();

	    //get the picture taken
	    var getSnap = $.get('/snapshot');
	    getSnap.done(function(snapshot){
            data = snapshot.snapshot;
            console.log(data);
            document.getElementById("maze").src = data;
        })

	}

	if (this.id == "convert"){
	    $("#GameBoardCanvas").hide();
        $("#maze").hide();
        $("#startMsg").hide();
        $("#load").show();
	    getMaze()
	}


	if (this.id == "start"){
		document.getElementById("maze").src = "https://camo.githubusercontent.com/fe94d9aba32c8683e6f5acfeddcf153577fd8051/687474703a2f2f6e756c6c70726f6772616d2e636f6d2f696d672f706174682f6d617a652e676966";
	    $("#maze").show();
	    $("#GameBoardCanvas").hide();
	    $("#load").hide();
	    $("#startMsg").hide();
	}



	var dest = '/';
	dest += this.id;

	$.ajax({
		type: "GET",
		url: dest,
	});
}