# AI-Powered Customer Support System

An AI pipeline that classifies customer complaints, extracts structured ticket data, generates empathetic responses, and logs everything to a searchable dashboard.

## What It Does

1. **Classifies** complaints into `Technical Issue`, `Billing Inquiry`, or `Product Feedback`
2. **Extracts** structured data: product, issue summary, urgency, and sentiment
3. **Generates** an empathetic support response
4. **Logs** every ticket to a SQLite database
5. **Displays** everything in a filterable Streamlit dashboard

## Screenshots

**Submission Form**
![Submission Form](image/image1.png)
![Submission Form](image/image2.png)
![Submission Form](image/image3.png)
**Dashboard**
![Dashboard](image/image6.png)

**Evaluation Output**
![Evaluation](image/image4.png)
![Evaluation](image/image5.png)

## Tech Stack

- **Python**
- **Ollama (Llama 3.1 8B)** — local LLM inference
- **Streamlit** — UI and dashboard
- **SQLite** — ticket storage

## Architecture

```
customer-support-ai/
│
├── app.py                   # Streamlit UI
├── config.py                 # LLM client and generation settings
├── database.py                # SQLite schema and queries
├── evaluate.py                # Accuracy evaluation script
│
├── modules/
│   ├── classifier.py
│   ├── entity_extractor.py
│   └── responder.py
│
└── prompts/
    ├── classify.txt
    ├── extract.txt
    └── respond.txt
```

## Evaluation

`evaluate.py` runs 8 test complaints through the full pipeline and checks classification accuracy and extraction completeness.

```
Classifier Accuracy: 8/8 (100.0%)
Extraction Completeness: 8/8 fully populated
```

## Running Locally

```bash
ollama pull llama3.1:8b
pip install -r requirements.txt
python evaluate.py
streamlit run app.py
```
