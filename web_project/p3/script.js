// Get the canvas and its drawing context
let canvas = document.querySelector("#canvas");
let ctx = canvas.getContext("2d");

// Set the width and height of the canvas
let width = canvas.width;
let height = canvas.height;

// Initial position of the circle
let x = 0;
let y = 0;

// Function to draw a circle at position (x, y)
function drawCircle(x, y) {
  ctx.fillStyle = "rgb(0, 128, 255)"; // Set the circle color to blue
  ctx.beginPath(); // Start drawing a shape
  ctx.arc(x, y, 10, 0, Math.PI * 2, false); // Draw a circle with radius 10
  ctx.fill(); // Fill the circle with the blue color
}

// Function to update the position of the circle
function update() {
  x += 1; // Move the circle to the right
  y += 1; // Move the circle down
}

// Function to clear the canvas and draw the updated circle
function draw() {
  ctx.clearRect(0, 0, width, height); // Clear the canvas
  drawCircle(x, y); // Draw the circle at the new position
}

// Set up the animation loop to run every 100 milliseconds
setInterval(() => {
  update(); // Update the circle's position
  draw(); // Draw the new frame
}, 10);
