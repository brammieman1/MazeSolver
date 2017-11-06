document.getElementById("camera").onclick = callPython;
document.getElementById("picture").onclick = callPython;
document.getElementById("convert").onclick = callPython;
document.getElementById("edit").onclick = callPython;
document.getElementById("save").onclick = callPython;
document.getElementById("delete").onclick = callPython;
document.getElementById("start").onclick = callPython;
document.getElementById("startp").onclick = callPython;
document.getElementById("endp").onclick = callPython;
document.getElementById("history").onclick = callPython;
document.getElementById("zoom").onclick = callPython;
document.getElementById("startpXL").onclick = callPython;
document.getElementById("endpXL").onclick = callPython;
document.getElementById("editXL").onclick = callPython;
//document.getElementById("convert").disabled = true;
document.getElementById("convert").disabled = false;

$('.dropdown-inverse li > a').click(function(e){
    var str = this.innerHTML;

    if (str == "PI Breadth-first Search" ){
    selectedAlgoritm = 0;
    }
    if (str == "PI A* Search" ){
    selectedAlgoritm = 1;
    }
    if (str == "FPGA Greedy Search" ){
    selectedAlgoritm = 2;
    }

    $('.status').text(this.innerHTML);
});




$('#myModal').on('hidden.bs.modal', function(e) {
editMode = 0;
getMazeSM();
});

$("#startMsg").show();
$("#maze").hide();
$("#grid").hide();
$("#load").hide();

var editMode = 0;
var solutionBlock = false;
var XL = false;
var selectedAlgoritm = 0;
var DBdata = [];
var picId= 0;

function callPython(){
	console.log(this.id);

	if (this.id == "camera"){
	    document.getElementById("convert").disabled = true;
	    editMode = 0;
	    document.getElementById("maze").src = "/static/loadingcam.png";
		document.getElementById("maze").src = "/video_feed";
		$("#maze").show();
		$("#grid").hide();
		$("#load").hide();
		$("#startMsg").hide();
	}


	if (this.id == "edit" ||this.id == "editXL"){
	    editMode = 1;
	}

	if (this.id == "startp" || this.id == "startpXL"){
	    editMode = -2;
	}

	if (this.id == "endp" || this.id == "endpXL"){
	    editMode = -1;
	}

	if (this.id == "zoom"){
	    editMode = 1;
	    getMazeXL();
	}

    if (this.id == "save"){


        var fname = prompt("Please enter a name:", "");
        if (fname == null || fname == "") {
          alert("No name given, Image NOT saved!");
        } else {
        console.log(fname);
        filename = fname;
	    var postName = $.post( "/saveMaze", {
        name: filename
        });
        }

	}

	if (this.id == "delete"){

	    if (pid != 0){
	    var postDelete = $.post( "/deleteMaze", {
        mid: picId
        });
	    }

	}

    if (this.id == "history"){
    var getData = $.get('/DBdata');
        //Check if python is done
        getData.done(function(DBresults){
        DBdata = DBresults.DBresults;
        myItemList = $('#myDropdown .dropdown-menu');
            //clear contents of dropdown
            myItemList.html('');
            //iterate array and create dropdown links
            $(DBdata).each(function(index, element){
                var item = ('<li><a href="#" id="'+element[2]+'">'+element[0]+'</a></li>');
                myItemList.append(item);
            });

            $('.dropdown-db li > a').click(function(e){
                picId = this.id;

                //hide all on screen
                //show loader
                editMode = 0;
                $("#load").show();

               //hide all
                $("#maze").hide();
                $("#grid").hide();
                $("#startMsg").hide();


                var postPid = $.post( "/puzzelPath", {
                pid: picId
                });

                postPid.done(function(pPath){
                console.log(pPath["pPath"][0]);

                var file = pPath["pPath"][0];


                document.getElementById("maze").src = file+'?t=' + new Date().getTime();
                $("#load").hide();
                $("#maze").show();
                document.getElementById("convert").disabled = false;

                console.log("Saved Image is loaded!")
                })

            });



        });
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
