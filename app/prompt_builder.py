from app.models import ClinicalNote, Consultation, TreatmentItem


def get_user_prompt(consultation: Consultation) -> str:
    pet = consultation.patient
    consult = consultation.consultation

    user_prompt = f"""
    Please generate a discharge note for the following consultation record.
    Patient Name: {pet.name}
    Species: {pet.species}
    Breed: {pet.breed}
    Gender: {pet.gender}
    Neutered: {"Yes" if pet.neutered else "No"}
    Date of Birth: {pet.date_of_birth}
    Weight: {pet.weight}

    Consultation Date: {consult.date} at {consult.time}
    Reason: {consult.reason}
    Type: {consult.type}

    Clinical Notes:
    {format_notes(consult.clinical_notes)}

    Treatments:
    {format_treatments(consult.treatment_items)}
    """
    return user_prompt.strip()


def format_notes(notes: list[ClinicalNote]) -> str:
    if not notes:
        return "No clinical notes."
    return "\n".join(f"- {n.note}" for n in notes)


def format_treatments(treatments: dict[str, list[TreatmentItem]]) -> str:
    summary = []
    for category, items in treatments.items():
        if items:
            summary.append(f"{category.capitalize()}:")
            for item in items:
                summary.append(f"- {item.name or 'Unkown'} at {item.time}")
    return "\n".join(summary) or "No treatments administered."
