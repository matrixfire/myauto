// 1, Basic structures


document.addEventListener('DOMContentLoaded', () => {
    // Some code here
});

array.forEach(function(element, index, array) {
    // Code to execute for each element
});



// 2, some basics

let counter = 0;
function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`)
    }
}


document.querySelector('form').onsubmit = function() {
    const button = document.querySelector('button');
    const head = document.querySelector('#hello');
    head.style.color = button.dataset.color;

    const name = document.querySelector('#name').value;
    alert(`Hello, ${name}`);
};



document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('select').onchange = (event) => {
        document.querySelector('#hello').style.color = event.target.value;
    }
});

// 3, events

onsubmit
onclick
onmouseover
onkeydown
onload
onblur
onchange 
