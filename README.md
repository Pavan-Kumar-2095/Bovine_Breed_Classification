# 🌾🐄🐃 AI-Powered Cow & Buffalo Breed Detection System

A full-stack AI system that detects whether an image contains a cow or buffalo, predicts the exact breed, and generates AI-powered veterinary insights using Deep Learning + Generative AI.

Built using:
- 🧠 TensorFlow (MobileNetV2 + EfficientNetB0)
- 🤖 Google Gemini API (Generative AI)
- ⚡ FastAPI (Python Backend)
- 🎨 React.js (Frontend)

---
## 🎥 Demo Video

https://github.com/user-attachments/assets/7173789d-831e-47a7-b3dd-0492705ea2ae

# 🚀 What This Project Does

1️⃣ Upload an image of livestock  
2️⃣ Detect whether it is a Cow or Buffalo  
3️⃣ Predict the exact breed  
4️⃣ Show confidence scores  
5️⃣ Generate AI veterinary summary (diet, vaccines, care tips)

---



# 🧬 Model Training

## Training Notebooks
```
Model Training/
├── Buffalo_Breed.ipynb
├── Cow_Breed.ipynb
├── Buffalo_VS_Cow.ipynb
├── mobileNetv2.ipynb
```
---

## AI Models Used

🐄 Cow vs Buffalo Model  
- MobileNetV2 (Transfer Learning)  
- Binary classification  

🐄 Cow Breed Model  
- EfficientNetB0 (Fine-tuned)  
- Ayrshire, Brown Swiss, Holstein Friesian, Khillari, Red Sindhi  

🐃 Buffalo Breed Model  
- EfficientNetB0 (Fine-tuned)  
- Banni, Jaffrabadi, Nagpuri, Nili Ravi, Toda  

---

## ⚙️ Training Strategy

- Transfer Learning with ImageNet pretrained weights  
- Frozen base layers initially  
- Fine-tuning top CNN layers for better accuracy  
- Data augmentation for robustness  
- Separate models for cow and buffalo breeds  
- Optimized learning rate tuning  

---

## 📦 Saved Models
```
Models/
├── buffalo_vs_cow_model.h5
├── buffalo_vs_cow_model.keras
├── Cow_breed.h5
├── Cow_breed.keras
├── Buffalo_breed.h5
├── Buffalo_breed.keras
```
---

# ⚙️ Backend (FastAPI - Server.py)

Features:
- /predict endpoint for image inference
- TensorFlow model loading
- Image preprocessing using PIL + NumPy
- Two-stage prediction pipeline
- Gemini API integration

Output:
- Animal type
- Breed name
- Confidence scores
- AI-generated veterinary summary

---

# 🎨 Frontend (React.js)
```
src/
├── Components/
│   ├── Breed_Predictor.js
│   ├── Breed_Predictor.css
├── App.js
├── App.css
├── index.js
```

Features:
- Image upload + preview
- AI prediction display
- Confidence scores
- Gemini-generated veterinary insights
- Clean UI

UI Flow:
Upload Image → Click Predict → View Results → AI Summary

---

# 🌐 Public Folder
```
public/
├── index.html
├── favicon.ico
├── logo192.png
├── logo512.png
├── manifest.json
├── robots.txt
```
---

# 🤖 Generative AI (Gemini)

After prediction, Gemini generates:
- Breed characteristics
- Weight & height
- Diet recommendations
- Vaccination details
- Veterinary care tips

Optimized for Indian agriculture use cases.

---


# 🌍 Real-World Impact

- Smart farming systems  
- Livestock identification  
- Precision agriculture  
- AI veterinary assistance  

---

# 📁 Full Project Structure
```
project-root/
├── Model Training/
├── Models/
├── public/
├── src/
├── Server.py
├── package.json
├── package-lock.json
├── .gitignore
```
---
# ⚙️ How to Setup & Use

This project has two parts:
- ⚡ Backend (FastAPI + AI Models)
- 🎨 Frontend (React)

---

#  1. Clone the Repository

```bash
git clone https://github.com/Pavan-Kumar-2095/Bovine_Breed_Classification/
cd your-repo-name
```
#   2. Backend Setup (FastAPI)
Install dependencies
```bash
pip install fastapi uvicorn tensorflow numpy pillow requests python-dotenv google-generativeai
```


#  3.Add environment variables

Create a .env file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```
# Run backend server
```bash
python Server.py
```

or <br> 
```bash
uvicorn Server:app --reload --host 0.0.0.0 --port 5000
```
Backend will run at:
```
http://localhost:5000
```

#  4. Frontend Setup (React)
Install dependencies
```bash
npm install
```

## Start frontend
```bash
npm start
```
Frontend will run at:
```
http://localhost:3000
```
