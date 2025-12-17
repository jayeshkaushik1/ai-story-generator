# app.py
import streamlit as st
from captioning import generate_caption
from story_perplexity import generate_story_from_caption

st.set_page_config(page_title="AI Story Generator", page_icon="📖", layout="wide")

st.title("📖 Image-based AI Story Generator")

st.sidebar.header("Options")
theme = st.sidebar.selectbox(
    "Story theme",
    ["Fantasy", "Adventure", "Sci‑Fi", "Mystery", "Slice of life", "Horror (mild)"],
    index=0,
)
user_prompt = st.sidebar.text_area(
    "Extra instructions",
    "Make it light-hearted and suitable for kids.",
    height=100,
)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)

if st.button("Generate Story", type="primary", disabled=uploaded_file is None):
    if uploaded_file is None:
        st.warning("Please upload an image first.")
    else:
        with st.spinner("Generating image caption..."):
            image_bytes = uploaded_file.read()
            caption = generate_caption(image_bytes)
            st.info(f"Detected caption: **{caption}**")

        with st.spinner("Generating story with Perplexity Sonar..."):
            story = generate_story_from_caption(caption, user_prompt, theme)

        st.subheader("Generated Story")
        st.write(story)
