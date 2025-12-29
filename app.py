import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit page config
st.set_page_config(
    page_title="🔒 Sensitive Data Detection & Masking",
    layout="centered"
)

st.title("🔒 Sensitive Data Detection & Masking")
st.caption("Detect and mask sensitive information like Name, Email, Phone, Address, ID numbers, etc.")

# Text input
user_text = st.text_area(
    "Enter Text to Analyze",
    height=300,
    placeholder="Paste text containing sensitive information here..."
)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a privacy filter. Detect and MASK all sensitive information in the given text. "
            "Replace sensitive entities with [MASKED_TYPE]. "
            "Examples: [MASKED_NAME], [MASKED_EMAIL], [MASKED_PHONE], [MASKED_ADDRESS], "
            "[MASKED_ID], [MASKED_CREDIT_CARD], [MASKED_PASSWORD]. "
            "Return only the masked text."
        ),
        (
            "user",
            "Please process the following text:\n\n{question}"
        )
    ]
)

# LLM setup
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key
)

output_parser = StrOutputParser()
chain = prompt | model | output_parser

# Button
mask_button = st.button("🔍 Detect & Mask Sensitive Data")

# Processing
if mask_button:
    if not user_text.strip():
        st.warning("Please enter text to analyze.")
    else:
        with st.spinner("Masking sensitive information..."):
            response = chain.invoke({"question": user_text})

            st.success("✅ Sensitive Data Masked Successfully")
            st.subheader("🔐 Masked Output")
            st.markdown(response)
