const images = [];
const target = 75;
let current = 0;
let currentCoord = 0;
let result = "image,x1,y1,x2,y2,x3,y3";

let x1 = null;
let y1 = null;
let x2 = null;
let y2 = null;
let x3 = null;
let y3 = null;

function setup() {
  createCanvas(144 * 4, 96 * 4);
  for (let i = 0; i < target; i++)
    images.push(loadImage(`./inputs/${i}.jpg`));
}

function nextStep() {
  if (current + 1 <= target) {
    logCSV();
    current++;
    currentCoord = 0;
  } else {
    console.log(result);
  }
}

function draw() {
  background(0, 0, 0);
  noStroke();
  ellipseMode(CENTER);
  if (current < target) {
    image(images[current], 0, 0, width, height);
    if (currentCoord > 0) {
      fill(255, 0, 0);
      ellipse(x1 * 4, y1 * 4, 5, 5);
    }
    if (currentCoord > 1) {
      fill(0, 255, 0);
      ellipse(x2 * 4, y2 * 4, 5, 5);
    }
    if (currentCoord > 2) {
      fill(0, 0, 255);
      ellipse(x3 * 4, y3 * 4, 5, 5);
    }
  }
}

function mousePressed() {
  if (currentCoord === 0) {
    x1 = mouseX / 4;
    y1 = mouseY / 4;
  }
  if (currentCoord === 1) {
    x2 = mouseX / 4;
    y2 = mouseY / 4;
  }
  if (currentCoord === 2) {
    x3 = mouseX / 4;
    y3 = mouseY / 4;
  }
  if (currentCoord >= 3) {
    nextStep();
  } else {
    currentCoord++;
  }
}

function logCSV() {
  result += `\n${current+1},${x1},${y1},${x2},${y2},${x3},${y3}`;
  console.log(`${current + 1}/${target}`);
}
