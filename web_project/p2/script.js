let canvas = document.querySelector("#canvas");
let ctx = canvas.getContext("2d");
// ctx.fillStyle = "blue";
// ctx.fillRect(10, 10, 200, 100);



ctx.lineWidth = 2;

ctx.strokeStyle = "red";
ctx.strokeRect(10, 10, 200, 100);


ctx.strokeStyle = "orange";
ctx.strokeRect(20, 20, 180, 80);

ctx.strokeStyle = "yellow";
ctx.strokeRect(30, 30, 160, 60);

ctx.strokeStyle = "green";
ctx.strokeRect(40, 40, 140, 40);

ctx.strokeStyle = "blue";
ctx.strokeRect(50, 50, 120, 20);
