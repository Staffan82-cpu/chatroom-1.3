from app import app
from flask import render_template, request, jsonify
from app.chat import chatbot_response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})
