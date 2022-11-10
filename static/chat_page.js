// Listen for complete page load
document.addEventListener("DOMContentLoaded", () => {
    // Get users data from database
    let users = document.querySelector("#users").getAttribute("data-users");

    // Get the add user form node from DOM
    let add_user_form = document.querySelector("#addcontact");

    // Get input field in the form node
    let input = add_user_form.querySelector("input");

    // Get the submit btn in the form node
    let submit_btn = add_user_form.querySelector("button[type='submit']");

    // Disable submit button
    submit_btn.disabled = true;

    // Listen for keyboard input in input field
    input.addEventListener("keyup", () => {
        //
        let empty = true;

        // Check if the input field is empty
        if (input.value !== ""){
            // submit_btn.disabled = false;
            empty = false;
        }

        if (empty == false){
            submit_btn.disabled = false;
        }

        else{
            submit_btn.disabled = true;
        }
    });

    // add_user_form.addEventListener("submit", (e) => {
    //     event.preventDefault(e)
    //     event.stopPropagation(e)
    // });
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