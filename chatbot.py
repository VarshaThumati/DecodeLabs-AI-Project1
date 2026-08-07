# DecodeBot - Rule-Based AI Chatbot
# DecodeLabs Artificial Intelligence Internship - Project 1


# Welcome message
print("🤖 DecodeBot: Hello! I am DecodeBot.")
print("🤖 DecodeBot: I am a simple rule-based AI chatbot.")
print("🤖 DecodeBot: Type 'help' to see what I can do.")
print("🤖 DecodeBot: Type 'bye' or 'exit' to end the conversation.")


# Continuous conversation loop
while True:
    user_input = input("You: ").lower().strip().rstrip("?!.,")
    
    # ---------------- GREETINGS ----------------
    if user_input in ["hello", "hi", "hey"]:
        print("🤖 DecodeBot: Hello! How can I help you?")

    elif user_input in ["good morning", "morning"]:
        print("🤖 DecodeBot: Good morning! ☀️ Have a great day!")

    elif user_input in ["good afternoon", "afternoon"]:
        print("🤖 DecodeBot: Good afternoon! 😊")

    elif user_input in ["good evening", "evening"]:
        print("🤖 DecodeBot: Good evening! 🌆")


    # ---------------- BASIC CONVERSATION ----------------
    elif user_input in ["how are you", "how are you doing"]:
        print("🤖 DecodeBot: I'm doing great! Thanks for asking. 😊")

    elif user_input in [
        "what is your name",
        "who are you",
        "tell me your name",
        "what should i call you"
    ]:
        print("🤖 DecodeBot: I'm DecodeBot, your rule-based AI assistant. 🤖")

    elif user_input in ["nice to meet you", "nice meeting you"]:
        print("🤖 DecodeBot: Nice to meet you too! 😊")

    elif user_input in ["thanks", "thank you", "thank you decodebot"]:
        print("🤖 DecodeBot: You're welcome! 😊")


    # ---------------- CHATBOT CAPABILITIES ----------------
    elif user_input in ["what can you do", "what do you do", "your capabilities"]:
        print("🤖 DecodeBot: I can respond to greetings, answer basic questions,")
        print("             explain basic AI concepts, and have simple conversations.")


    # ---------------- AI-RELATED QUESTIONS ----------------
    elif user_input in [
        "what is ai",
        "what is artificial intelligence",
        "define ai"
    ]:
        print("🤖 DecodeBot: Artificial Intelligence is the field of creating")
        print("             systems that can perform tasks that normally require")
        print("             human-like intelligence.")


    # ---------------- CREATOR INFORMATION ----------------
    elif user_input in ["who created you", "who made you"]:
        print("🤖 DecodeBot: I was created as a Rule-Based AI project for")
        print("             the DecodeLabs Artificial Intelligence internship.")


    # ---------------- HELP COMMAND ----------------
    elif user_input == "help":
        print("\n🤖 DecodeBot: Here are some things you can ask me:")
        print("   • Say hello, hi, or hey")
        print("   • Ask 'How are you?'")
        print("   • Ask 'What is your name?'")
        print("   • Ask 'What can you do?'")
        print("   • Ask 'What is AI?'")
        print("   • Ask 'Who created you?'")
        print("   • Say 'Thank you'")
        print("   • Type 'bye' or 'exit' to end the chat\n")


    # ---------------- EXIT COMMANDS ----------------
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("🤖 DecodeBot: Goodbye! 👋 Have a great day!")
        break


    # ---------------- UNKNOWN INPUT ----------------
    else:
        print("🤖 DecodeBot: Sorry, I don't understand that yet.")
        print("             Type 'help' to see what I can do.")