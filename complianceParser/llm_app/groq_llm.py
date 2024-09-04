from complianceParser.llm_app.base_llm import BaseLLM
from groq import Groq
import os

class GroqLLM(BaseLLM):

    def __init__(self):
        self.__api_key = os.environ.get("GROQ_API_KEY")

    def initialize_client(self, model = None) -> None:
        self.client = Groq(
    api_key=self.__api_key,)
        self.model = model
        

    def get_response(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        model=self.model,
        )
        return chat_completion.choices[0].message.content
