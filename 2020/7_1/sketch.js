let input
let counter = 0;


function preload() {
  //input = loadStrings("input.txt");
  input = loadStrings("inputTest.txt");

}

function setup() {
  createCanvas(400, 400);

  inputProcessed = processInput("shiny gold");
  console.log(inputProcessed);
  //console.log(input);

  while (inputProcessed.length > 0) {
    //for each result in the results array call processInput with the result into a temp array
    //then add the temp array to the inputProcessed array
    inputProcessed = inputProcessed.concat(processInput(inputProcessed[0]));
  }
  console.log(inputProcessed);
  console.log(counter - 1);
}






//find each line which includes given value and add the text before the first "bags" to the results array
//then counter++
//then delete the entire line with the value at the beginning from input and this result
//Then clean result form trailing spaces
//Then add it to the results and return the results
function processInput(value) {
  let results = [];
  for (let i = 0; i < input.length; i++) {
    if (input[i].includes(value)) {
      counter++;
      results.push(input[i].substring(0, input[i].indexOf("bags")));
      input.splice(i, 1);
      i--;
    }
  }
  for (let i = 0; i < results.length; i++) {
    results[i] = results[i].trim();
  }
  //remove entry "shiny gold" from results
  results.splice(results.indexOf(value), 1);

  return results;
}


function draw() {

  background(220);

}
