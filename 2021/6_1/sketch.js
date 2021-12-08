let inputTmp;
let fishs = [];
let done = false;
const cycles = 80;



function preload() {
  //inputTmp = loadStrings("input.txt");
  inputTmp = loadStrings("inputTest.txt");


}

function setup() {
  noLoop();
  //createCanvas(400, 400);
  console.log(inputTmp);
  readInput();

  if (!done) {
    //for cycles go through all fishs and update their age
    for (let i = -1; i < cycles; i++) {

      //go through fishs array and update their age
      for (let j = 0; j < fishs.length; j++) {
        fishs[j].ageFish();
      }

    }
    done = true;
  }

  console.log(fishs.length);


}

//process inputTmp and return array of fishs age split by comma
function readInput() {
  let input = inputTmp[0].split(",");
  for (let i = 0; i < input.length; i++) {
    let age = input[i];
    fishs.push(new Fish(age));
  }
  return fishs;
}


//generate fish class with age
class Fish {
  constructor(age) {
    this.age = age;
    this.ready = false;

  }

  //function to age fish by reducing age by 1
  //if age is below 0 , set age to 6 and add a new fish to the array with age 8
  ageFish() {
    if (this.ready) {
      this.age--;
    }
    this.ready = true;
    if (this.age < 0) {
      this.age = 6;
      fishs.push(new Fish(8));
    }
  }
}



function draw() {
  background(220);



}
