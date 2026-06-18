# from modules.classifier import classify_complaint

# complaint = "I was charged twice for my subscription this month"
# print(classify_complaint(complaint))


# from modules.classifier import classify_complaint

# tests = [
#     "My app keeps crashing every time I open it",
#     "I love the new update, the dark mode looks great!",
#     "I was charged twice for my subscription this month"
# ]

# for t in tests:
#     print(f"{t} -> {classify_complaint(t)}")



# from modules.entity_extractor import extract_entities

# complaint = "I was charged twice for my subscription this month"
# print(extract_entities(complaint))



# from modules.responder import generate_response_to_complaint

# complaint = "I was charged twice for my subscription this month"
# print(generate_response_to_complaint(complaint))


# from modules.translator import translate_response

# text = "I'm sorry to hear about this issue. We will resolve it as soon as possible."
# print(translate_response(text))


# from database import init_db, save_ticket, get_all_tickets

# init_db()
# save_ticket(
#     complaint="I was charged twice",
#     category="Billing Inquiry",
#     product="subscription",
#     issue_summary="charged twice, unexpected billing error",
#     urgency="High",
#     response="I'm sorry to hear about this issue..."
# )

# print(get_all_tickets())

# from config import generate_response

# prompt_classify = open("prompts/classify.txt").read().replace("{complaint}", "My app keeps crashing every time I try to open the camera feature, and I have an important video call in an hour.")
# print("CLASSIFY RAW OUTPUT:")
# print(generate_response(prompt_classify))
# print("---")

# prompt_extract = open("prompts/extract.txt").read().replace("{complaint}", "My app keeps crashing every time I try to open the camera feature, and I have an important video call in an hour.")
# print("EXTRACT RAW OUTPUT:")
# print(generate_response(prompt_extract))

from config import generate_response

complaint = "Just wanted to say the new dashboard redesign looks really clean, great job on the update."

prompt_extract = open("prompts/extract.txt").read().replace("{complaint}", complaint)
print("EXTRACT RAW OUTPUT:")
print(generate_response(prompt_extract))