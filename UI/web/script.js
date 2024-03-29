const messageForm = document.getElementsByClassName("message-form");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatBox = document.querySelector("#chat-box");
const themeController = document.querySelector("#icon");

// setting up the light and dark theme
themeController.addEventListener("click", () => {
  document.body.classList.toggle("light-theme");
  document.body.className === "light-theme"
    ? (themeController.src = "./img/moon.png")
    : (themeController.src = "./img/sun.png");
});

let isScrolledToBottom = true;

messageInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    sendButton.click();
  }
});

function show_user_query(query) {
  document.querySelector("#chat-box").innerHTML +=
    '<br><div class="container"><img id="user-icon" src="img/user_icon_2.png" alt=""><p class="text-container user">' +
    query +
    "<br></p></div>";
  scrollIfNeeded();
}

// function show_ai_ans(ans) {

// 	document.querySelector("#chat-box").innerHTML += '<div class="container"><img id="ai-icon" src="img/pinac_logo.png" alt=""><p class="text-container ai">' + ans + '<br><br><br></p></div>'
// 	scrollToBottom(); // Scroll to bottom after showing AI response
// }
function show_ai_ans(ans) {
  const container = document.querySelector("#chat-box");
  const div = document.createElement("div");
  div.className = "container";
  const img = document.createElement("img");
  img.id = "ai-icon";
  img.src = "img/pinac_logo.png";
  img.alt = "";
  const p = document.createElement("p");
  p.className = "text-container ai";
  div.appendChild(img);
  div.appendChild(p);
  container.appendChild(div);

  let index = 0;
  const timer = setInterval(function () {
    p.innerHTML += ans[index].replace(/\n/g, "<br>");
    container.scrollTop = container.scrollHeight;
    index++;
    if (index >= ans.length) {
      clearInterval(timer);
      scrollIfNeeded();
    }
  }, 10);
}

function give_response() {
  if (messageInput.value !== '') {

    //Disable while AI generates response
    messageInput.disabled = true;
    sendButton.disabled = true;
    
    // Show user query
    show_user_query(messageInput.value);

    // Show loading animation
    showLoadingAnimation();

    // Call AI response function
    eel.give_response(messageInput.value)(function (response) {
      // Hide loading animation
      hideLoadingAnimation();
      // Show AI response
      show_ai_ans(response);

      //Enbale after AI generates response
      messageInput.disabled = false;
      sendButton.disabled = false;

    });
  }
  messageInput.value = "";
}

function showLoadingAnimation() {
  // Create loading animation elements
  const loadingAnimation = document.createElement("div");
  loadingAnimation.className = "loading-animation";
  loadingAnimation.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';

  // Append loading animation to chat box
  chatBox.appendChild(loadingAnimation);
}

function hideLoadingAnimation() {
  // Remove loading animation
  const loadingAnimation = document.querySelector(".loading-animation");
  if (loadingAnimation) {
    loadingAnimation.remove();
  }
}

function scrollIfNeeded() {
  isScrolledToBottom =
    chatBox.scrollHeight - chatBox.scrollTop === chatBox.clientHeight;

  if (isScrolledToBottom) {
    chatBox.scrollTop = chatBox.scrollHeight;
  }
}
