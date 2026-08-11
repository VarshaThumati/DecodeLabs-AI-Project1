from flask import Flask, request, jsonify, render_template
from chatbot import get_response
import threading
import webbrowser


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    bot_response = get_response(user_message)

    return jsonify({
        "response": bot_response
    })


def open_browser():
    webbrowser.open(
        "http://127.0.0.1:5000"
    )


if __name__ == "__main__":

    threading.Timer(
        1.5,
        open_browser
    ).start()

    app.run(debug=True)