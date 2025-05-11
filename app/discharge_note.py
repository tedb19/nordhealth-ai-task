from app.models import Consultation
from app.prompt_builder import get_user_prompt
from app.providers.base import BaseModelProvider


def generate_discharge_note(
    consultation: Consultation,
    provider: BaseModelProvider,
) -> str:
    user_prompt = get_user_prompt(consultation)
    return provider.generate_discharge_note(user_prompt)
