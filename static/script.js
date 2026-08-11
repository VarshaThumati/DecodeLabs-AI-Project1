const chatForm = document.getElementById("chatForm");

const messageInput = document.getElementById("messageInput");

const chatMessages = document.getElementById("chatMessages");

const sendButton = document.getElementById("sendButton");

const typingIndicator =
    document.getElementById("typingIndicator");

const clearChatButton =
    document.getElementById("clearChatButton");


/* ================= TIME ================= */

function getCurrentTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

}


/* ================= ESCAPE HTML ================= */

function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}


/* ================= ADD MESSAGE ================= */

function addMessage(message, sender) {

    const messageDiv =
        document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender === "bot"
            ? "bot-message"
            : "user-message"
    );


    const safeMessage =
        escapeHTML(message);


    if (sender === "bot") {

       messageDiv.innerHTML = `
    <div class="message-avatar">🤖</div>
    <div class="message-content">
        <div class="message-name">DecodeBot</div>
        <div class="message-bubble">${safeMessage}</div>
        <div class="message-time">${getCurrentTime()}</div>
    </div>
`;

    }

    else {
    messageDiv.innerHTML = `
        <div class="message-content">
            <div class="message-name">You</div>
            <div class="message-bubble">${safeMessage}</div>
            <div class="message-time">${getCurrentTime()}</div>
        </div>
        <div class="message-avatar">👤</div>
    `;
}

    chatMessages.appendChild(messageDiv);


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


/* ================= TYPING ================= */

function showTyping() {

    typingIndicator.classList.remove(
        "hidden"
    );

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


function hideTyping() {

    typingIndicator.classList.add(
        "hidden"
    );

}


/* ================= SEND MESSAGE ================= */

chatForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const message =
            messageInput.value.trim();


        if (!message) {

            return;

        }


        addMessage(
            message,
            "user"
        );


        messageInput.value = "";


        sendButton.disabled = true;


        showTyping();


        try {

            const response =
                await fetch(
                    "/chat",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            message: message
                        })

                    }
                );


            if (!response.ok) {

                throw new Error(
                    "Server error"
                );

            }


            const data =
                await response.json();


            /*
             * Small delay so the typing
             * indicator feels natural.
             */

            await new Promise(
                resolve =>
                    setTimeout(
                        resolve,
                        400
                    )
            );


            hideTyping();


            addMessage(
                data.response,
                "bot"
            );


            /*
             * If the user says goodbye,
             * show the response but keep
             * the application available.
             */

            if (
                [
                    "bye",
                    "goodbye",
                    "exit",
                    "quit"
                ].includes(
                    message
                        .toLowerCase()
                        .trim()
                        .replace(/[?!.,]+$/, "")
                )
            ) {

                messageInput.disabled =
                    true;

                sendButton.disabled =
                    true;

            }


        }

        catch (error) {

            console.error(
                "Chat error:",
                error
            );


            hideTyping();


            addMessage(
                "Sorry, I'm having trouble connecting right now. Please try again.",
                "bot"
            );

        }

        finally {

            if (!messageInput.disabled) {

                sendButton.disabled =
                    false;

                messageInput.focus();

            }

        }

    }
);


/* ================= CLEAR CHAT ================= */

clearChatButton.addEventListener(
    "click",
    function() {

        chatMessages.innerHTML = `

            <div class="message bot-message">

                <div class="message-avatar">
                    🤖
                </div>

                <div class="message-content">

                    <div class="message-name">
                        DecodeBot
                    </div>

                    <div class="message-bubble">

                        Hello again! 👋

                        <br><br>

                        How can I help you?

                    </div>

                    <div class="message-time">
                        ${getCurrentTime()}
                    </div>

                </div>

            </div>

        `;


        messageInput.disabled =
            false;

        sendButton.disabled =
            false;

        messageInput.focus();

    }
);


/* ================= INITIAL FOCUS ================= */

messageInput.focus();