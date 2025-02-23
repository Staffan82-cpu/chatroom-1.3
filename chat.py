def chatbot_response(message):
    message = message.lower()
    
    if message == "hello":
        return {
            "response": "Hi there! 👋 How can I assist with your Full-Stack Developer portfolio?",
            "options": ["Build a Portfolio Website", "Optimize Resume & LinkedIn", "Prepare for Interviews", "Learn New Technologies"]
        }
    elif message == "build a portfolio website":
        return {
            "response": "To build a great portfolio website, consider using React, Next.js, or HTML/CSS/JS.",
            "options": ["Get Portfolio Templates", "Best Hosting Platforms", "Portfolio Design Tips"]
        }
    elif message == "optimize resume & linkedin":
        return {
            "response": "For resume & LinkedIn optimization, focus on projects, skills, and clear descriptions.",
            "options": ["See Resume Templates", "Improve LinkedIn Profile", "Best Resume Tips"]
        }
    elif message == "prepare for interviews":
        return {
            "response": "For interview prep, focus on coding challenges (LeetCode), system design, and behavioral questions.",
            "options": ["Practice Coding Challenges", "System Design Tips", "Common Interview Questions"]
        }
    elif message == "learn new technologies":
        return {
            "response": "Learning new tech? Explore AI, cloud computing, or backend frameworks like Django and Node.js.",
            "options": ["Learn AI & ML", "Explore Cloud Computing", "Backend Frameworks"]
        }
    else:
        return {"response": "I'm not sure about that. Can you try rephrasing? 🤔"}

