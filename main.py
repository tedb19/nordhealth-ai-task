import json
import sys
from pathlib import Path

from app.discharge_note import generate_discharge_note
from app.models import Consultation
from app.providers.fireworks_provider import FireworksProvider
from app.utils import load_json, write_json

EXPECTED_ARG_COUNT = 2


def main() -> None:
    if len(sys.argv) != EXPECTED_ARG_COUNT:
        print("Usage: python main.py <path_to_input_json>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"File {input_path} does not exist.")
        sys.exit(1)

    try:
        consultation_data = load_json(input_path)
        consultation = Consultation.model_validate(consultation_data)
    except ValueError as e:
        print(f"Invalid consultation data: {e}", file=sys.stderr)
        sys.exit(1)

    provider = FireworksProvider()
    # Through dependency injection, we can use any provider
    # that implements the BaseModelProvider interface.
    # In this case, we are using the FireworksProvider.
    # This allows us to easily switch to a different provider
    # in the future without changing the rest of the code.
    # This is useful for testing and flexibility.
    note = generate_discharge_note(consultation, provider)

    output_data = {"discharge_note": note}
    print(json.dumps(output_data, indent=2))

    output_path = Path("solution") / f"output_{input_path.stem}.json"
    write_json(output_data, output_path)


if __name__ == "__main__":
    main()
