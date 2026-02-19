# Flavour-Fusion-AI-Driven-Recipe-Blogging
🍲 Flavour Fusion: AI-Driven Recipe Blogging

Flavour Fusion is an interactive AI-powered web application that generates engaging recipe blog posts using Google Gemini AI. Whether you're a food blogger, home cook, or student developer, this app helps you instantly create structured, creative, and ready-to-publish recipe content.

Built with Python + Streamlit + Gemini 1.5 Flash, the application combines Generative AI with a clean user interface to simplify recipe blogging.

🌐 Project Demo

🎥 Demo Video:
https://drive.google.com/file/d/1Hz9EQJXTTLktwJt50uUEF7UBd7bYIDuV/view?usp=sharing

💻 GitHub Repository:
https://github.com/PattapuChohitha/Flavour-Fusion-AI-Driven-Recipe-Blogging

✨ Features
🤖 AI-Powered Recipe Generation

Generates complete recipe blog posts including:

Catchy Title

Ingredients List

Step-by-Step Instructions

Engaging Introduction

Powered by Gemini 1.5 Flash

🎯 Customizable Output

Enter any dish name or ingredient
(e.g., “Paneer Butter Masala”, “Chocolate Lava Cake”)

Adjust blog length from 100 to 2000 words

😄 Fun Element

Displays a random programming joke while the AI generates your recipe

📥 Download Option

Save generated recipes as Markdown (.md) files

🎨 Modern UI

Clean, responsive interface built using Streamlit

Custom styling for better user experience

🛠️ Tech Stack

Frontend: Streamlit

AI Model: Google Gemini (Gemini 1.5 Flash)

Programming Language: Python

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/PattapuChohitha/Flavour-Fusion-AI-Driven-Recipe-Blogging.git
cd Flavour-Fusion-AI-Driven-Recipe-Blogging

2️⃣ Install Dependencies

Make sure Python is installed, then run:

pip install -r requirements.txt

🔑 API Configuration

This application requires a Google Gemini API key.

Recommended Secure Setup:

Get your API key from Google AI Studio

Create a file:

.streamlit/secrets.toml


Add your key:

GOOGLE_API_KEY = "your_api_key_here"


Update code to use:

st.secrets["GOOGLE_API_KEY"]

💡 Usage
▶️ Run the Application
streamlit run app.py

🧑‍🍳 Generate a Recipe

Enter a recipe topic

Select desired word count

Click Generate Recipe

Wait for AI magic ✨

Download if you like it

📂 Project Structure
Flavour-Fusion/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
├── README.md           # Documentation

👩‍💻 Developed By

Pattapu Chohitha

⭐ Acknowledgment

This project demonstrates the use of Generative AI for creative content generation and was built as part of an academic innovation project.
