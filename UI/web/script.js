
const messageForm = document.getElementsByClassName('message-form');
const messageInput = document.getElementById('message-input');


function show_user_query(query) {

	document.querySelector("#chat-box").innerHTML += '<li class="container user"><img class="user-ai-icon" src="img/user_icon_2.png" alt="">' + query + '<br></li>'
}

function show_ai_ans(ans) {

	document.querySelector("#chat-box").innerHTML += '<li class="container ai"><img class="user-ai-icon" src="img/pinac_logo.png" alt="">' + ans + '<br></li>'
}


function give_response() {

	if (messageInput.value != 0) {
		show_user_query(messageInput.value)

		eel.give_response(messageInput.value)(function (response) {
			show_ai_ans(response)
		})
	}
	messageInput.value = "";
}
