# Nordhealth AI Task

- This project automates the generation of discharge notes from veterinary
  consultation data using an LLM, specifically leveraging the **Fireworks API** for
  model inference.

### How It Works

- Uses Fireworks AI API to interact with the
  `accounts/fireworks/models/llama-v3p1-405b-instruct` model
- Extracts relevant patient and consultation details from input JSON files
- Crafts a detailed prompt to the model to generate discharge notes
- Outputs the discharge note in a structured JSON format

### Why Fireworks AI

- **Performance:** The llama-v3p1-405b-instruct model has been optimized for structured
  prompt-based tasks, making it suitable for generating detailed, high-quality
  discharge notes.

- **Cost Efficiency:** By using Fireworks API, we can scale the task with a lower
  cost compared to other LLMs, while still ensuring quality and accuracy.

- **Flexibility:** The API allows for easy integration with our workflow, making
  it possible to switch models or services with minimal effort.

### Prerequisites

Before running the project, ensure you have:

- **Python 3.11** (Tested on version 3.11, but versions 3.8+ should work)

- An **API key from Fireworks AI** (look at .env.example)

### 🚀 How to Run

1. Clone the repository and navigate to the project folder

```bash
git clone https://github.com/tedb19/nordhealth-ai-task.git
cd nordhealth-ai-task
```

2. Create and activate a virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Set up your API key - Create a .env file in the root directory:

```bash
FIREWORKS_API_KEY=your_api_key_here
```

5. Run the script

```bash
python main.py data/consultation1.json
```

### 🌠 What to expect:

The script will:

1. Print the generated discharge note to the terminal

2. Save the output as solution/output_consultation1.json


### 🧪 Running Tests
This project uses **pytest** for testing.

To run tests:

```bash
pytest
```

Test coverage includes:
- Prompt construction
- Discharge note formatting
- Edge cases (e.g. missing treatments, notes)

#### Sample test run:

```bash
nordhealth-ai-task on  main !+                          (.venv)  dev-admin 4s
󰄛 ❯ pytest -v
============================= test session starts ==============================
platform darwin -- Python 3.11.11, pytest-8.3.5, pluggy-1.5.0 -- /Users/teddybrian/Area51/NordHealth/nordhealth-ai-task/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/teddybrian/Area51/NordHealth/nordhealth-ai-task
configfile: pyproject.toml
plugins: approvaltests-0.2.4, anyio-4.9.0, approvaltests-14.5.0
collected 8 items

tests/test_discharge_note.py::test_generate_discharge_note_with_mock_provider PASSED [ 12%]
tests/test_discharge_note.py::test_generate_discharge_note_fireworks_provider PASSED [ 25%]
tests/test_prompt_builder.py::test_format_notes_with_notes PASSED        [ 37%]
tests/test_prompt_builder.py::test_format_notes_empty PASSED             [ 50%]
tests/test_prompt_builder.py::test_format_treatments_with_data PASSED    [ 62%]
tests/test_prompt_builder.py::test_format_treatments_empty PASSED        [ 75%]
tests/test_prompt_builder.py::test_get_user_prompt_includes_basic_info PASSED [ 87%]
tests/test_prompt_builder.py::test_get_user_prompt_with_minimal_data PASSED [100%]
```

### 🗂 Project Structure

```bash
.
├── README.md
├── app
│   ├── __init__.py
│   ├── discharge_note.py
│   ├── models.py
│   ├── prompt
│   │   ├── __init__.py
│   │   └── system_prompt.txt
│   ├── prompt_builder.py
│   ├── providers
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── fireworks_provider.py
│   └── utils.py
├── data
│   ├── consultation1.json
│   └── consultation2.json
├── main.py
├── pyproject.toml
├── requirements.txt
├── solution
│   ├── output_consultation1.json
│   └── output_consultation2.json
└── tests
    ├── __init__.py
    ├── test_discharge_note.py
    └── test_prompt_builder.py
```

### 🧼 Pre-commit Setup
- We use pre-commit to enforce code quality via formatters and linters.
- Install the pre-commit hooks:

```bash
pre-commit install
```

- Run all hooks manually (optional):

```bash
pre-commit run --all-files
```

#### Hooks include checks for:

- Code formatting (via black)
- Linting (via ruff)
- Type checking (via mypy)

### ✅ Completed Examples

data/consultation1.json → solution/output_consultation1.json
data/consultation2.json → solution/output_consultation2.json

### 🛡 Notes

- API keys are not committed — stored in .env
- The script is resilient to missing data (e.g., no notes/treatments)
- Designed to be easily extended or swapped for another LLM

### 🙌 Thanks

Looking forward to discussing this solution further. Built with ❤️ by Teddy Brian.
