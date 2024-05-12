let wordList = document.querySelector("#word-list");
let sentence = document.querySelector("#sentence");

wordList.addEventListener("click", event => {
  let word = event.target.textContent;
  sentence.textContent += word;
  sentence.textContent += " ";
});

let box = document.querySelector("#box");


document.querySelector("html").addEventListener("mousemove", e => {
    // console.log(`mousemove x: ${e.clientX}, y: ${e.clientY}`);
    box.style.left = e.clientX + "px";
    box.style.top = e.clientY + "px";

  });

document.querySelector("html").addEventListener("keydown", e => {
  console.log(e);
});
