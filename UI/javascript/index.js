// DOM Elements
const messageForm = document.getElementsByClassName('message-form');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatBox = document.querySelector('#chat-box');
const welcomeText = document.getElementById('welcome-text');
const themeCheckbox = document.getElementById('darkmode-toggle');


// Initialization
let isScrolledToBottom = true;


// AI response showing conditions [ans cat, (ans/subject, body)]
const final_response = (response) => {
  let responseArray = Array.from(response)
  if (responseArray[0] != 'email') {
    return responseArray[1]
  } else {
    subject = responseArray[1]
    body = responseArray[2]
    localStorage.setItem('subject', subject);
    localStorage.setItem('body', body);
    window.location.href = 'email-composer.html'
    return "You had reviewed composed email"
  }
}


// Functions
// Check for user logIn, if user already Loged In then it removes Sign Up button
const checkLogIn = () => {
  eel.logIn()(function(check) {
    if (check) {
      document.querySelector('#signUp-btn').remove();
    }
  });
}

// setting up the light and dark theme
const changeTheme = () => {
  const newTheme = themeCheckbox.checked ? 'light' : 'dark';
  document.body.classList.toggle('light-theme', newTheme === 'light');
  localStorage.setItem('preferred-theme', newTheme);
}

// to change theme on page reload based on local storage
const changeThemeOnReload = () => {
  const preferredTheme = localStorage.getItem('preferred-theme');
  if (preferredTheme === 'light') {
    themeCheckbox.checked = true;
    document.body.classList.add('light-theme');
  } else if (preferredTheme === 'dark') {
    themeCheckbox.checked = false;
    document.body.classList.remove('light-theme');
  }
}

// activates send button on clicking enter
const handleEnterPress = (event) => {
  if (event.key === 'Enter') {
    welcomeText.remove();
    sendButton.click();
  }
}

const show_user_query = (query) => {
  chatBox.innerHTML += "<br><div class='container'><img id='user-icon' src='img/user_icon.png' alt=''><p class='text-container user'>" + query + "<br></p></div>";
  scrollIfNeeded();
}

// function to show AI response with autoscroll
const show_ai_ans = (ans) => {
  const div = document.createElement('div');
  div.className = 'container';
  const img = document.createElement('img');
  img.id = 'ai-icon';
  img.src = 'img/pinac_logo.png';
  const p = document.createElement('p');
  p.className = 'text-container ai';
  div.appendChild(img);
  div.appendChild(p);
  chatBox.appendChild(div);

  let index = 0;
  const timer = setInterval(function() {
    p.innerHTML += ans[index].replace(/\n/g, '<br>');
    chatBox.scrollTop = chatBox.scrollHeight;
    index++;
    if (index >= ans.length) {
      clearInterval(timer);
      scrollIfNeeded();
    }
  }, 10);
}

const give_response = () => {
  if (messageInput.value !== '') {
    //Disable while AI generates response
    messageInput.disabled = true;
    sendButton.disabled = true;
    // Show user query
    show_user_query(messageInput.value);
    // Show loading animation
    showLoadingAnimation();
    // Call AI response function
    eel.giveResponseArray(messageInput.value)(function(responseArray) {
      // Hide loading animation
      hideLoadingAnimation();
      // Show AI response
      response = final_response(responseArray)
      show_ai_ans(response);
      //Enable after AI generates response
      messageInput.disabled = false;
      sendButton.disabled = false;
    });
  }
  messageInput.value = '';
}

// Adds loading animation
const showLoadingAnimation = () => {
  const loadingAnimation = document.createElement("div");
  loadingAnimation.className = "loading-animation";
  loadingAnimation.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
  // Append loading animation to chat box
  chatBox.appendChild(loadingAnimation);
}

// Remove loading animation
const hideLoadingAnimation = () => {
  const loadingAnimation = document.querySelector(".loading-animation");
  if (loadingAnimation) {
    loadingAnimation.remove();
  }
}

const scrollIfNeeded = () => {
  isScrolledToBottom = chatBox.scrollHeight - chatBox.scrollTop === chatBox.clientHeight;
  if (isScrolledToBottom) {
    chatBox.scrollTop = chatBox.scrollHeight;
  }
}


// Menu Functions
const menu_open = () => {
  document.getElementById('mySidebar').style.display = 'block';
}

const menu_close = () => {
  document.getElementById('mySidebar').style.display = 'none';
}


// Redirection Functions
const clearChat = () => {
  eel.clearMemory();
  window.location.href = 'index.html';
}

const redirectToAbout = () => {
  window.location.href = 'about.html';
}

const redirectToProfile = () => {
  window.location.href = 'profile.html';
}


// Welcome Text Animation
const displayAnimatedWelcomeText = (delay = 200) => {
  // Define multi line welcome message
  const welcome_multi_msg = [
    'Hello, how can I help you today.',
    'Stay at the top of your schedule with me.',
    'Have any questions? Just ask me.'
  ];

  let lineIndex = 0; // Initialize index to track current line
  let charIndex = 0; // Initialize index to track current character within the line

  const intervalId = setInterval(function() {
    const line = welcome_multi_msg[lineIndex]; // Get the current line from the message
    const char = line[charIndex]; // Get the current character from the line
    const element = welcomeText;

    element.innerHTML += char; 
    charIndex++; // Move to the next character

    if (charIndex == line.length){
      charIndex = 0; // Reset character index
      lineIndex++; // Move to the next line
    
    // If reached end of message, reset the cycle
    if (lineIndex === welcome_multi_msg.length) {
      lineIndex = 0;
      element.innerHTML = ''; // Clear the welcome message
    }else{
      // Add a delay before clearing innerHTML
      setTimeout(function() {
        element.innerHTML = ''; // Clear the welcome message
      }, delay=50);
    }
  }
  }, delay); // Delay for displaying each character
}


// Event Listeners
window.addEventListener('load', checkLogIn);
window.addEventListener('load', changeThemeOnReload);
themeCheckbox.addEventListener('change', changeTheme);
messageInput.addEventListener('keydown', handleEnterPress);
