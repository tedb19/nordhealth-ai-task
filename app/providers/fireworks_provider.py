import os

from dotenv import load_dotenv
from fireworks.client import Fireworks

from app.prompt import load_prompt
from app.providers.base import BaseModelProvider

load_dotenv()


class FireworksProvider(BaseModelProvider):
    def __init__(self) -> None:
        self.client = Fireworks(api_key=os.getenv("FIREWORKS_API_KEY"))
        self.model = "accounts/fireworks/models/llama-v3p1-405b-instruct"

    def generate_discharge_note(self, user_prompt: str) -> str:
        system_prompt = load_prompt("system_prompt")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.4,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
