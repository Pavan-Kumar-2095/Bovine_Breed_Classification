from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = "AIzaSyDvr4wgL4lj7gSdoXvCnN6npoDUyIsOouo"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI()

# ✅ CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend host
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Breed classes
cow_breeds = ['Ayshire', 'Brown_swiss', 'Holstein_Friesian', 'Khillari', 'Red_Sindhi']
buffalo_breeds = ["Banni", "Jaffrabadi", "Nagpuri", "Nili_ravi", "Toda"]

# ✅ Load models
try:
    cow_vs_buffalo_model = tf.keras.models.load_model("Models/buffalo_vs_cow_model.keras")
    cow_breed_model = tf.keras.models.load_model("Models/Cow_breed.keras")
    buffalo_breed_model = tf.keras.models.load_model("Models/Buffalo_breed.keras")
except Exception as e:
    raise RuntimeError(f"Failed to load models: {e}")

# ✅ Image preprocessing
def preprocess_image(image_bytes: bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        img = img.resize((224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

# ✅ Breed summarization using Gemini
def get_breed_summary(breed_name: str) -> str:
    prompt = (
    f"Assume you are an experienced animal doctor. "
    f"Provide a brief, clear summary of the animal breed '{breed_name}' for Indian farmers. "
    f"Include the following details in short bullet points: average weight, height, typical diet, common vaccines, and essential care tips. "
    f"Keep it concise and easy to understand.")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

# ✅ Prediction and summarization
@app.post("/predict")
async def predict_image(image: UploadFile = File(...)):
    if not image:
        raise HTTPException(status_code=400, detail="No image uploaded")

    img_bytes = await image.read()
    img_array = preprocess_image(img_bytes)

    # Step 1: Predict animal
    animal_pred = cow_vs_buffalo_model.predict(img_array)[0][0]
    animal = "buffalo" if animal_pred < 0.5 else "cow"

    # Step 2: Predict breed
    if animal == "cow":
        breed_preds = cow_breed_model.predict(img_array)
        breed_index = np.argmax(breed_preds, axis=1)[0]
        breed = cow_breeds[breed_index]
        breed_conf = float(breed_preds[0][breed_index])
    else:
        breed_preds = buffalo_breed_model.predict(img_array)
        breed_index = np.argmax(breed_preds, axis=1)[0]
        breed = buffalo_breeds[breed_index]
        breed_conf = float(breed_preds[0][breed_index])

    # Step 3: Get Gemini summary
    summary = get_breed_summary(breed)

    print(summary)
    print(breed , animal)

    return {
        "animal": animal,
        "breed": breed,
        "confidence": breed_conf,
        "animal_confidence": float(animal_pred),
        "summary": summary
    }

# ✅ Allow running via `python fastapi_app.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Server:app", host="0.0.0.0", port=5000, reload=True)
