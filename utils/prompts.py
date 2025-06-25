from pathlib import Path

PROMPT_PATH = Path(__file__).parent / "src" / "instructions.md"

def get_instructions() -> str:
    """
    Get the instructions for the assistant.
    """
    try:
        with open(PROMPT_PATH, "r", encoding="utf-8") as file:
            instructions = file.read()
        return instructions
    except Exception as error:
        return f"Error reading instructions: {error}" 