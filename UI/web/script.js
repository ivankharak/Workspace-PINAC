
const messageForm = document.getElementsByClassName('message-form');
const messageInput = document.getElementById('message-input');



function give_response() {

	if (messageInput.value != 0) {
		document.querySelector("#chat-box").innerHTML += "<b>You:</b> " + messageInput.value + "<br><br>"

		eel.give_response(messageInput.value)(function (response) {
			document.querySelector("#chat-box").innerHTML += response[0] + "<br><br>"
			document.querySelector("#chat-box").innerHTML += response[1] + "<br><br>"
			document.querySelector("#chat-box").innerHTML += "Creating draft email...<br>Draft email created: " + response[2] + "<br><br><br><br>"
		})
	}
	messageInput.value = "";
}
