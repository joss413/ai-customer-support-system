import json
import re
from config import generate_response

def extract_entities(complaint: str) -> dict:
    with open("prompts/extract.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{complaint}", complaint)

    raw_output = generate_response(prompt).strip()

    match = re.search(r"\{.*?\}", raw_output, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    return {
        "product": "Unknown",
        "issue_summary": raw_output,
        "urgency": "Unknown"
    }