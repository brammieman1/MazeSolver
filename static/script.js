document.getElementById("camera").onclick = callPython;
document.getElementById("picture").onclick = callPython;
document.getElementById("convert").onclick = callPython;
document.getElementById("edit").onclick = callPython;
document.getElementById("save").onclick = callPython;
document.getElementById("delete").onclick = callPython;
document.getElementById("start").onclick = callPython;
document.getElementById("startp").onclick = callPython;
document.getElementById("endp").onclick = callPython;
//document.getElementById("convert").disabled = true;
document.getElementById("convert").disabled = false;

$("#startMsg").show();
$("#maze").hide();
$("#grid").hide();
$("#load").hide();

var editMode = 0;

function callPython(){
	console.log(this.id);

	if (this.id == "camera"){
	    editMode = 0;
	    document.getElementById("maze").src = "/static/loadingcam.png";
		document.getElementById("maze").src = "/video_feed";
		$("#maze").show();
		$("#grid").hide();
		$("#load").hide();
		$("#startMsg").hide();
	}


	if (this.id == "edit"){
	    editMode = 1;
	}

	if (this.id == "startp"){
	    editMode = -2;
	}

	if (this.id == "endp"){
	    editMode = -1;
	}

	if (this.id == "picture"){
	    editMode = 0;
        document.getElementById("maze").src = "/";
        //show loading
        $("#load").show();

       //hide all
        $("#maze").hide();
		$("#grid").hide();
		$("#startMsg").hide();

	    //get the picture taken
	    var getSnap = $.get('/snapshot');
	    getSnap.done(function(snapshot){
            data = snapshot.snapshot;
            console.log(data);
            document.getElementById("maze").src = "/static/images/output.jpg?t=" + new Date().getTime();
            $("#load").hide();
            $("#maze").show();
            document.getElementById("convert").disabled = false;
        })

	}

	if (this.id == "convert"){
	    editmode = 0;
	    $("#grid").hide();
        $("#maze").hide();
        $("#startMsg").hide();
        $("#load").show();
	    getMaze();
	}


	if (this.id == "start"){
	    editmode = 0;

	    if((typeof endCoordinate !== 'undefined')&& (typeof startCoordinate !== 'undefined')){

        console.log("hier komt de data");
	        console.log(board);
            var sendmaze;

	    $.post( "/sendMaze", {
            maze: JSON.stringify(board),
            startx: startCoordinate["x"],
            starty: startCoordinate["y"],
            endx: endCoordinate["x"],
            endy: endCoordinate["y"],
            });

	    document.getElementById("maze").src = "https://camo.githubusercontent.com/fe94d9aba32c8683e6f5acfeddcf153577fd8051/687474703a2f2f6e756c6c70726f6772616d2e636f6d2f696d672f706174682f6d617a652e676966";
	    $("#maze").show();
	    $("#grid").hide();
	    $("#load").hide();
	    $("#startMsg").hide();
	    } else{
	    alert("Select start and end point")
	    }
	}



	var dest = '/';
	dest += this.id;

	$.ajax({
		type: "GET",
		url: dest,
	});
}
