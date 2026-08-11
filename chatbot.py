# DecodeBot - Rule-Based AI Chatbot
# DecodeLabs Artificial Intelligence Internship - Project 1


def get_response(user_input):
    """
    Process user input and return a rule-based chatbot response.
    """

    # Normalize user input
    user_input = user_input.lower().strip().rstrip("?!., ")

    # ---------------- GREETINGS ----------------
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif user_input in ["good morning", "morning"]:
        return "Good morning! ☀️ Have a great day!"

    elif user_input in ["good afternoon", "afternoon"]:
        return "Good afternoon! 😊"

    elif user_input in ["good evening", "evening"]:
        return "Good evening! 🌆"


    # ---------------- BASIC CONVERSATION ----------------
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking. 😊"

    elif user_input in [
        "what is your name",
        "who are you",
        "tell me your name",
        "what should i call you"
    ]:
        return "I'm DecodeBot, your rule-based AI assistant. 🤖"

    elif user_input in ["nice to meet you", "nice meeting you"]:
        return "Nice to meet you too! 😊"

    elif user_input in ["thanks", "thank you", "thank you decodebot"]:
        return "You're welcome! 😊"


    # ---------------- CHATBOT CAPABILITIES ----------------
    elif user_input in [
        "what can you do",
        "what do you do",
        "your capabilities"
    ]:
        return (
            "I can respond to greetings, answer basic questions, "
            "explain basic AI concepts, and have simple conversations."
        )


    # ---------------- AI-RELATED QUESTIONS ----------------
    elif user_input in [
        "what is ai",
        "what is artificial intelligence",
        "define ai"
    ]:
        return (
            "Artificial Intelligence is the field of creating systems "
            "that can perform tasks that normally require human-like intelligence."
        )


    # ---------------- CREATOR INFORMATION ----------------
    elif user_input in ["who created you", "who made you"]:
        return (
            "I was created as a Rule-Based AI project for "
            "the DecodeLabs Artificial Intelligence internship."
        )


    # ---------------- HELP COMMAND ----------------
    elif user_input == "help":
        return (
            "Here are some things you can ask me:\n"
            "• Say hello, hi, or hey\n"
            "• Ask 'How are you?'\n"
            "• Ask 'What is your name?'\n"
            "• Ask 'What can you do?'\n"
            "• Ask 'What is AI?'\n"
            "• Ask 'Who created you?'\n"
            "• Say 'Thank you'\n"
            "• Type 'bye' or 'exit' to end the chat"
        )


    # ---------------- EXIT COMMANDS ----------------
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"


    # ---------------- UNKNOWN INPUT ----------------
    else:
        return (
            "Sorry, I don't understand that yet. "
            "Type 'help' to see what I can do."
        )


# Terminal version
if __name__ == "__main__":

    print("🤖 DecodeBot: Hello! I am DecodeBot.")
    print("🤖 DecodeBot: I am a simple rule-based AI chatbot.")
    print("🤖 DecodeBot: Type 'help' to see what I can do.")
    print("🤖 DecodeBot: Type 'bye' or 'exit' to end the conversation.")

    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("🤖 DecodeBot:", response)

        if user_input.lower().strip().rstrip("?!., ") in [
            "bye",
            "goodbye",
            "exit",
            "quit"
        ]:
            break