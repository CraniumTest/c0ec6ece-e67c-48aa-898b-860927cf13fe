import openai

class AgriLangChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def get_advice(self, user_query):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"You are an expert agriculture advisor. {user_query}",
                temperature=0.5,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {str(e)}"
