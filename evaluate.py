from modules.classifier import classify_complaint
from modules.entity_extractor import extract_entities

# Test cases: (complaint, expected_category)
test_cases = [
    ("My app keeps crashing every time I try to open the camera feature", "Technical Issue"),
    ("I was charged twice for my subscription this month", "Billing Inquiry"),
    ("Just wanted to say the new dashboard redesign looks really clean", "Product Feedback"),
    ("The mobile app won't let me log in anymore, it just keeps spinning", "Technical Issue"),
    ("My free trial ended but I never got an email about it", "Billing Inquiry"),
    ("I really appreciate how fast your support team replied yesterday", "Product Feedback"),
    ("The export to PDF feature produces a blank file every time", "Technical Issue"),
    ("Why was I charged a late fee when I paid on time?", "Billing Inquiry"),
]

correct = 0
total = len(test_cases)

print("=" * 60)
print("EVALUATION REPORT — Classifier Accuracy")
print("=" * 60)

for complaint, expected in test_cases:
    predicted = classify_complaint(complaint)
    is_correct = predicted == expected
    correct += int(is_correct)

    status = "✅" if is_correct else "❌"
    print(f"{status} Complaint: {complaint[:50]}...")
    print(f"   Expected: {expected} | Predicted: {predicted}")
    print("-" * 60)

accuracy = (correct / total) * 100
print(f"\nFinal Accuracy: {correct}/{total} ({accuracy:.1f}%)")
print("=" * 60)

# check entity extraction doesn't crash or return Unknown/null on any case
print("\nEVALUATION REPORT — Entity Extraction Stability")
print("=" * 60)

failures = 0
for complaint, _ in test_cases:
    entities = extract_entities(complaint)
    has_unknown = any(v in ("Unknown", None, "") for v in entities.values())
    status = "⚠️ Incomplete" if has_unknown else "✅ Complete"
    if has_unknown:
        failures += 1
    print(f"{status}: {entities}")

print(f"\nExtraction completeness: {total - failures}/{total} fully populated")
print("=" * 60)