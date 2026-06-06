# AIPersona

AIPersona is an AI-powered professional profile assistant built using Python, Gemini, and Gradio.

The application allows users to chat with an AI that answers questions based on resume content and professional summaries.

## Features

* Resume-based question answering
* PDF resume ingestion
* Gemini-powered responses
* Interactive Gradio interface
* Personalized professional profile assistant

## Tech Stack

* Python
* Gemini API
* Gradio
* PyPDF
* Python Dotenv

## Setup Instructions

1. Clone the Repository
git clone <repository-url>
cd AIPersona
2. Create and Activate a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Gemini API Key
Create a .env file in the project root and add your Gemini API key:
GEMINI_API_KEY=your_api_key_here
You can obtain a Gemini API key from Google AI Studio.
5. Add Your Resume and Summary
Place your resume PDF in the data folder.
Example:
data/
├── sample_resume.pdf
└── sample_summary.txt
Update the file names in app.py if you use different names.
Add a short professional summary in sample_summary.txt. The AI will use both the resume and summary as context when answering questions.
6. Run the Application
python app.py
A Gradio interface will open in your browser where you can chat with your AI-powered professional profile assistant.

## Future Improvements

* Retrieval Augmented Generation (RAG)
* Interview preparation assistant
* ATS resume review
* Job description matching
* Career recommendation engine
