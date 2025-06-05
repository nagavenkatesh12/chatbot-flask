from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def get_chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you?"])
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in message:
        return "I'm your friendly chatbot."
    elif "bye" in message or "exit" in message:
        return "Goodbye! Have a nice day!"
    return "I'm not sure how to respond to that. Can you ask something else?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot_response = get_chatbot_response(user_input)
    return jsonify({"response": bot_response})
