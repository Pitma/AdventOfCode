var grid = [];
var cellSize = 10;
var cols, rows;
var snakeLine;
var snake;
var dir;
var speed;
var target;
var targetCount;
var points;

function setup() {
  createCanvas(500, 500);
  cols = int(width / cellSize);
  rows = int(height / cellSize);

  for (i = 0; i < rows; i++) {
    for (j = 0; j < cols; j++) {
      var c = new Cell(i * cellSize, j * cellSize);
      grid.push(c);
    }
  }

}



function draw() {
    background(0);


  };





