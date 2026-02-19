# 🍲 Flavour Fusion — AI-Driven Recipe Blogging

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-4285F4)

**Flavour Fusion** is an AI-powered recipe blogging application that generates complete, structured, and engaging recipe posts using **Google Gemini 1.5 Flash**.

Designed for food bloggers, home cooks, and content creators, the app instantly produces ready-to-publish recipes with introductions, ingredients, and step-by-step instructions.

---

## 🎥 Project Demo

🔗 **Demo Video:**
[https://drive.google.com/file/d/1Hz9EQJXTTLktwJt50uUEF7UBd7bYIDuV/view?usp=sharing](https://drive.google.com/file/d/1Hz9EQJXTTLktwJt50uUEF7UBd7bYIDuV/view?usp=sharing)

💻 **GitHub Repository:**
[https://github.com/PattapuChohitha/Flavour-Fusion-AI-Driven-Recipe-Blogging](https://github.com/PattapuChohitha/Flavour-Fusion-AI-Driven-Recipe-Blogging)

---

## ✨ Key Features

### 🤖 AI Recipe Generation

* Generates complete blog-style recipes
* Includes:

  * Catchy Title
  * Ingredients List
  * Cooking Instructions
  * Engaging Introduction

### 🎯 Customizable Output

* Enter any dish or ingredient
* Adjustable blog length (100–2000 words)

### 😄 Fun Experience

* Displays random programming jokes while generating content

### 📥 Download Support

* Export recipes as Markdown (.md) files

### 🎨 Modern User Interface

* Clean and responsive Streamlit UI
* Custom styling for better user experience

---

## 🛠️ Tech Stack

| Component | Technology              |
| --------- | ----------------------- |
| Frontend  | Streamlit               |
| AI Model  | Google Gemini 1.5 Flash |
| Language  | Python                  |

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/PattapuChohitha/Flavour-Fusion-AI-Driven-Recipe-Blogging.git
cd Flavour-Fusion-AI-Driven-Recipe-Blogging
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a file:

```bash
.streamlit/secrets.toml
```

Add your API key:

```toml
GOOGLE_API_KEY = "your_api_key_here"
```

Update code to use:

```python
st.secrets["GOOGLE_API_KEY"]
```

---

## 💡 Usage

### ▶️ Run Application

```bash
streamlit run app.py
```

### 🧑‍🍳 Generate Recipe

1. Enter recipe topic
2. Select word count
3. Click **Generate Recipe**
4. Wait for AI magic ✨
5. Download your recipe

---

## 📂 Project Structure

```
Flavour-Fusion/
│
├── app.py
├── requirements.txt
├── README.md
```

---

## 👩‍💻 Developed By

**Pattapu. Chohitha**


## 🌟 Future Enhancements

* Multi-language recipe generation
* Image generation for dishes
* Nutrition analysis
* Voice input support
* Blog publishing integration

---

## ⭐ Acknowledgment

This project demonstrates the power of Generative AI in content creation and was developed as part of an academic innovation initiative.

