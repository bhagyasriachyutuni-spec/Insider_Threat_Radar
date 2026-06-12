// future enhancements// EMAIL VALIDATION
function validateEmail(email) {
    if (!email.endsWith("@savantis.com")) {
        alert("Invalid email! Only @savantis.com allowed");
        return false;
    }
    return true;
}

// KEYSTROKE CAPTURE
let keystrokes = [];
let lastTime = null;

function captureKey(event) {
    let currentTime = new Date().getTime();

    if (lastTime !== null) {
        keystrokes.push(currentTime - lastTime);
    }

    lastTime = currentTime;
}

// SEND KEYSTROKE DATA TO BACKEND
function sendKeystrokes() {
    fetch('/save_keystroke', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pattern: keystrokes })
    });
}