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

// Set enter key to send message
document.querySelector("#chat_input").addEventListener("keypress", (event) => {
    if (event.key == "Enter"){
        document.querySelector("#chat_button").click();
    }
});

// create list for rooms
let room_pairs = []
// Create room variable
let room;

//  beginning of  Socket Implementation
var socket = io.connect("http://localhost:5000");

socket.on('connect', function() {
    socket.send("Connected!");
    console.log("Hello");
});

document.querySelector("#chat_button").onclick = function() {
    let input = document.querySelector("#chat_input");
    socket.send({"msg": input.value, "user_ID": user_ID, "room": room});
    input.value = "";
}

// message event
socket.on("message", function(data) {
    // Vanilla Javascript
    let p = document.createElement("p");
    let br = document.createElement("br");
    p.innerHTML = data["msg"] + br.outerHTML;
    document.querySelector("#chat").append(p);
});


// room selection AND Clicking on a new chat
document.querySelectorAll(".block").forEach(friend => {
    friend.addEventListener("click", () => {
        // set the name of current chat
        const current_chat = document.querySelector("#current_chat");
        current_chat.innerHTML = friend.querySelector("h4").innerHTML;
        friend_id = friend.querySelector(".friends_id").innerHTML;

        // If a room already exists
        if (room_pairs.includes(user_ID + friend_id) || room_pairs.includes(friend_id + user_ID) ){
            alert("already exists");
            // console.log(room_pairs);
            // leaveRoom(room);
            joinRoom(rooms);
        }
        //create a new room
        else{
            let newRoom = user_ID + friend_id; 109
            if (!room_pairs.includes(newRoom)){
                room_pairs.push(newRoom);
            }
            // room_pairs.push(newRoom);
            // alert(room_pairs);
            console.log(room_pairs);
            leaveRoom(room);
            joinRoom(newRoom);
            room = newRoom;
        }

        // let newRoom = current_chat.innerHTML;
        // if (newRoom == room){
        //     msg = `You dey this room already boss!`
        //     systemMessage(msg);
        // }
        // else {
        //     leaveRoom(room);
        //     joinRoom(newRoom);
        //     room = newRoom;
        // }
    });
});

// Create functions for leave room, join room and system message
function leaveRoom(room){
    socket.emit("leave", {"user_ID": user_ID, "room": room});
}

function joinRoom(room){
    socket.emit("join", {"user_ID": user_ID, "room": room});
    // clear chat section
    document.querySelector("#chat").innerHTML = ""
}

function systemMessage(msg){
    const p = document.createElement("p");
    p.innerHTML = msg;
    document.querySelector("#chat").append(p);
}
