document.getElementById("sendBtn").addEventListener("click", function() {
    let userInput = document.getElementById("userInput").value;
    appendMessage("You: " + userInput);

    fetch("https://your-backend-url.com/chat", { // Replace with your hosted backend
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("AI: " + data.reply);
    })
    .catch(error => {
        appendMessage("AI: Error reaching the server.");
        console.error("Error:", error);
    });

    document.getElementById("userInput").value = "";
});

function appendMessage(message) {
    let chatBox = document.getElementById("chatBox");
    let msgElement = document.createElement("p");
    msgElement.innerText = message;
    chatBox.appendChild(msgElement);
}
