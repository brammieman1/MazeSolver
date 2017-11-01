var canvas = $('#GameBoardCanvas');

var data = [];
//look here : http://www.makeuseof.com/tag/python-javascript-communicate-json/
//https://www.youtube.com/watch?v=geKvJbQsOmM&t=427s
//http://jsfiddle.net/n8j1s/4y22135r/


//The game board 1 = walls, 0 = free space, and -1 = the goal

var getData = $.get('/data');

getData.done(function(results){
data = results.results;
console.log(data);
var board = data;

var player = {
    x: 0,
    y: 0
};

//Draw the game board
function draw(){

//check if board has data other wise show loading image
     if (board.length > 0 ){
        $("#GameBoardCanvas").show();
        $("#load").hide();
     } else {
        $("#GameBoardCanvas").hide();
        $("#load").show();
     }



    // set canvas properties
    //var width = canvas.width();

    var width = (($("#canvasSize").width())/100)*90;

    console.log(width);

    var widthArray = board[0].length;
    var heightArray = board.length;
    var blockSize = width/widthArray;
    var height = blockSize * heightArray;


    document.getElementById("GameBoardCanvas").height = height;
    document.getElementById("GameBoardCanvas").width = width;
    document.getElementById("GameBoardCanvas").style.borderWidth = `${blockSize}px`;




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
        }
    }
    //Draw the player
    ctx.beginPath();
    var half = blockSize/2;
    ctx.fillStyle = "green";
    ctx.arc(player.x*blockSize+half, player.y*blockSize+half, half, 0, 2*Math.PI);
    ctx.fill();
}

//Check to see if the new space is inside the board and not a wall
function canMove(x, y){
    return (y>=0) && (y<board.length) && (x >= 0) && (x < board[y].length) && (board[y][x] != 1);
}

$(document).keyup(function(e){
    if((e.which == 38) && canMove(player.x, player.y-1))//Up arrow
        player.y--;
    else if((e.which == 40) && canMove(player.x, player.y+1)) // down arrow
        player.y++;
    else if((e.which == 37) && canMove(player.x-1, player.y))
        player.x--;
    else if((e.which == 39) && canMove(player.x+1, player.y))
        player.x++;
    draw();
    e.preventDefault();
});

draw();
});


