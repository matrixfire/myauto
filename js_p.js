// 1, Basic structures


document.addEventListener('DOMContentLoaded', () => {
    // Some code here
});

array.forEach(function(element, index, array) {
    // Code to execute for each element
});

document.querySelector('h1')


const li = document.createElement('li');
document.querySelector('#tasks').append(li);


setInterval(count, 1000);

localStorage.getItem(key)
localStorage.setItem(key, value)
 
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


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('select').onchange = function() {
        document.querySelector('#hello').style.color = this.value;
    }
});


document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('select').onchange = (event) => {
        document.querySelector('#hello').style.color = event.target.value;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // Send a GET request to the URL
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        // Put response into json form
        .then(response => response.json())
        .then(data => {
            // Get currency from user input and convert to upper case
            const currency = document.querySelector('#currency').value.toUpperCase();

            // Get rate from data
            const rate = data.rates[currency];

            // Check if currency is valid:
            if (rate !== undefined) {
                // Display exchange on the screen
                document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
            }
            else {
                // Display error on the screen
                document.querySelector('#result').innerHTML = 'Invalid Currency.';
            }
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.log('Error:', error);
        });
        // Prevent default submission
        return false;
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


// 4, properties and methods

.value
.value.length
.innerHTML