# 🤖 DecodeBot — Rule-Based AI Chatbot

A beginner-friendly rule-based AI chatbot developed as **Project 1 of the DecodeLabs Artificial Intelligence Internship**.

## 📌 Project Overview

DecodeBot is a simple conversational chatbot that uses predefined rules and conditional logic to respond to user inputs.

The project demonstrates the fundamentals of **rule-based Artificial Intelligence**, where responses are determined using explicitly programmed `if`, `elif`, and `else` conditions rather than machine learning.

This project serves as a foundation for understanding control flow, decision-making, and basic AI concepts.

## 🎯 Objective

The objective of this project is to create a chatbot that:

* Handles greetings and exit commands
* Responds to predefined user inputs
* Uses `if-elif-else` decision-making logic
* Runs continuously until the user chooses to exit
* Demonstrates basic rule-based AI concepts

## ✨ Features

* 👋 Multiple greeting responses
* 🌅 Morning, afternoon, and evening greetings
* 💬 Basic conversational responses
* 🤖 Information about the chatbot
* 🧠 Basic explanation of Artificial Intelligence
* 🛠️ Chatbot capability information
* 👨‍💻 Information about the project's purpose
* ❓ Interactive help command
* 🚪 Multiple exit commands
* 🔤 Case-insensitive user input
* ✨ Basic punctuation handling
* 🛡️ Fallback response for unknown inputs
* 🔄 Continuous conversation loop

## 🧠 How It Works

DecodeBot follows a simple rule-based decision-making process:

```text
User Input
     ↓
Input Normalization
     ↓
Check Predefined Rules
     ↓
┌─────────────────────────────┐
│ Greeting?                   │
│ Basic question?             │
│ AI-related question?        │
│ Help command?               │
│ Exit command?               │
└─────────────────────────────┘
     ↓
Generate Predefined Response
     ↓
Continue Conversation
     ↓
Exit when requested
```

The chatbot does not learn from conversations. Instead, it compares the user's input against predefined rules and produces the corresponding response.

## 🛠️ Technologies Used

* **Python 3**
* Python Standard Library
* Conditional Statements
* `while` Loop
* String Processing
* Console Input/Output

No external Python packages are required.

## 📂 Project Structure

```text
DecodeLabs_AI_Project1/
│
├── chatbot.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
```

### File Description

| File / Folder      | Description                         |
| ------------------ | ----------------------------------- |
| `chatbot.py`       | Main chatbot application            |
| `README.md`        | Project documentation               |
| `requirements.txt` | Project dependency information      |
| `.gitignore`       | Files excluded from version control |
| `screenshots/`     | Demonstration screenshots           |


## 💬 Example Conversation

```text
🤖 DecodeBot: Hello! I am DecodeBot.
🤖 DecodeBot: I am a simple rule-based AI chatbot.
🤖 DecodeBot: Type 'help' to see what I can do.
🤖 DecodeBot: Type 'bye' or 'exit' to end the conversation.

You: hello
🤖 DecodeBot: Hello! How can I help you?

You: What is your name?
🤖 DecodeBot: I'm DecodeBot, your rule-based AI assistant. 🤖

You: What is AI?
🤖 DecodeBot: Artificial Intelligence is the field of creating
             systems that can perform tasks that normally require
             human-like intelligence.

You: help
🤖 DecodeBot: Here are some things you can ask me:

You: bye
🤖 DecodeBot: Goodbye! 👋 Have a great day!
```


## 🎓 Internship Context

This project was developed as **Project 1 — Rule-Based AI Chatbot** as part of the **DecodeLabs Artificial Intelligence Internship**.

The project focuses on foundational concepts including:

* Control flow
* Decision-making logic
* Predefined responses
* Continuous program execution
* Basic Artificial Intelligence concepts

## 👩‍💻 Author

**Lakshmi Varsha Thumati**

Artificial Intelligence Intern
DecodeLabs Internship - 2026
