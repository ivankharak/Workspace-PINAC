
const messageForm = document.getElementsByClassName('message-form');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button')


messageInput.addEventListener('keydown', function(event) {
	if (event.key === 'Enter') {
		sendButton.click()
	}
})

function show_user_query(query) {

	document.querySelector("#chat-box").innerHTML += '<div class="container"><img id="user-icon" src="img/user_icon_2.png" alt=""><p class="text-container user">' + query + '<br></p></div>'
}

function show_ai_ans(ans) {

	document.querySelector("#chat-box").innerHTML += '<div class="container"><img id="ai-icon" src="img/pinac_logo.png" alt=""><p class="text-container ai">' + ans + '<br><br><br></p></div>'
}


function give_response() {

	if (messageInput.value != 0) {
		show_user_query(messageInput.value)

		eel.give_response(messageInput.value)(function (response) {
			show_ai_ans(response);
		})
	}
	messageInput.value = "";
}
