import ollama

MODEL = "llama3.1:8b"

def generate_response(prompt: str, temperature: float = 0.0) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": temperature
        }
    )
    return response["message"]["content"]