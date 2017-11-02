//look here : http://www.makeuseof.com/tag/python-javascript-communicate-json/
//https://www.youtube.com/watch?v=geKvJbQsOmM&t=427s
//http://jsfiddle.net/n8j1s/4y22135r/

//The game board 1 = walls, 0 = free space, and -1 = the goal
window.addEventListener('mousemove', mousePos, false);

var canvas = $('#GameBoardCanvas');
var canvasElement = document.getElementById("GameBoardCanvas");
var data = [];
var board = [];
var width;
var widthArray;
var heightArray;
var blockSize;
var height;
var clickReady;
var xblock;
var yblock;
var endCoordinate;
var startCoordinate;

function getMaze(){
    //getting the data from pyhton
    console.log("The python is now asked to return the array")
    var getData = $.get('/data');

    //Check if python is done
    getData.done(function(results){
    data = results.results;
    board = data;

    //Draw the game board
    draw();
    canvasElement.addEventListener("click", edit);
    });
}

function setupCanvas(){
        width = ($("#grid").width());
        widthArray = board[0].length;
        heightArray = board.length;
        blockSize = width/widthArray;
        height = blockSize * heightArray;

        console.log(width,widthArray,heightArray,blockSize,height)

        document.getElementById("GameBoardCanvas").height = height;
        document.getElementById("GameBoardCanvas").width = width;
//        document.getElementById("GameBoardCanvas").style.borderWidth = `${blockSize}px`;
}

function draw(){

      console.log("Draw");

        //check if board has data other wise show loading image
         if (board.length > 0 ){
            $("#grid").show();
            $("#load").hide();
         } else {
            $("#grid").hide();
            $("#load").show();
         }

        setupCanvas();

        var ctx = canvas[0].getContext('2d');
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, width, width);
        ctx.fillStyle="black";

        //Loop through the board array drawing the walls and the goal
        for(var y = 0; y < board.length; y++){
            for(var x = 0; x < board[y].length; x++){
                //Draw a wall
                if(board[y][x] === 1){
                    ctx.fillRect(x*blockSize, y*blockSize, blockSize, blockSize);
                }
                //Draw the goal
                else if(board[y][x] === -1){
                    ctx.beginPath();
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = "red";
                    ctx.moveTo(x*blockSize, y*blockSize);
                    ctx.lineTo((x+1)*blockSize, (y+1)*blockSize);
                    ctx.moveTo(x*blockSize, (y+1)*blockSize);
                    ctx.lineTo((x+1)*blockSize, y*blockSize);
                    ctx.stroke();
                }

                //Start
                else if(board[y][x] === -2){
                    ctx.beginPath();
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = "green";
                    ctx.moveTo(x*blockSize, y*blockSize);
                    ctx.lineTo((x+1)*blockSize, (y+1)*blockSize);
                    ctx.moveTo(x*blockSize, (y+1)*blockSize);
                    ctx.lineTo((x+1)*blockSize, y*blockSize);
                    ctx.stroke();
                }


                //Draw the visited
                else if(board[y][x] === 2){
                    ctx.fillStyle="gray";
                    ctx.fillRect(x*blockSize, y*blockSize, blockSize, blockSize);
                    ctx.fillStyle="black";

                }

                //Draw the path
                else if(board[y][x] === 3){
                    ctx.fillStyle="blue";
                    ctx.fillRect(x*blockSize, y*blockSize, blockSize, blockSize);
                    ctx.fillStyle="black";
                }

            }
        }
    }

function mousePos(e) {
          var pos = getCoordinates(canvasElement, e);
        }

function getCoordinates(canvasElement, evt) {

          var rect = canvasElement.getBoundingClientRect(), // abs. size of element
          scaleX = canvasElement.width / rect.width, // relationship bitmap vs. element for X
          scaleY = canvasElement.height / rect.height; // relationship bitmap vs. element for Y

            var mx = (evt.clientX - rect.left) * scaleX; // scale mouse coordinates after they have
            var my = (evt.clientY - rect.top) * scaleY; // been adjusted to be relative to element


           //check if mouse poss is in canvas
          if (mx >= 0 && mx <= canvasElement.width && my >= 0 && my <= canvasElement.height){
            var widthArr = board[0].length;
            var heightArr = board.length;

            var mappingx = (canvasElement.width / widthArr)* scaleX;
            var mappingy = (canvasElement.height / heightArr)* scaleY;


            xblock = Math.floor(mx/mappingx);
            yblock = Math.floor(my/mappingy);

            console.log("x: "+xblock);
            console.log("y: "+yblock);

//            console.log("x block: "+xblock);
//            console.log("y block: "+yblock);

            clickReady =true;
            } else {
            clickReady =false;
            }
        }

function edit(){
    console.log("er is geklikt");
    //First check if edit mode is set
    console.log("editmode: "+editMode);

    if (!editMode == 0){
        if (clickReady){
            if (editMode == 1){
                var currentVal = board[yblock][xblock]
                if(currentVal >= 1){
                board[yblock][xblock]=0;
                }
                if(currentVal < 1){
                board[yblock][xblock]=1;
                }
                draw();
            }
            if (editMode == -1){
                var currentVal = board[yblock][xblock]

                if (currentVal == 0){
                    if (typeof endCoordinate !== 'undefined'){
                    board[endCoordinate["y"]][endCoordinate["x"]]= 0;
                    }

                    endCoordinate = {y:yblock, x:xblock};
                    board[yblock][xblock]=-1;
                    draw();
                }
            }
            if (editMode == -2){
                var currentVal = board[yblock][xblock]

                if (currentVal == 0){
                    if (typeof startCoordinate !== 'undefined'){
                    board[startCoordinate["y"]][startCoordinate["x"]]= 0;
                    }

                    startCoordinate = {y:yblock, x:xblock};
                    board[yblock][xblock]=-2;
                    draw();
                }
            }
        }
    }
}




// canvasElement.addEventListener("click",function(){
//            console.log("clicked");
//            board[yblock][xblock]=-2;
//            draw();
//            });












