import streamlit as st
import google.generativeai as genai
import random

# Configure Google Generative AI API key
# Ideally, this should be stored in st.secrets or environment variables
api_key = "AIzaSyDCG7_AE9N3ocS8pT3lQWyP2icEnHsGMCE"
genai.configure(api_key=api_key)

# Generation Configuration
generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Function to get a random programming joke
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the developer go broke? Because he used up all his cache.",
        "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
        "What is a programmer's favorite hangout place? Foo Bar.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "What do you call a programmer from Finland? Nerdic.",
        "Why did the computer go to the doctor? Because it had a virus!",
        "There are 10 types of people in the world: those who understand binary, and those who don't."
    ]
    return random.choice(jokes)

# Function to generate recipe blog
def recipe_generation(topic, word_count):
    try:
        model = genai.GenerativeModel(
            # model_name="gemini-flash-latest",
            model_name="gemini-2.5-flash",
            generation_config=generation_config,
        )
        
        prompt = f"""
        You are a professional food blogger. Create a detailed and engaging recipe blog post about "{topic}".
        The blog post should be approximately {word_count} words long.
        Include a catchy title, an introduction, ingredients list, step-by-step instructions, and a conclusion.
        Make it fun and appetizing.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error creating recipe: {str(e)}"

# Streamlit UI
def main():
    st.set_page_config(
        page_title="Flavor Fusion",
        page_icon="🍲",
        layout="wide",
        initial_sidebar_state="expanded"
    )


    st.markdown("""
<style>

/* Page background */
.stApp {
    background-color: #F0FFF4;
}

/* Title */
h1 {
    color: #27AE60;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    border-bottom: 3px solid #27AE60;
    padding-bottom: 10px;
}

/* Buttons */
.stButton > button {
    background-color: #27AE60;
    color: white;
    border-radius: 25px;
    padding: 12px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #1E8449;
    transform: scale(1.05);
}

/* Input box */
.stTextInput input {
    border-radius: 12px;
}

/* Recipe card */
.recipe-card {
    background-color: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    border-left: 8px solid #27AE60;
}

/* Joke box */
.joke-box {
    background-color: #FEF9E7;
    color: #856404;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #F9E79F;
    text-align: center;
    font-style: italic;
    margin-bottom: 20px;
}
                

</style>
""", unsafe_allow_html=True)

    
    st.title("🍲 Flavor Fusion")
    st.markdown("<h3 style='text-align: center; color: #555;'>AI-Driven Recipe Blogging</h3>", unsafe_allow_html=True)
    st.markdown("---")

    # Layout with columns
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.markdown("### 🍳 Configuration")
        st.info("Customize your recipe request below.")
        
        topic = st.text_input("📝 Recipe Topic", placeholder="e.g., Gluten Free Bread")
        word_count = st.slider("📏 Desired Word Count", min_value=100, max_value=2000, value=500, step=50)
        
        st.markdown("### 🤖 Model Settings")
        st.caption("Using Gemini Flash for fast generation.")
        
        generate_btn = st.button("✨ Generate Recipe")

    with col2:
        if generate_btn:
            if topic:
                # Joke display
                joke = get_joke()
                
                # Create a placeholder for the joke
                joke_placeholder = st.empty()
                joke_placeholder.markdown(f"""
                <div class="joke-box">
                    😄 <b>Programmer Joke:</b><br>{joke}
                </div>
                """, unsafe_allow_html=True)
                
                with st.spinner("👨‍🍳 Chef AI is cooking up your blog post..."):
                    recipe_content = recipe_generation(topic, word_count)
                
                # Clear joke
                joke_placeholder.empty()

                if recipe_content and "Error" not in recipe_content:
                    st.markdown(f"""
                    <div class="recipe-card">
                        {recipe_content}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.success("🎉 Recipe generated successfully!")
                    
                    st.download_button(
                        label="📥 Download Recipe",
                        data=recipe_content,
                        file_name=f"{topic.replace(' ', '_').lower()}_recipe.md",
                        mime="text/markdown",
                        help="Save this recipe to your computer"
                    )
                else:
                    st.error("😕 " + recipe_content)
            else:
                st.warning("⚠️ Please enter a recipe topic first.")
        else:
            st.markdown("""
            <div style='text-align: center; padding: 50px; color: #888;'>
                <h3>👈 Ready to cook?</h3>
                <p>Enter a topic in the sidebar and hit Generate!</p>
                <div style='font-size: 50px;'>🥗 🍕 🍰 🌮</div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
