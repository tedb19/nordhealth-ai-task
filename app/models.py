from pydantic import BaseModel


class ClinicalNote(BaseModel):
    note: str


class TreatmentItem(BaseModel):
    name: str
    time: str | None = ""


class Patient(BaseModel):
    name: str
    species: str | None = "Unknown"
    breed: str | None = "Unknown"
    gender: str | None = "Unknown"
    neutered: bool | None = False
    date_of_birth: str | None = "Unknown"
    weight: str | None = "Unknown"


class ConsultationDetails(BaseModel):
    date: str
    time: str
    reason: str
    type: str
    clinical_notes: list[ClinicalNote] = []
    treatment_items: dict[str, list[TreatmentItem]] = {}


class Consultation(BaseModel):
    patient: Patient
    consultation: ConsultationDetails
