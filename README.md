# 🖼️ Text-to-Image Generator

> Generate stunning AI images from text prompts using the **SDXL Flash** model — powered by Hugging Face, wrapped in a clean Gradio web UI.


## ✨ Features

- 🚀 **Fast image generation** via SDXL Flash on Hugging Face Inference API
- 🎨 **Real-time brightness control** — slider from 0.5× (dark) to 2.0× (bright)
- 🎛️ **Real-time contrast control** — slider from 0.5× (flat) to 2.0× (vivid)
- 🌐 **Instant public link** — shareable URL generated automatically via Gradio
- 💻 **No local GPU required** — inference runs on Hugging Face servers

---

## 📸 Demo

| Prompt | Output |
|--------|--------|
| *"A futuristic city skyline at night with neon lights"* | AI-generated image |
| *"A cozy cabin in an autumn forest, warm window glow"* | AI-generated image |
| *"Abstract watercolor painting of galaxies merging"* | AI-generated image |

---

## 🗂️ Project Structure

```
text-to-image-generator/
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## ⚙️ Requirements

- Python 3.8+
- A [Hugging Face](https://huggingface.co) account and API token
- Internet connection

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-to-image-generator.git
cd text-to-image-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install gradio requests Pillow transformers huggingface_hub
```

### 3. Add your Hugging Face API token

Open `app.py` and replace the placeholder:

```python
headers = {"Authorization": "Bearer hf_YOUR_TOKEN_HERE"}
```

> ⚠️ **Security tip:** Never commit your token to version control. Use a `.env` file instead:
>
> ```bash
> pip install python-dotenv
> ```
>
> ```python
> import os
> from dotenv import load_dotenv
> load_dotenv()
> headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
> ```
>
> Then create a `.env` file:
> ```
> HF_TOKEN=hf_your_token_here
> ```
> And add `.env` to your `.gitignore`.

### 4. Run the app

```bash
python app.py
```

Gradio will print a **local URL** and a **public shareable URL** (valid for 72 hours).

---

## 🎮 Usage

| Control | Type | Default | Description |
|---------|------|---------|-------------|
| **Prompt** | Text | — | Describe the image you want to generate |
| **Brightness** | Slider 0.5 – 2.0 | 1.0 | 1.0 = original · lower = darker · higher = brighter |
| **Contrast** | Slider 0.5 – 2.0 | 1.0 | 1.0 = original · lower = flatter · higher = more vivid |

### Example prompts

```
A photorealistic portrait of a golden retriever wearing a wizard hat
A futuristic city skyline at night with neon lights reflecting on wet streets
Abstract watercolor painting of galaxies merging together, vibrant colors
A cozy cabin in an autumn forest, warm light glowing from the windows
```

---

## 🔧 How It Works

```
User Prompt + Sliders
        │
        ▼
  Gradio Interface
        │
        ▼
  POST → Hugging Face
  Inference API (SDXL Flash)
        │
        ▼
  Raw image bytes returned
        │
        ▼
  PIL decodes bytes → Image
        │
        ▼
  ImageEnhance.Brightness applied
  ImageEnhance.Contrast applied
        │
        ▼
  Final image displayed in UI
```
