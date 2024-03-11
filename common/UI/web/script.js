
const messageForm = document.getElementsByClassName('message-form');
const messageInput = document.getElementById('message-input');



function give_response() {

	if (messageInput.value != 0) {
		document.querySelector("#chat-box").innerHTML += "<b>You:</b> " + messageInput.value + "<br><br>"

		eel.ask(messageInput.value)(function (response) {
			document.querySelector("#chat-box").innerHTML += "<b>PINAC:</b> " + response + "<br><br><br><br>"
		})
	}
	messageInput.value = "";
}
