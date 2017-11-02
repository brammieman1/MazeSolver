document.getElementById("camera").onclick = callPython;
document.getElementById("picture").onclick = callPython;
document.getElementById("convert").onclick = callPython;
document.getElementById("edit").onclick = callPython;
document.getElementById("save").onclick = callPython;
document.getElementById("delete").onclick = callPython;
document.getElementById("start").onclick = callPython;
document.getElementById("startp").onclick = callPython;
document.getElementById("endp").onclick = callPython;
document.getElementById("convert").disabled = true;
//document.getElementById("convert").disabled = false;

$("#startMsg").show();
$("#maze").hide();
$("#grid").hide();
$("#load").hide();

var editMode = 0;
var solutionBlock = false;

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

	    document.getElementById("edit").disabled = false;
        document.getElementById("startp").disabled = false;
        document.getElementById("endp").disabled = false;
        document.getElementById("start").disabled = false;
        solutionBlock = false;
	}


	if (this.id == "start"){
	    editmode = 0;


	    if((typeof endCoordinate !== 'undefined')&& (typeof startCoordinate !== 'undefined')){
        $("#grid").hide();
        $("#maze").hide();
        $("#startMsg").hide();
        $("#load").show();
        getSolution();

        solutionBlock = true;
        document.getElementById("edit").disabled = true;
        document.getElementById("startp").disabled = true;
        document.getElementById("endp").disabled = true;
        document.getElementById("start").disabled = true;


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
