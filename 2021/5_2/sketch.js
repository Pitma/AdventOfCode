let linesTmp;
let lines = [];
let dots = [];



function preload() {
  //linesTmp = loadStrings("lines.txt");
  linesTmp = loadStrings("linesTest.txt");
  console.log(linesTmp);
}

function setup() {
  createCanvas(400, 400);

  lines = generateLines();
  console.log(lines);

  dots = generateDots();

  console.log(dots);
  //results

  console.log(getAmountOfDots());

}
//return amount of dots with count > 1
function getAmountOfDots() {
  let amount = 0;
  for (let i = 0; i < dots.length; i++) {
    if (dots[i].count > 1) {
      amount++;
    }
  }
  return amount;
}



//generate class lines with start and end point (start [x,y], end [x,y])
function generateLines() {
  let lines = [];
  let start = [0, 0];
  let end = [0, 0];
  for (let i = 0; i < linesTmp.length; i++) {
    let line = linesTmp[i].split(" ");
    start[0] = parseInt(line[0].split(",")[0]);
    start[1] = parseInt(line[0].split(",")[1]);
    end[0] = parseInt(line[1].split(",")[0]);
    end[1] = parseInt(line[1].split(",")[1]);
    lines.push(new Line(start[0], start[1], end[0], end[1]));
  }
  return lines;
}

//generate dots between start and end point for each line (start [x,y], end [x,y]) and
//add them to the dots array
//the movement x and y is always 1
//if the dot is already in the array, add 1 to the count of the dot, else add a new dot
function generateDots() {
  let dots = [];
  for (let i = 0; i < lines.length; i++) {
    let start = lines[i].start;
    let end = lines[i].end;
    let x = start.x;
    let y = start.y;
    let xEnd = end.x;
    let yEnd = end.y;
    let xDiff = xEnd - x;
    let yDiff = yEnd - y;
    let xMove = 0;
    let yMove = 0;
    console.log(xDiff, yDiff, start, end);
    if (xDiff < 0) {
      xMove = -1;
    }
    if (yDiff < 0) {
      yMove = -1;
    }
    if (xDiff > 0) {
      xMove = 1;
    }
    if (yDiff > 0) {
      yMove = 1;
    }
    //if dot is not horizontal or vertical do nothing
    //if (xDiff != 0 && yDiff != 0) {
    //  console.log("not horizontal or vertical");
    // } else {



    while (x != xEnd || y != yEnd) {

      //break when 2 dots are in the array
      if (dots.length > 2000000) {
        break;
      }
      let dot = new Dot(x, y);
      //check if dot is already in the array with the same x and y value
      let index = dots.findIndex(function (element) {
        return element.x == dot.x && element.y == dot.y;
      });
      if (index > -1) {
        dots[index].count++;
        console.log("dot already in array");
      } else {
        dots.push(dot);
      }
      x += xMove;
      y += yMove;

    }
    //add last dot
    let dot = new Dot(x, y);
    let index = dots.findIndex(function (element) {
      return element.x == dot.x && element.y == dot.y;
    });
    if (index > -1) {
      dots[index].count++;
      console.log("dot already in array");
    }
    else {
      dots.push(dot);
    }
    //}
  }
  return dots;
}



//class dot
function Dot(x, y) {
  this.x = x;
  this.y = y;
  this.count = 1;
}

//generate class line with start and end point (start, end)
class Line {
  constructor(startx, starty, endx, endy) {
    this.start = createVector(startx, starty);
    this.end = createVector(endx, endy);
  }
}


function draw() {

  //move canvas to center
  translate(width / 2, height / 2);

  background(220);
  //show dots grid and count how often each dot is called, add 20 px to the x and y value
  for (let i = 0; i < dots.length; i++) {
    fill(0);
    ellipse(dots[i].x * 20, dots[i].y * 10, 5, 5);
    text(dots[i].count, dots[i].x * 10, dots[i].y * 10);
  }
}
