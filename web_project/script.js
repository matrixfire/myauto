document.addEventListener('click', function (event) {
    var isClickInside = document.querySelector('.main-menu').contains(event.target);
    if (!isClickInside) {
        var dropdowns = document.querySelectorAll('.dropdown-menu, .flyout-menu');
        dropdowns.forEach(function (dropdown) {
            dropdown.style.display = 'none';
        });
    }
});

document.querySelectorAll('.dropdown, .flyout').forEach(function (menu) {
    menu.addEventListener('mouseover', function () {
        menu.querySelector('.dropdown-menu, .flyout-menu').style.display = 'block';
    });

    menu.addEventListener('mouseout', function () {
        menu.querySelector('.dropdown-menu, .flyout-menu').style.display = 'none';
    });
});
