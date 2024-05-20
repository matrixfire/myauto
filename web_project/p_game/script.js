// Class to handle the game view and rendering
class GameView {
  constructor() {
      let canvas = document.querySelector("#canvas"); // Select the canvas element
      this.ctx = canvas.getContext("2d"); // Get the 2D drawing context
      this.width = canvas.width; // Canvas width
      this.height = canvas.height; // Canvas height
      this.offsetTop = canvas.offsetTop; // Canvas offset from the top of the viewport
  }

  draw(...entities) {
      // Fill the canvas with black
      this.ctx.fillStyle = "black";
      this.ctx.fillRect(0, 0, this.width, this.height);

      // Draw each entity (ball, paddles)
      entities.forEach(entity => entity.draw(this.ctx));
  }

  drawScores(scores) {
      this.ctx.fillStyle = "white";
      this.ctx.font = "30px monospace";
      this.ctx.textAlign = "left";
      this.ctx.fillText(scores.leftScore.toString(), 50, 50); // Draw left score
      this.ctx.textAlign = "right";
      this.ctx.fillText(scores.rightScore.toString(), this.width - 50, 50); // Draw right score
  }

  drawGameOver() {
      this.ctx.fillStyle = "white";
      this.ctx.font = "30px monospace";
      this.ctx.textAlign = "center";
      this.ctx.fillText("GAME OVER", this.width / 2, this.height / 2); // Draw game over text
  }
}

// Base class for game entities (ball and paddles)
class Entity {
  constructor(x, y, width, height) {
      this.x = x; // x position
      this.y = y; // y position
      this.width = width; // width of the entity
      this.height = height; // height of the entity
  }

  boundingBox() {
      // Return the bounding box of the entity
      return {
          left: this.x,
          right: this.x + this.width,
          top: this.y,
          bottom: this.y + this.height
      };
  }

  draw(ctx) {
      // Draw the entity as a white rectangle
      ctx.fillStyle = "white";
      ctx.fillRect(this.x, this.y, this.width, this.height);
  }
}

// Class for paddle entities
class Paddle extends Entity {
  static WIDTH = 5;
  static HEIGHT = 20;
  static OFFSET = 10;

  constructor(x, y) {
      super(x, y, Paddle.WIDTH, Paddle.HEIGHT); // Call the parent constructor
  }
}

// Class for the ball entity
class Ball extends Entity {
  static SIZE = 5;

  constructor() {
      super(0, 0, Ball.SIZE, Ball.SIZE); // Call the parent constructor
      this.init(); // Initialize the ball position and speed
  }

  init() {
      this.x = 20; // Initial x position
      this.y = 30; // Initial y position
      this.xSpeed = 4; // Horizontal speed of the ball
      this.ySpeed = 2; // Vertical speed of the ball
  }

  update() {
      this.x += this.xSpeed; // Update x position
      this.y += this.ySpeed; // Update y position
  }

  adjustAngle(distanceFromTop, distanceFromBottom) {
      if (distanceFromTop < 0) {
          // If ball hit near top of paddle, reduce ySpeed
          this.ySpeed -= 0.5;
      } else if (distanceFromBottom < 0) {
          // If ball hit near bottom of paddle, increase ySpeed
          this.ySpeed += 0.5;
      }
  }

  checkPaddleCollision(paddle, xSpeedAfterBounce) {
      let ballBox = this.boundingBox();
      let paddleBox = paddle.boundingBox();

      // Check if the ball and paddle overlap vertically and horizontally
      let collisionOccurred = (
          ballBox.left < paddleBox.right &&
          ballBox.right > paddleBox.left &&
          ballBox.top < paddleBox.bottom &&
          ballBox.bottom > paddleBox.top
      );

      if (collisionOccurred) {
          let distanceFromTop = ballBox.top - paddleBox.top;
          let distanceFromBottom = paddleBox.bottom - ballBox.bottom;
          this.adjustAngle(distanceFromTop, distanceFromBottom);
          this.xSpeed = xSpeedAfterBounce; // Update xSpeed based on collision
      }
  }

  checkWallCollision(width, height, scores) {
      let ballBox = this.boundingBox();

      // Hit left wall
      if (ballBox.left < 0) {
          scores.rightScore++;
          this.init(); // Reset ball position
      }
      // Hit right wall
      if (ballBox.right > width) {
          scores.leftScore++;
          this.init(); // Reset ball position
      }
      // Hit top or bottom walls
      if (ballBox.top < 0 || ballBox.bottom > height) {
          this.ySpeed = -this.ySpeed; // Reverse y direction
      }
  }
}

// Class to handle game scores
class Scores {
  constructor() {
      this.leftScore = 0; // Initial left player score
      this.rightScore = 0; // Initial right player score
  }
}

// Class to control the computer paddle
class Computer {
  static followBall(paddle, ball) {
      const MAX_SPEED = 2; // Maximum speed of the paddle
      let ballBox = ball.boundingBox();
      let paddleBox = paddle.boundingBox();

      if (ballBox.top < paddleBox.top) {
          paddle.y -= MAX_SPEED; // Move paddle up
      } else if (ballBox.bottom > paddleBox.bottom) {
          paddle.y += MAX_SPEED; // Move paddle down
      }
  }
}

// Main game class
class Game {
  constructor() {
      this.gameView = new GameView();
      this.ball = new Ball();
      this.leftPaddle = new Paddle(Paddle.OFFSET, 10);
      this.rightPaddle = new Paddle(
          this.gameView.width - Paddle.OFFSET - Paddle.WIDTH,
          30
      );
      this.scores = new Scores();
      this.gameOver = false;

      // Event listener to update right paddle position based on mouse movement
      document.addEventListener("mousemove", e => {
          this.rightPaddle.y = e.y - this.gameView.offsetTop;
      });
  }

  draw() {
      // Draw the ball and paddles
      this.gameView.draw(
          this.ball,
          this.leftPaddle,
          this.rightPaddle
      );

      // Draw the scores
      this.gameView.drawScores(this.scores);
  }

  checkCollision() {
      // Check collisions with the paddles
      this.ball.checkPaddleCollision(this.leftPaddle, Math.abs(this.ball.xSpeed));
      this.ball.checkPaddleCollision(this.rightPaddle, -Math.abs(this.ball.xSpeed));

      // Check collisions with the walls
      this.ball.checkWallCollision(
          this.gameView.width,
          this.gameView.height,
          this.scores
      );

      // Check if game over condition is met
      if (this.scores.leftScore > 9 || this.scores.rightScore > 9) {
          this.gameOver = true;
      }
  }

  update() {
      this.ball.update(); // Update ball position
      Computer.followBall(this.leftPaddle, this.ball); // Move computer paddle
  }

  loop() {
      this.draw(); // Draw the game
      this.update(); // Update game state
      this.checkCollision(); // Check for collisions

      if (this.gameOver) {
          this.draw(); // Draw final game state
          this.gameView.drawGameOver(); // Display game over message
      } else {
          // Call this method again after a timeout to continue the game loop
          setTimeout(() => this.loop(), 30);
      }
  }
}

// Create a new game instance and start the game loop
let game = new Game();
game.loop();
