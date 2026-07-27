# 🩺 CareBot – Hybrid AI Healthcare Assistant

> An intelligent healthcare chatbot that combines **Machine Learning (Random Forest)** with **Google Gemini 2.5 Flash Lite** to provide preliminary disease prediction, multilingual medical guidance, and voice-enabled interaction.

---

# 📖 About The Project

**CareBot** is a hybrid AI-powered healthcare assistant developed to improve access to preliminary healthcare guidance, particularly for people living in rural and resource-limited areas.

The system combines the prediction capability of a **Random Forest Machine Learning model** with the reasoning ability of **Google Gemini 2.5 Flash Lite**. Instead of relying solely on a Large Language Model, CareBot first predicts possible diseases using a trained ML model based on user symptoms and then utilizes Gemini to generate structured, easy-to-understand medical guidance.

CareBot follows a **hybrid AI architecture** where Machine Learning provides reliable disease prediction while Gemini enhances the explanation, symptom interpretation, preventive measures, and home-care guidance.

The chatbot is designed strictly for **preliminary healthcare assistance** and **does not replace professional medical diagnosis or treatment**.

---

# ✨ Features

## 🧠 Hybrid AI Diagnosis

* Hybrid AI architecture combining Machine Learning and Large Language Models
* Random Forest based disease prediction
* Top-3 possible disease prediction with confidence scores
* AI-generated medical explanations
* Preliminary health guidance and symptom interpretation

---

## 🩺 Medical Assistance

* Symptom-based disease prediction
* Disease information queries
* Prevention and healthcare guidance
* Natural home remedies
* Doctor consultation recommendations
* Medical disclaimer for every diagnosis

---

## 🌍 Multilingual Support

* Automatic language detection
* Responds in the user's language
* Supports English, Hindi, Gujarati, Marathi, Tamil, Telugu, Bengali, Punjabi, and many more languages supported by Gemini

---

## 🎙️ Voice Interaction

* Speech-to-Text using Google Speech Recognition
* Voice input through microphone
* Hands-free healthcare interaction

---

## 🛡️ AI Safety Features

* Domain-restricted medical chatbot
* Crisis & self-harm detection
* Emergency helpline recommendations
* Prompt injection protection
* Jailbreak resistance
* Ethical AI responses
* Prevents non-medical conversations

---

## 🎨 User Experience

* Modern Streamlit interface
* Real-time streaming responses
* Conversation memory
* Interactive chat interface
* Responsive layout

---

# 🛠️ Tech Stack

| Category                  | Technologies                      |
| ------------------------- | --------------------------------- |
| **Programming Language**  | Python                            |
| **Frontend**              | Streamlit                         |
| **Machine Learning**      | Scikit-learn (Random Forest)      |
| **Large Language Model**  | Google Gemini 2.5 Flash Lite      |
| **AI SDK**                | Google GenAI SDK (`google-genai`) |
| **Speech-to-Text**        | SpeechRecognition                 |
| **Environment Variables** | python-dotenv                     |
| **Model Serialization**   | Joblib                            |
| **Language Detection**    | langdetect                        |

---

# 📂 Project Structure

```text
CareBot/
│
├── app.py                 # Streamlit frontend
├── brain.py               # AI reasoning and chatbot logic
├── model.py               # Disease prediction pipeline
├── model_loader.py        # Model loading utilities
├── utils.py               # Symptom extraction & language detection
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

* Python 3.9 or above
* Google Gemini API Key
* Internet connection
* Microphone (optional)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Devansh-Mankad/CareBot-Hybrid-AI-System-Chatbot-.git
cd CareBot-Hybrid-AI-System-Chatbot-
```

---

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

The application will launch locally in your browser.

---

# ⚙️ System Workflow

```text
User (Text / Voice)
        │
        ▼
Speech Recognition (Optional)
        │
        ▼
Symptom Extraction
        │
        ▼
Random Forest Model
        │
        ▼
Top-3 Disease Predictions
        │
        ▼
Google Gemini 2.5 Flash Lite
        │
        ▼
Medical Explanation
Home Remedies
Prevention
Doctor Recommendation
        │
        ▼
Response Displayed to User
```

---

# 🔒 Safety Features

CareBot incorporates multiple safety mechanisms to promote responsible AI usage.

* Domain-restricted healthcare assistant
* Crisis and self-harm detection
* Emergency mental health helpline support
* Prompt injection prevention
* Jailbreak protection
* Ethical AI response filtering
* Mandatory medical disclaimer
* No replacement for professional medical advice

---

# 📈 Future Enhancements

* User Authentication
* Patient Consultation History
* Hospital Recommendation System
* Medical Report Analysis
* Medicine Reminder System
* Appointment Booking
* Image-Based Symptom Analysis
* Electronic Health Record (EHR) Integration
* Retrieval-Augmented Generation (RAG)
* Cloud Deployment

---

# 👨‍💻 Author

**Devansh Mankad**

Computer Engineering Student

* GitHub: https://github.com/Devansh-Mankad
---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

---
