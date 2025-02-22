import random

responses = {
    "hello": [
        "Hi there! 👋 How can I assist with your Full-Stack Developer portfolio?",
        "Here are some options you might find helpful:\n"
        "1️⃣ Build a Portfolio Website 🌐\n"
        "2️⃣ Optimize Resume & LinkedIn 📄\n"
        "3️⃣ Prepare for Interviews 🎯\n"
        "4️⃣ Learn New Technologies 🚀\n"
        "Just type the number of the option you'd like to explore!"
    ],
    "1": ["To build a great portfolio website, consider using React, Next.js, or plain HTML/CSS/JS. Do you need help with templates?"],
    "2": ["For resume & LinkedIn optimization, focus on projects, skills, and clear descriptions. Need some templates or guidance?"],
    "3": ["For interview prep, focus on coding challenges (LeetCode), system design, and behavioral questions. Want some tips?"],
    "4": ["Learning new tech? Explore AI, cloud computing, or backend frameworks like Django and Node.js. Need recommendations?"],
    "default": ["I'm not sure about that. Can you try rephrasing? 🤔"]
}

def chatbot_response(message):
    message = message.lower()
    for key in responses.keys():
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])
