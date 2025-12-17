# 📖 AI Story Generator

An image-to-story generator powered by **Streamlit**, **BLIP** (local image captioning), and **Perplexity Sonar** (AI story generation). Upload an image, and watch it become a creative story!

## ✨ Features

- **Local Image Captioning**: Uses Salesforce BLIP model to generate captions from images (no external API calls for image understanding)
- **Perplexity AI Story Generation**: Leverages Perplexity's Sonar model to create engaging, thematic stories
- **Customizable Themes**: Choose from Fantasy, Adventure, Sci-Fi, Mystery, Slice of life, or Horror (mild)
- **User Instructions**: Add extra context for fine-tuned story generation
- **Streamlit UI**: Simple, intuitive web interface
- **Cost-Efficient**: Image captioning is free (local), and Perplexity keeps API costs low with the Pro monthly credit

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- A Perplexity Pro API key (get one at [https://www.perplexity.ai/](https://www.perplexity.ai/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jayeshkaushik1/ai-story-generator.git
cd ai-story-generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
cp .env.example .env
# Edit .env and add your Perplexity API key
```

5. Run the app:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
ai-story-generator/
├── app.py                 # Streamlit frontend
├── captioning.py          # Local BLIP image captioning
├── story_perplexity.py    # Perplexity API integration
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🛠 How It Works

### 1. Image Captioning (Local)
- User uploads an image via Streamlit UI
- **BLIP model** (Salesforce/blip-image-captioning-base) generates a caption locally
- No external API call needed for this step

### 2. Story Generation (Perplexity API)
- Combined caption + user instructions + theme are sent to **Perplexity Sonar**
- Sonar generates a 600-1000 word story fitting the selected theme
- Result is displayed in the Streamlit UI

## 🔧 Configuration

### Environment Variables

Create a `.env` file (or copy from `.env.example`) with:
```
PERPLEXITY_API_KEY=sk-your_api_key_here
```

### API Costs

- **Image Captioning**: FREE (runs locally using BLIP)
- **Story Generation**: Uses Perplexity Pro monthly credit (~$5/month included with Pro)

## 📚 Dependencies

- **streamlit**: Web UI framework
- **torch**: PyTorch for BLIP model
- **transformers**: Hugging Face transformers library (BLIP models)
- **pillow**: Image processing
- **openai**: OpenAI client (compatible with Perplexity's API)
- **python-dotenv**: Environment variable management

## 🎯 Usage Tips

1. **Best Results**: Use clear, well-lit images
2. **Custom Themes**: Select a theme that matches your mood
3. **Extra Instructions**: Add details like "Make it funny" or "Include magic elements"
4. **Story Length**: Currently set to 600-1000 words; adjust in `story_perplexity.py` if needed

## ⚙️ Advanced Customization

### Change Image Captioning Model

Edit `captioning.py` to use a different BLIP variant:
```python
# Other options:
# "Salesforce/blip-image-captioning-large"
# "Salesforce/blip-vqa-base"
processor = BlipProcessor.from_pretrained("Your-Model-Name")
```

### Adjust Perplexity Story Parameters

Edit `story_perplexity.py`:
```python
resp = client.chat.completions.create(
    model="sonar-pro",  # or "sonar" for faster/cheaper
    messages=messages,
    max_tokens=1200,    # Adjust story length
    temperature=0.9,    # 0.0 = deterministic, 1.0 = creative
)
```

## 📝 Example Flow

1. User uploads `sunset_beach.jpg`
2. BLIP generates: "A beautiful sunset over a calm beach with palm trees"
3. User selects theme: "Fantasy" and adds: "Include a mystical creature"
4. Perplexity Sonar generates a 800-word fantasy story about the beach
5. Story is displayed in Streamlit with styling

## 🐛 Troubleshooting

### CUDA Out of Memory
If you get CUDA errors:
- Run on CPU: Comment out `device = "cuda"` in `captioning.py` and set `device = "cpu"`
- Or reduce model size: Use `Salesforce/blip-image-captioning-base` instead of `large`

### Perplexity API Errors
- Verify your API key in `.env`
- Check Perplexity API status at [https://www.perplexity.ai/](https://www.perplexity.ai/)
- Ensure you have Pro credits remaining

### Slow Image Processing
- First run downloads the BLIP model (~1-2 GB)
- Subsequent runs are cached and faster
- Using GPU (`torch.cuda.is_available()`) significantly speeds up inference

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open-source. Use it freely!

## 🙏 Acknowledgments

- **Salesforce Research** for BLIP model
- **Perplexity AI** for Sonar API
- **Streamlit** for the web framework
- **Hugging Face** for transformers library

---

**Made with ❤️ by Jayesh Kaushik**

Questions? Issues? Open a GitHub issue!
