import ollama

MODEL = "llama3.1:8b"

def generate_response_to_complaint(complaint: str) -> str:
    with open("prompts/respond.txt", "r") as f:
        system_prompt = f.read()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": complaint}
        ],
        options={
            "temperature": 0.7
        }
    )

    return response["message"]["content"].strip()