# 🧠 Log Classification with Hybrid NLP Framework

This project implements an intelligent **Hybrid Log Classification System** that combines **Regex**, **ML (Sentence Transformer + Logistic Regression)**, and **LLM-based approaches** to accurately classify log messages into categories.  
It’s designed as a complete end-to-end system — from preprocessing and model training to API deployment — making it a showcase of both **Machine Learning** and **Software Engineering** skills.

---

## ⚙️ Hybrid Classification Pipeline

The system uses a **three-stage decision pipeline** for log classification:

1. **🧩 Regular Expression (Regex)**
   - Handles simple and recurring log patterns efficiently.
   - Useful for logs with predictable formats (e.g., “ERROR 404”, “Connection Timeout”).

2. **🔍 Sentence Transformer + Logistic Regression**
   - Manages complex log messages with structured training data.
   - Sentence embeddings are extracted using `sentence-transformers`, and classification is done via Logistic Regression.

3. **🧠 Large Language Model (LLM)**
   - Used when the training data is limited or ambiguous.
   - Acts as a fallback classifier for logs that don’t match Regex or model predictions confidently.

---

## 📁 Project Structure

```
Log_classification_project/
│
├── api/
│   └── server.py                # FastAPI server for inference
│
├── src/
│   ├── classify.py              # Core classification pipeline
│   ├── processor_regex.py       # Regex-based classification logic
│   ├── preprocess.py            # Text cleaning & preprocessing functions
│
├── models/
│   ├── log_model.pkl            # Trained Logistic Regression model
│   └── sentence_transformer/    # Sentence Transformer embeddings
│
├── resources/
│   ├── example_logs.csv         # Example input dataset
│   └── arch.png                 # Architecture diagram
│
├── Dockerfile                   # Docker build configuration
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/log-classification.git
cd log-classification
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv logenv
logenv\Scripts\activate        # For Windows
```
### 🔗 Download Pre-Trained Model
You can download the trained model here:
👉 [Google Drive Link](https://drive.google.com/your-link)

Once downloaded, place it inside:
models/log_classifier.joblib

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI Server
```bash
cd api
uvicorn server:app --reload
```

Server will start at:  
- 🌐 `http://127.0.0.1:8000/`  
- 📘 Docs: `http://127.0.0.1:8000/docs`  
- 🔍 Redoc: `http://127.0.0.1:8000/redoc`

---

## 💻 Optional: Streamlit Frontend

A simple **Streamlit dashboard** can be used to upload a CSV file and visualize results (predicted log categories, confidence, charts).

Run it with:
```bash
streamlit run app.py
```

---

## 🐳 Docker Deployment

### 1️⃣ Build Docker Image
```bash
docker build -t log-classification-app .
```

### 2️⃣ Run Docker Container
```bash
docker run -p 8000:8000 log-classification-app
```

### 3️⃣ Access the App
Open your browser and go to:  
👉 `http://localhost:8000/docs`

---

## 📊 Example Input

| source | log_message |
|--------|--------------|
| app1 | Connection failed due to timeout |
| app2 | FileNotFoundError: dataset.csv missing |

---

## 📈 Example Output

| source | log_message | target_label |
|--------|--------------|---------------|
| app1 | Connection failed due to timeout | NetworkError |
| app2 | FileNotFoundError: dataset.csv missing | IOError |

---

## 🧾 Logging

The project uses Python’s built-in **`logging`** module for:
- Tracking prediction requests
- Monitoring model inference time
- Debugging unexpected log formats

Logs appear directly in the **VS Code terminal** or **Docker container logs** during runtime.

---

## 🧠 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Language** | Python |
| **Frameworks** | FastAPI, Streamlit |
| **ML/NLP** | Sentence-Transformers, Scikit-learn |
| **Visualization** | Plotly, Matplotlib |
| **Deployment** | Docker |
| **Version Control** | Git & GitHub |

---

## 👨‍💻 Author

**Aditya Mangal**  
💼 Data Science & ML Developer  
🔗 [LinkedIn](https://linkedin.com/in/aditya-mangal)  
📂 [GitHub](https://github.com/aditya-mangal)

---

## 🪪 License
This project is for **educational and portfolio purposes** only.  
All rights reserved © 2025 Aditya Mangal.
