//
document.addEventListener("DOMContentLoaded", () => {
    // Get the add user form node from DOM
    add_user_form = document.querySelector("#addcontact");

    // Get input field in the form node
    input = add_user_form.querySelector("input");

    // Get the submit btn in the foem node 
    submit_btn = add_user_form.querySelector("#add_user_btn");

    // DIsable submit button
    submit_btn.disabled = true;

    // Listen for keyboard input in input field
    input.addEventListener("keyup", () => {
        // Check if the input field is empty
        if (input.value !== ""){
            submit_btn.disabled = false;
        }

        else{
            submit_btn.disabled = true;
        }


    });
});









// /* javascript file for the chat_page */

// // form that adds new contacts / friends
// let form = document.getElementById("addcontact");

// // prevent the page from submitting
// form.addEventListener('submit', event => {
//     event.preventDefault();
// });

// //
// document.getElementById("cancel").onclick = function () {

//     form.style.display = "none";
//     document.getElementById("contacts").style.display = "inline";
//     document.getElementById("contactform").style.display = "inline";

// }

// document.getElementById("contactform").onclick = function () {
//     form.style.display = "inline";
//     document.getElementById("contactform").style.display = "none";
//     document.getElementById("contacts").style.display = "none";

// }

// document.getElementById("dismiss").onclick = function () {
//     form.style.display = "none";
//     document.getElementById("contactform").style.display = "inline";
//     document.getElementById("contacts").style.display = "inline";

// }


// // for some reason turning it into a funtion does not allow it to work
// /*
// function() form_control {

//     form.style.display = "inline";
//     document.getElementById("contactform").style.display = "none";
//     document.getElementById("contacts").style.display = "none";

// }


// document.getElementById("contactform").onclick = form_control();
// document.getElementById("dismiss").onclick = form_control();
// */