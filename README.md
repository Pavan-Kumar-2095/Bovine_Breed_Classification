# AI-Powered Cow & Buffalo Breed Detection System

A full-stack AI application that detects whether an uploaded image contains a **cow** or **buffalo**, predicts its breed, and generates AI-powered veterinary insights using Deep Learning and Generative AI.

## Technologies Used

- TensorFlow (MobileNetV2 & EfficientNetB0)
- Google Gemini API
- FastAPI
- React.js

---

## Demo Video

https://github.com/user-attachments/assets/7173789d-831e-47a7-b3dd-0492705ea2ae

---

# Project Overview

The application performs the following steps:

1. Upload an image of livestock.
2. Detect whether the animal is a cow or buffalo.
3. Predict the corresponding breed.
4. Display confidence scores.
5. Generate AI-powered veterinary insights, including diet, vaccination, and care recommendations.

---

# Model Training

## Training Notebooks

```text
Model Training/
├── Buffalo_Breed.ipynb
├── Cow_Breed.ipynb
├── Buffalo_VS_Cow.ipynb
└── mobileNetv2.ipynb
```

## AI Models

### Cow vs Buffalo Classification

- MobileNetV2 (Transfer Learning)
- Binary Classification

### Cow Breed Classification

- EfficientNetB0 (Fine-Tuned)

Supported breeds:

- Ayrshire
- Brown Swiss
- Holstein Friesian
- Khillari
- Red Sindhi

### Buffalo Breed Classification

- EfficientNetB0 (Fine-Tuned)

Supported breeds:

- Banni
- Jaffrabadi
- Nagpuri
- Nili Ravi
- Toda

---

# Training Strategy

- Transfer Learning using ImageNet pretrained weights
- Initial training with frozen base layers
- Fine-tuning higher CNN layers
- Data augmentation for improved robustness
- Separate models for animal detection and breed classification
- Learning rate optimization

---

# Saved Models

```text
Models/
├── buffalo_vs_cow_model.h5
├── buffalo_vs_cow_model.keras
├── Cow_breed.h5
├── Cow_breed.keras
├── Buffalo_breed.h5
└── Buffalo_breed.keras
```

---

# Backend (FastAPI)

The backend is implemented in **Server.py**.

## Features

- REST API for image prediction
- TensorFlow model loading
- Image preprocessing using PIL and NumPy
- Two-stage prediction pipeline
- Google Gemini API integration

## API Output

- Animal Type
- Predicted Breed
- Confidence Scores
- AI-Generated Veterinary Summary

---

# Frontend (React.js)

## Project Structure

```text
src/
├── Components/
│   ├── Breed_Predictor.js
│   └── Breed_Predictor.css
├── App.js
├── App.css
└── index.js
```

## Features

- Image upload with preview
- Breed prediction
- Confidence score visualization
- AI-generated veterinary insights
- Clean and responsive user interface

## User Workflow

```
Upload Image
      ↓
Click Predict
      ↓
View Prediction
      ↓
Read AI Veterinary Summary
```

---

# Public Folder

```text
public/
├── favicon.ico
├── index.html
├── logo192.png
├── logo512.png
├── manifest.json
└── robots.txt
```

---

# Generative AI Integration

After breed prediction, the Gemini API generates:

- Breed characteristics
- Estimated weight and height
- Diet recommendations
- Vaccination schedule
- Veterinary care suggestions

The generated information is tailored for Indian livestock and agriculture use cases.

---

# Real-World Applications

- Smart Farming
- Livestock Identification
- Precision Agriculture
- AI-Assisted Veterinary Support
- Animal Breed Recognition
- Agricultural Decision Support Systems

---

# Project Structure

```text
project-root/
├── Model Training/
├── Models/
├── public/
├── src/
├── Server.py
├── package.json
├── package-lock.json
└── .gitignore
```

---

# Setup & Installation

This project consists of two components:

- Backend (FastAPI)
- Frontend (React.js)

---

## 1. Clone the Repository

```bash
git clone https://github.com/Pavan-Kumar-2095/Bovine_Breed_Classification.git
cd Bovine_Breed_Classification
```

---

## 2. Backend Setup

### Install Dependencies

```bash
pip install fastapi uvicorn tensorflow numpy pillow requests python-dotenv google-generativeai
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Backend

```bash
python Server.py
```

or

```bash
uvicorn Server:app --reload --host 0.0.0.0 --port 5000
```

The backend will be available at:

```
http://localhost:5000
```

---

## 3. Frontend Setup

### Install Dependencies

```bash
npm install
```

### Start the Development Server

```bash
npm start
```

The frontend will be available at:

```
http://localhost:3000
```

---

# System Workflow

```text
Input Image
      │
      ▼
Cow vs Buffalo Classification
      │
      ▼
Breed Classification
      │
      ▼
Confidence Score Generation
      │
      ▼
Gemini AI Veterinary Analysis
      │
      ▼
Prediction Results Display
```