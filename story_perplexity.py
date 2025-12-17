# story_perplexity.py
import os
from openai import OpenAI

# Using Perplexity's OpenAI-compatible API
PPLX_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PPLX_BASE_URL = "https://api.perplexity.ai"

client = OpenAI(
    api_key=PPLX_API_KEY,
    base_url=PPLX_BASE_URL,
)

SYSTEM_PROMPT = (
    "You are a creative story generator. "
    "Given an image caption and optional user instructions, "
    "write an engaging, coherent story suitable for children and young adults."
)

def generate_story_from_caption(caption: str, user_prompt: str, theme: str) -> str:
    """Generate a story from an image caption using Perplexity Sonar."""
    full_prompt = (
        f"Image caption: {caption}\n\n"
        f"Theme: {theme}\n\n"
        f"User instructions: {user_prompt}\n\n"
        "Write a detailed story (600-1000 words) that fits the theme, "
        "is imaginative, and easy to understand."
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": full_prompt},
    ]

    resp = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
        max_tokens=1200,
        temperature=0.9,
    )

    return resp.choices[0].message.content
