const recipientEmail = document.getElementById('to');
const subjectInput = document.getElementById('subject');
const bodyInput = document.getElementById('body');
const sendButton = document.getElementById('send-button');
const goBackButton = document.getElementById('goBack-button');
const saveDraftButton = document.getElementById('save-draft-button');

const subject = localStorage.getItem('subject');
const body = localStorage.getItem('body');


// This autofill the input boxes with values with page reload
const autoFill = () => {
    subjectInput.value = subject
    bodyInput.value = body
}

const goBack = () => {
    window.location.href = 'index.html';
}

const sendEmail = () => {
    if (recipientEmail.value) {
        eel.validateEmail(recipientEmail.value)(function(valid) {
            if (valid) {
                eel.sendInstEmail(recipientEmail.value, subjectInput.value, bodyInput.value)(function () {})
                window.location.href = 'index.html';
            } else {
                // Added temporarily, will be replaced in future
                alert("Invalid Email Id")
            }
        })
    } else {
        // Added temporarily, will be replaced in future
        alert("Unable to send email without recipient email")
    }
}

const createDraft = () => {
    if (recipientEmail.value) {
        eel.validateEmail(recipientEmail.value)(function(valid) {
            if (valid) {
                eel.createDraftEmail(subjectInput.value, bodyInput.value, recipientEmail.value)(function() {})
                window.location.href = 'index.html';
            } else {
                // Added temporarily, will be replaced in future
                alert("Invalid Email Id")
            }
        })
    } else {
        eel.createDraftEmail(subjectInput.value, bodyInput.value)(function() {})
        window.location.href = 'index.html';
    }
}


// Event Listeners
window.addEventListener('load', autoFill());