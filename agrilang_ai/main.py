from flask import Flask, request, jsonify
from agri_chatbot import AgriLangChatbot

app = Flask(__name__)

# Initialize the chatbot with your OpenAI API key
chatbot = AgriLangChatbot(api_key="your_openai_api_key")

@app.route('/get-advice', methods=['POST'])
def get_advice():
    user_query = request.json.get("query", "")
    advice = chatbot.get_advice(user_query)
    return jsonify({"advice": advice})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
