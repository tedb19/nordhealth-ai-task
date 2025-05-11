from abc import ABC, abstractmethod


class BaseModelProvider(ABC):
    @abstractmethod
    def generate_discharge_note(self, user_prompt: str) -> str:
        pass
