// Get the canvas element and its 2D drawing context
let canvas = document.querySelector("#canvas");
let ctx = canvas.getContext("2d");

// Store the canvas width and height for easy access
let width = canvas.width;
let height = canvas.height;

// Define constants for game settings
const MAX_COMPUTER_SPEED = 2; // Maximum speed the computer paddle can move
const BALL_SIZE = 5; // Size of the ball

// Variables to store ball position and speed
let ballPosition;
let xSpeed;
let ySpeed;

// Initialize ball position and speed
function initBall() {
  ballPosition = { x: 20, y: 30 }; // Starting position of the ball
  xSpeed = 4; // Horizontal speed of the ball
  ySpeed = 2; // Vertical speed of the ball
}

// Define constants for paddle settings
const PADDLE_WIDTH = 5; // Width of the paddles
const PADDLE_HEIGHT = 20; // Height of the paddles
const PADDLE_OFFSET = 10; // Distance from the edge to the paddles

// Variables to store paddle positions
let leftPaddleTop = 10;
let rightPaddleTop = 30;

// Variables to store scores
let leftScore = 0;
let rightScore = 0;

// Variable to track if the game is over
let gameOver = false;

// Event listener to update the right paddle position based on mouse movement
document.addEventListener("mousemove", e => {
  rightPaddleTop = e.y - canvas.offsetTop;
});

// Function to draw the game elements on the canvas
function draw() {
  // Clear the canvas by filling it with black
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, width, height);

  // Set the color to white for drawing the ball and paddles
  ctx.fillStyle = "white";

  // Draw the ball
  ctx.fillRect(ballPosition.x, ballPosition.y, BALL_SIZE, BALL_SIZE);

  // Draw the left paddle
  ctx.fillRect(PADDLE_OFFSET, leftPaddleTop, PADDLE_WIDTH, PADDLE_HEIGHT);

  // Draw the right paddle
  ctx.fillRect(width - PADDLE_WIDTH - PADDLE_OFFSET, rightPaddleTop, PADDLE_WIDTH, PADDLE_HEIGHT);

  // Draw the scores
  ctx.font = "30px monospace";
  ctx.textAlign = "left";
  ctx.fillText(leftScore.toString(), 50, 50);
  ctx.textAlign = "right";
  ctx.fillText(rightScore.toString(), width - 50, 50);
}

// Function to control the computer paddle to follow the ball
function followBall() {
  let ball = { top: ballPosition.y, bottom: ballPosition.y + BALL_SIZE };
  let leftPaddle = { top: leftPaddleTop, bottom: leftPaddleTop + PADDLE_HEIGHT };

  if (ball.top < leftPaddle.top) {
    leftPaddleTop -= MAX_COMPUTER_SPEED; // Move paddle up
  } else if (ball.bottom > leftPaddle.bottom) {
    leftPaddleTop += MAX_COMPUTER_SPEED; // Move paddle down
  }
}

// Function to update the ball position and move the computer paddle
function update() {
  ballPosition.x += xSpeed;
  ballPosition.y += ySpeed;
  followBall();
}

// Function to check if the ball collides with a paddle
function checkPaddleCollision(ball, paddle) {
  return (
    ball.left < paddle.right &&
    ball.right > paddle.left &&
    ball.top < paddle.bottom &&
    ball.bottom > paddle.top
  );
}

// Function to adjust the ball's angle based on where it hits the paddle
function adjustAngle(distanceFromTop, distanceFromBottom) {
  if (distanceFromTop < 0) {
    ySpeed -= 0.5; // Hit near top of paddle, reduce vertical speed
  } else if (distanceFromBottom < 0) {
    ySpeed += 0.5; // Hit near bottom of paddle, increase vertical speed
  }
}

// Function to check all collisions and handle scoring
function checkCollision() {
  let ball = {
    left: ballPosition.x,
    right: ballPosition.x + BALL_SIZE,
    top: ballPosition.y,
    bottom: ballPosition.y + BALL_SIZE
  };
  let leftPaddle = {
    left: PADDLE_OFFSET,
    right: PADDLE_OFFSET + PADDLE_WIDTH,
    top: leftPaddleTop,
    bottom: leftPaddleTop + PADDLE_HEIGHT
  };
  let rightPaddle = {
    left: width - PADDLE_WIDTH - PADDLE_OFFSET,
    right: width - PADDLE_OFFSET,
    top: rightPaddleTop,
    bottom: rightPaddleTop + PADDLE_HEIGHT
  };

  // Check collision with left paddle
  if (checkPaddleCollision(ball, leftPaddle)) {
    let distanceFromTop = ball.top - leftPaddle.top;
    let distanceFromBottom = leftPaddle.bottom - ball.bottom;
    adjustAngle(distanceFromTop, distanceFromBottom);
    xSpeed = Math.abs(xSpeed); // Ensure the ball bounces to the right
  }

  // Check collision with right paddle
  if (checkPaddleCollision(ball, rightPaddle)) {
    let distanceFromTop = ball.top - rightPaddle.top;
    let distanceFromBottom = rightPaddle.bottom - ball.bottom;
    adjustAngle(distanceFromTop, distanceFromBottom);
    xSpeed = -Math.abs(xSpeed); // Ensure the ball bounces to the left
  }

  // Check if the ball hits the left wall
  if (ball.left < 0) {
    rightScore++;
    initBall(); // Reset the ball position and speed
  }

  // Check if the ball hits the right wall
  if (ball.right > width) {
    leftScore++;
    initBall(); // Reset the ball position and speed
  }

  // Check if the game is over
  if (leftScore > 9 || rightScore > 9) {
    gameOver = true;
  }

  // Check if the ball hits the top or bottom wall
  if (ball.top < 0 || ball.bottom > height) {
    ySpeed = -ySpeed; // Reverse vertical direction
  }
}

// Function to draw the "Game Over" message
function drawGameOver() {
  ctx.fillStyle = "white";
  ctx.font = "30px monospace";
  ctx.textAlign = "center";
  ctx.fillText("GAME OVER", width / 2, height / 2);
}

// Main game loop function
function gameLoop() {
  draw();
  update();
  checkCollision();

  if (gameOver) {
    draw();
    drawGameOver();
  } else {
    setTimeout(gameLoop, 30); // Continue the game loop
  }
}

// Initialize the ball and start the game loop
initBall();
gameLoop();
