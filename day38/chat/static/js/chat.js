const messageInputElem = document.querySelector("#new_message");
const messageLogElem = document.querySelector(".chat_log");

document.querySelector("#send_button").addEventListener("click", newMessageHandler);
messageInputElem.addEventListener("keypress", (evt) => {
    if (evt.key === 'Enter') newMessageHandler();
});

function newMessageHandler() {
    if (messageInputElem.value === "") {
        alert("Please enter a message!");
        return;
    }

    // Doesn't make sense to send a message if the sender or the message is blank
    fetch("/new_message", {
        method: "post",
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify({ text: messageInputElem.value })
    })
        .then(res => res.json())
        .then(res => {
            // if (res.message == "OK") window.location.reload();
            if (res.message == "OK") {
                messageInputElem.value = "";
                getNewMessages();
            }
            else alert(res.message);
        });
}

function getNewMessages() {
    fetch("/all_messages")
        .then(res => res.json())
        .then(processNewMessages)  // Same as above, without the intermediate function.
}
getNewMessages();  // Run initial time.

// Loop through each message to create a giant HTML string, and then add it to the UI.
function processNewMessages(all_messages) {
    // console.log("processNewMessages:", all_messages);
    let new_html = "";
    all_messages.forEach(message => {
        new_html += `
                <div class="message ${message.user === currUser ? "my_message" : "their_message"}">
                    <div class="message_header">
                        <div class="message_sender">${message.user}</div>
                        <div class="message_datetime">${message.time}</div>
                    </div>
                    <div class="message_text">${message.text}</div>
                </div>
                `;
    });
    messageLogElem.innerHTML = new_html;

    // Scroll to the bottom of the chat log area.
    messageLogElem.scrollTop = messageLogElem.scrollHeight;

    setTimeout(getNewMessages, 5000);  // 30sec timeout.
}
