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
    if (input.value !== "") {
        // submit_btn.disabled = false;
        empty = false;
    }

    if (empty == false) {
        submit_btn.disabled = false;
    }

    else {
        submit_btn.disabled = true;
    }
});

// add_user_form.addEventListener("submit", (e) => {
//     event.preventDefault(e)
//     event.stopPropagation(e)
// });

// Set enter key to send message
document.querySelector("#chat_input").addEventListener("keypress", (event) => {
    if (event.key == "Enter") {
        document.querySelector("#chat_button").click();
    }
});

// create list for rooms
let room_pairs = []
// Create room variable
let room;
let friend_id;

// the current chat we're in
const current_chat = document.querySelector("#current_chat");


//  beginning of  Socket Implementation
var socket = io.connect("http://localhost:5000");

socket.on('connect', function () {
    socket.send("Connected!");
    console.log("Hello");
});

// User sending a message
document.querySelector("#chat_button").onclick = function () {
    console.log(room);
    let input = document.querySelector("#chat_input");
    socket.send({ "msg": input.value, "user_ID": user_ID, "room": room, "friend_id": friend_id, "friend_username": current_chat.innerHTML});
    input.value = "";
}

// previous messages event
socket.on("previous messages", function (data) {
    for (message of data) {
        let p = document.createElement("p");
        let br = document.createElement("br");
        p.innerHTML = message["message"] + br.outerHTML;
        document.querySelector("#chat").append(p);
    }
});

let chatid_list = [];
// all the existing active chats
// chats = document.querySelectorAll(".chats .friends_id");
for (let chat of document.querySelectorAll(".chats .friends_id")) {
    chatid_list.push(parseInt(chat.innerHTML));
}

console.log(chatid_list);

// message event. We can't
socket.on("message", function (data) {
    // Vanilla Javascript
    // append a new message
    if (current_chat.innerHTML == data["friend_username"]) {
        let p = document.createElement("p");
        let br = document.createElement("br");
        p.innerHTML = data["msg"] + br.outerHTML;
        document.querySelector("#chat").append(p);
    }

    if (!chatid_list.includes(data["friend_id"])) {

        let newchat = `<div class="block chats">` +
            `<img class="imgBox" src="https://avatars.dicebear.com/api/human/123.svg">`
            + `<div class="details">` +
            `<div class="listHead">` +
            `<h4>${current_chat.innerHTML}</h4>` +
            `<h4 hidden class="friends_id">${data["friend_id"]}</h4>`
            + `</div>`
            + `</div>` +
            `</div>`;

        document.querySelector("#chat_id").innerHTML += newchat;

    }
});


// room selection AND Clicking on a new chat
document.querySelectorAll(".block").forEach(friend => {
    friend.addEventListener("click", () => {
        // Get the name of current chat
        // const current_chat = document.querySelector("#current_chat");
        // current_chat = document.querySelector("#current_chat");
        current_chat.innerHTML = friend.querySelector("h4").innerHTML;

        // Get the friends ID to chat with
        friend_id = friend.querySelector(".friends_id").innerHTML;
        console.log(friend_id);

        // convert users and friends ID to int
        users_User_ID = parseInt(user_ID);
        friend_id = parseInt(friend_id);

        // calculate unique value for a room for user and friend
        room = uniqueRoom(users_User_ID, friend_id);

        // convert unique value to string
        room = room.toString();

        // Join the room
        joinRoom(room);

    });
});

// Create functions for leave room, join room and system message
function leaveRoom(room) {
    socket.emit("leave", { "user_ID": user_ID, "room": room });
}

function joinRoom(room) {
    socket.emit("join", { "user_ID": user_ID, "friend_id": friend_id, "room": room });
    // clear chat section
    document.querySelector("#chat").innerHTML = ""
}

// this function creates a unique number from two numbers using a modified cantor pairing function
function uniqueRoom(id_1, id_2) {
    return ((id_1 + id_2 + 1) * (id_1 + id_2) / 2) + (id_1 * id_2);
}

// function systemMessage(msg){
//     // Display a system message
//     const p = document.createElement("p");
//     p.innerHTML = msg;
//     document.querySelector("#chat").append(p);
// }

// Add Event Listener to friend profile button
document.querySelector("#friend_profile_button").onclick = () => {
    // Pass friend's username to backend bucket
    socket.emit("friend profile", current_chat.innerHTML);
}

socket.on("friend profile", (data) => {
    // Get profile fields from DOM
    document.querySelector("#friend_name").innerHTML = data["name"];
    document.querySelector("#friend_username").innerHTML = data["username"];
    document.querySelector("#friend_email").innerHTML = data["email"];
    document.querySelector("#friend_phone_number").innerHTML = data["phone_number"];

    // Check if user has a bio
    if (data["bio"] == "empty"){
        document.querySelector("#friend_bio").innerHTML = 'Some place holder text if bio is "empty"';
    }
    else{
        document.querySelector("#friend_bio").innerHTML = data["bio"]
    }
});