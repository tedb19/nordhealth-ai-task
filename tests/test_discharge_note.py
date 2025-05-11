import os

import pytest

from app.discharge_note import generate_discharge_note
from app.models import Consultation, ConsultationDetails, Patient
from app.providers.base import BaseModelProvider
from app.providers.fireworks_provider import FireworksProvider


class MockProvider(BaseModelProvider):
    def generate_discharge_note(self, user_prompt: str) -> str:
        assert (
            "Patient Name: Fluffy" in user_prompt
        )  # simple check that prompt includes correct detail
        return "Mocked discharge note for Fluffy"


@pytest.fixture()
def mock_consultation() -> Consultation:
    return Consultation(
        patient=Patient(
            name="Fluffy",
            species="Canine",
            breed="Labrador",
            gender="Female",
            neutered=True,
            date_of_birth="2018-06-01",
            weight="25kg",
        ),
        consultation=ConsultationDetails(
            date="2024-05-01",
            time="14:30",
            reason="Routine check-up",
            type="Wellness",
            clinical_notes=[],
            treatment_items={},
        ),
    )


def test_generate_discharge_note_with_mock_provider(
    mock_consultation: Consultation,
) -> None:
    provider = MockProvider()
    note = generate_discharge_note(mock_consultation, provider)
    assert note == "Mocked discharge note for Fluffy"


@pytest.mark.skipif(
    not os.getenv("RUN_INTEGRATION_TESTS"),
    reason="Integration tests disabled by default",
)
def test_generate_discharge_note_fireworks_provider() -> None:
    provider = FireworksProvider()

    consultation = Consultation(
        patient=Patient(
            name="Rex",
            species="Canine",
            breed="German Shepherd",
            gender="Male",
            neutered=False,
            date_of_birth="2017-02-15",
            weight="30kg",
        ),
        consultation=ConsultationDetails(
            date="2025-05-11",
            time="10:00",
            reason="Injury",
            type="Emergency",
            clinical_notes=[],
            treatment_items={},
        ),
    )

    note = generate_discharge_note(consultation, provider)
    assert "Discharge Note" in note
    assert isinstance(note, str)
    assert len(note) > 0
    assert "Thank you for using Provet Cloud" in note
