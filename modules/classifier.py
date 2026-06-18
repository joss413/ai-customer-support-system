from config import generate_response

CATEGORY_MAP = {
    "Technical": "Technical Issue",
    "Billing": "Billing Inquiry",
    "Feedback": "Product Feedback"
}

def classify_complaint(complaint: str) -> str:
    with open("prompts/classify.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{complaint}", complaint)

    raw_output = generate_response(prompt).strip()

    for key in CATEGORY_MAP:
        if key.lower() in raw_output.lower():
            return CATEGORY_MAP[key]

    return "Unknown"