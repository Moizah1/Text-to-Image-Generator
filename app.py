import gradio
import requests 
import io

from PIL import Image, ImageEnhance   



#authorization token for Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
headers = {"Authorization": "your token here"}


#function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content



#function to generate image from prompt
def generate_image(prompt, brightness, contrast):
    image_bytes =query({"inputs": prompt})
    image = Image.open(io.BytesIO(image_bytes))


    #Apply brightness and contrast enhancement
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)  # Increase brightness by 20%
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)  # Increase contrast by 20    


    return image

#gradio interface
interface = gradio.Interface(
    fn=generate_image, 
    inputs=["text", gradio.Slider(0.5,2.0,1.0, label="Brightness"), gradio.Slider(0.5,2.0,1.0, label="Contrast")], 
    outputs="image", 
    title="Text to Image Generator", 
    description="Enter a prompt to generate an image using the SDXL Flash model."
    )
interface.launch(share=True)

