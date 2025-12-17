# story_gemini.py
import os
import google.generativeai as genai

# Using Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = (
    "You are a creative story generator. "
    "Given an image caption and optional user instructions, "
    "write an engaging, coherent story suitable for children and young adults."
)

def generate_story_from_caption(caption: str, user_prompt: str, theme: str) -> str:
    """Generate a story from an image caption using Google Gemini."""
    full_prompt = (
        f"Image caption: {caption}\n\n"
        f"Theme: {theme}\n\n"
        f"User instructions: {user_prompt}\n\n"
        f"{SYSTEM_PROMPT}\n\n"
        "Write a detailed story (600-1000 words) that fits the theme, "
        "is imaginative, and easy to understand."
    )

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(full_prompt)
    
    return response.text
