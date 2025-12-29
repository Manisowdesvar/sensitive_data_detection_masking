# sensitive_data_detection_masking
AI-powered sensitive data detection and masking tool using LLMs to identify and redact PII such as names, emails, phone numbers, addresses, and credentials from unstructured text. Built with LangChain, Groq and Streamlit.

# Sensitive Data Detection & Masking (GenAI)

An AI-powered application that detects and masks sensitive information such as names, emails, phone numbers, addresses, IDs, and credentials from text using Large Language Models (LLMs).

---

## 🚀 Overview
This project leverages **Generative AI** to automatically identify and redact sensitive data from unstructured text. It helps improve data privacy, security, and compliance by replacing detected entities with standardized masked tokens.

Built using **LangChain, Groq LLaMA-3, and Streamlit**, the application provides real-time sensitive data masking through a simple and intuitive UI.

---

## ✨ Features
- Detects multiple types of sensitive data
- Masks PII and confidential information
- Supports unstructured text inputs
- Real-time processing using LLMs
- Interactive Streamlit interface

---

## 🔐 Masked Entity Types
- `[MASKED_NAME]`
- `[MASKED_EMAIL]`
- `[MASKED_PHONE]`
- `[MASKED_ADDRESS]`
- `[MASKED_ID]`
- `[MASKED_CREDIT_CARD]`
- `[MASKED_PASSWORD]`

---

## 🏗️ Tech Stack
- Python
- Generative AI
- LangChain
- Groq (LLaMA-3.3 70B)
- Streamlit
- Prompt Engineering

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/sensitive-data-detection-masking.git
cd sensitive-data-detection-masking
pip install -r requirements.txt
streamlit run app.py
