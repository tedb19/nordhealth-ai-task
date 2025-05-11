from app.models import (
    ClinicalNote,
    Consultation,
    ConsultationDetails,
    Patient,
    TreatmentItem,
)
from app.prompt_builder import format_notes, format_treatments, get_user_prompt


def sample_consultation() -> Consultation:
    return Consultation(
        patient=Patient(
            name="Luna",
            species="Dog",
            breed="Golden Retriever",
            gender="Female",
            neutered=True,
            date_of_birth="2020-06-01",
            weight="25kg",
        ),
        consultation=ConsultationDetails(
            date="2025-05-10",
            time="10:30",
            reason="Annual vaccination",
            type="Vaccination",
            clinical_notes=[
                ClinicalNote(note="Patient was calm and cooperative."),
                ClinicalNote(note="No abnormalities detected."),
            ],
            treatment_items={
                "medications": [TreatmentItem(name="Rabies Vaccine", time="10:35")],
                "procedures": [],
            },
        ),
    )


def test_format_notes_with_notes() -> None:
    notes = [ClinicalNote(note="Note 1"), ClinicalNote(note="Note 2")]
    result = format_notes(notes)
    assert "- Note 1" in result
    assert "- Note 2" in result


def test_format_notes_empty() -> None:
    assert format_notes([]) == "No clinical notes."


def test_format_treatments_with_data() -> None:
    treatments = {
        "medications": [TreatmentItem(name="Antibiotic", time="14:00")],
        "procedures": [TreatmentItem(name="Wound cleaning", time="14:05")],
    }
    result = format_treatments(treatments)
    assert "Medications:" in result
    assert "- Antibiotic at 14:00" in result
    assert "Procedures:" in result
    assert "- Wound cleaning at 14:05" in result


def test_format_treatments_empty() -> None:
    assert format_treatments({}) == "No treatments administered."


def test_get_user_prompt_includes_basic_info() -> None:
    consultation = sample_consultation()
    prompt = get_user_prompt(consultation)

    assert "Patient Name: Luna" in prompt
    assert "Species: Dog" in prompt
    assert "Neutered: Yes" in prompt
    assert "Consultation Date: 2025-05-10 at 10:30" in prompt
    assert "Reason: Annual vaccination" in prompt
    assert "Type: Vaccination" in prompt

    # Clinical notes
    assert "- Patient was calm and cooperative." in prompt
    assert "- No abnormalities detected." in prompt

    # Treatments
    assert "Medications:" in prompt
    assert "- Rabies Vaccine at 10:35" in prompt


def test_get_user_prompt_with_minimal_data() -> None:
    consultation = Consultation(
        patient=Patient(name="Max"),
        consultation=ConsultationDetails(
            date="2025-01-01",
            time="08:00",
            reason="Checkup",
            type="General",
            clinical_notes=[],
            treatment_items={},
        ),
    )
    prompt = get_user_prompt(consultation)

    assert "Patient Name: Max" in prompt
    assert "No clinical notes." in prompt
    assert "No treatments administered." in prompt
