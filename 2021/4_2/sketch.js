let boards = [];
let boardsTmp;
let numbersTmp;
let numbers;

let boardId = null;
let bestMove = null;
let lastNumber;
let bestLastNumber = 0;
let sumNotSelected = 0;
let split = 5;

//gehe jedes Board durch und prüfe wann / ob Bingo erreicht wird
//wenn ja, dann prüfe was das bisherige Beste Ergebnis war
//wenn das aktuelle Ergebnis kleiner ist, dann überschreibe den die Werte
//Board; Zug ; letzte Zahl; summe Aller nicht getroffenen Zahlen

//Resultat letzte Zahl * Summe nicht getroffener Zahlen

function preload() {
  //load numbers
  //load boards
  boardsTmp = loadStrings("boards.txt");
  numbersTmp = loadStrings("numbers.txt");
}

function setup() {
  createCanvas(400, 400);

  setupBoards();
  setupNumbers();

  for (let i = 0; i < boards.length; i++) {
    processBoard(i);
  }


  //console.log(bestlastNumber);
  console.log(bestlastNumber * sumNotSelected);

  //results
}

function processBoard(id) {
  let moves = 0;
  let check = false;
  for (let i = 0; i < numbers.length; i++) {
    moves++;
    //Nummer markieren
    for (let pos = 0; pos < boards[id].length; pos++) {

      if (str(boards[id][pos][0]) == str(numbers[i])) {
        boards[id][pos][1] = 1;
        console.log("BoardZahl " + boards[id][pos][0]);
        lastNumber = boards[id][pos][0];

        break;
      } else {
        //console.log("nicht gefunden");
      }
      //wenn i >=5

      if (i >= 4) {
        //console.log("moves " + moves);
        check = checkBoardBingo(id);

        //(Performance)Prüfen ob umliegende Zahlen bereits getroffen wurden
        //Boardprüfung aufrufen (columns und rows)
      }
      if (check) {
        console.log("Bingo in " + moves + " moves");
        console.log(lastNumber);
        if (bestMove == null || moves > bestMove) {
          bestMove = moves;
          console.log("bestMove " + bestMove);
          bestlastNumber = lastNumber;
          console.log("bestlastNumber " + bestlastNumber);
          sumNotSelected = getSumNotSelected(id);
          console.log("sumNotSelected " + sumNotSelected);
        }
        break;
      }
    }

    if (check) { break; }
  }

  //console.log(boards);
  //console.log(bestMove);
}

function checkBoardBingo(id) {

  //check Columns

  for (let column = 0; column < 5; column++) {
    let count = 0;
    for (let row = 0; row < 25; row += split) {
      //console.log(count);

      if (boards[id][column + row][1] == 1) {
        count++;
        //console.log("treffer");

        if (count == 5) {

          return true;

        }

      }

    }

  }

  //check Rows
  for (let row = 0; row < 21; row += split) {
    let count = 0;
    for (let column = 0; column < 5; column++) {
      //console.log(count);

      if (boards[id][column + row][1] == 1) {
        count++;
        //console.log("treffer");

        if (count == 5) {

          return true;

        }

      }



    }
    //console.log("break");
  }

  return false;
}

function getSumNotSelected(id) {
  let sum = 0;
  for (let i = 0; i < boards[id].length; i++) {
    if (boards[id][i][1] == 0) {
      sum += int(boards[id][i][0]);
    }
  }
  return sum;
}

function setupNumbers() {
  numbers = numbersTmp[0].split(",");
  console.log(numbers);
}

function setupBoards() {
  //transform to 2d array boards
  for (let i = 0; i < boardsTmp.length; i++) {
    boards[i] = boardsTmp[i].split(",");
  }
  for (let i = 0; i < boards.length; i++) {
    for (let x = 0; x < boards[i].length; x++) {
      boards[i][x] = [boards[i][x], 0];
    }
  }
  console.log(boards[0]);

}

function draw() {
  background(220);
}
