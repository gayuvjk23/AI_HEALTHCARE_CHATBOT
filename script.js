async function sendMessage() {

    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if(message === "") return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user-message">
            <b>You:</b> ${message}
        </div>
    `;

    input.value = "";

    chatBox.innerHTML += `
        <div class="typing" id="typing">
            🤖 Bot is typing...
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    document.getElementById("typing").remove();

    chatBox.innerHTML += `
        <div class="bot-message">
            <b>Healthcare Bot:</b><br><br>
            ${data.reply}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById("userInput")
.addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        sendMessage();
    }

});