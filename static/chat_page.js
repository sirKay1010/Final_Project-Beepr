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


// Socket Implementation
var socket = io.connect("http://localhost:5000");
socket.on('connect', function() {
    socket.send("Connected!");
    console.log("Hello");
});

socket.on("message", function(data) {
    // Vanilla Javascript
    // let p = document.createElement("p");
    // document.querySelector("#chat").append(p.innerHTML = data);

    // Ibrahims Research script
    // document.querySelector("#chat").append(`<p> + data + </p>`);

    // jQuery
    $("#chat").append($("<p>").text(data));
});

document.querySelector("#chat_button").onclick = function() {
    let input = document.querySelector("#chat_input");
    socket.send(input.value);
    input.value = "";
    console.log(data)
};