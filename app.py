import os
import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

reader = PdfReader("data/sample_resume.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text

with open("data/sample_summary.txt", "r") as f:
    summary = f.read()

system_prompt = f"""
You are an AI professional profile assistant.

Resume:
{resume_text}

Summary:
{summary}

Answer questions based on the provided information.
If information is unavailable, say so.
"""

def chat(message, history):
    prompt = f"""
{system_prompt}

User: {message}
"""

    response = model.generate_content(prompt)

    return response.text

gr.ChatInterface(chat).launch()