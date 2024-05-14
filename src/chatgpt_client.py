from openai import AsyncOpenAI

class ChatGptClient:
    def __init__(self):
        self._chat_history = []  # Initialize a chat history
        self.client = AsyncOpenAI()

    async def chat_client(self, user_input):
        # Add user input to the chat history
        self.set_chat_history({"role": "user", "content": user_input})

        # Request a completion from the model using the getter for chat history
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.get_chat_history(),
            temperature=1,
            max_tokens=700,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the content from the response
        message_content = response.choices[0].message.content
        # Identify the first sentence by finding the first ending punctuation
        first_sentence = self.extract_first_sentence(message_content)

        # Add the model's response to the chat history
        self.set_chat_history({"role": "assistant", "content": first_sentence})
        return first_sentence

    def extract_first_sentence(self, text):
        # extract content to make shorty
        end_points = [text.find(char) for char in '.?!']
        end_points = [point for point in end_points if point != -1]

        if end_points:
            first_end_point = min(end_points) + 1
            return text[:first_end_point].strip()
        return text

    def get_chat_history(self):
        return self._chat_history

    def set_chat_history(self, message):
        if not isinstance(message, dict):
            raise ValueError("Message must be a dictionary")
        self._chat_history.append(message)
