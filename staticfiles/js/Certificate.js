/*scroll navbar*/
window.addEventListener("scroll", function () {
    var nav = document.querySelector("#mainNav");
    if (window.scrollY > 50) {
        nav.classList.add("navbar-scrolled");
    } else {
        nav.classList.remove("navbar-scrolled");
    }
});


/*navbar dropdown hover*/
function showDropdown(element) {
    var dropdownMenu = element.querySelector('.dropdown-menu');
    dropdownMenu.classList.add('show');
}

function hideDropdown(element) {
    var dropdownMenu = element.querySelector('.dropdown-menu');
    dropdownMenu.classList.remove('show');
}



window.onload = function () {
    var arrow = document.getElementById('arrow');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 20) {
            arrow.style.display = "block";
        } else {
            arrow.style.display = "none";
        }
    });


    arrow.onclick = function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };
};




$.noConflict();
$(document).ready(function () {

    $('#tableSearch').DataTable();
});





//    var class3Value = parseInt('{{owner_form.class3}}');
//    var iconElement = document.getElementById('class3_checkbox');
//
//    if (class3Value === 1) {
//
//        iconElement.style.display = 'inline';
//    } else {
//
//        iconElement.style.display = 'none';
//    }

function displayIcon() {
    var inputValue = document.getElementById("Model").value; // Get the current value of the input
    var iconElement = document.getElementById("class3_icon"); // Get the icon element

    if(inputValue === "1") {
        // If the input value is "1", show the icon
        iconElement.style.display = "inline-block"; // Change this to "block" or "inline" as per your layout needs
    } else {
        // If the input value is anything else, hide the icon
        iconElement.style.display = "none";
    }
}