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

name = <Add_your_name_here>

system_prompt = f"""You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and Resume which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer, say so.

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