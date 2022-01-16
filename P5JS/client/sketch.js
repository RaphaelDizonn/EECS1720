var r;
var g;
var b


function setup() {
  createCanvas(400, 400);
}

function draw() {
   r = random(255); 
  g = random(255)
  b = random(255); 
 
  background(0, 0, 0)
  
  if (mouseIsPressed) {
fill(r, g, b);
  } else {
    fill(255);
  }
  rect(mouseX, mouseY, 80, 80);

}