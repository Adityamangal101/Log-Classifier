🧠 Log Classification with Hybrid NLP Framework

This project implements an intelligent Hybrid Log Classification System combining Regex, Machine Learning (Sentence Transformer + Logistic Regression), and LLM-based reasoning to classify log messages into meaningful categories.

It’s a complete end-to-end production system, featuring separate FastAPI backend and Streamlit frontend—packaged via Docker and deployable on Render.

🏗️ Project Architecture
Log_Classification_Project/
│
├── backend/
│   ├── api/
│   │   └── server.py             # FastAPI backend API
│   ├── src/
│   │   ├── classify.py           # Core hybrid classification pipeline
│   │   ├── processor_regex.py    # Regex-based classification logic
│   │   ├── preprocess.py         # Text cleaning and preprocessing
│   ├── models/
│   │   ├── log_model.pkl         # Logistic Regression model
│   │   └── sentence_transformer/ # Sentence Transformer model
│   ├── requirements.txt
│   ├── Dockerfile
│   └── start.sh                  # Backend startup script
│
├── frontend/
│   ├── dashboard/
│   │   └── st_app.py             # Streamlit dashboard for visualization
│   ├── requirements.txt
│   ├── Dockerfile
│   └── start.sh                  # Frontend startup script
│
├── resources/
│   ├── example_logs.csv
│   └── architecture.png
│
└── README.md

⚙️ Hybrid Classification Workflow

The hybrid classifier follows a three-tiered logic flow:

🧩 Regex Layer
Quickly detects well-known or patterned log formats (e.g. ERROR 404, Timeout, Disk full).

🔍 ML Layer (Sentence Transformer + Logistic Regression)
Encodes log messages and predicts labels using a trained model for structured log data.

🧠 LLM Fallback Layer
Invoked when the above two models return uncertain predictions or ambiguous messages.

🚀 Local Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/log-classification.git
cd log-classification

2️⃣ Backend Setup
cd backend
python -m venv logenv
logenv\Scripts\activate          # (Windows)
pip install -r requirements.txt
uvicorn api.server:app --host 0.0.0.0 --port 8000


Endpoints:

API Root → http://127.0.0.1:8000/

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

3️⃣ Frontend Setup
cd ../frontend
pip install -r requirements.txt
streamlit run dashboard/st_app.py


Once running, visit → http://localhost:8501

🧩 Update API_URL inside your Streamlit app to point to your deployed backend API:

API_URL = "https://your-backend-service.onrender.com/classify"

🐳 Docker Setup

Each module (backend + frontend) has its own Dockerfile.

🧠 Build Backend Image
cd backend
docker build -t log-backend .
docker run -p 8000:8000 log-backend

📊 Build Frontend Image
cd ../frontend
docker build -t log-frontend .
docker run -p 8501:8501 log-frontend

🌐 Deploy on Render
1️⃣ Create Two Services:
Service	Folder	Type	Port
Backend Service	/backend	FastAPI (Docker)	8000
Frontend Service	/frontend	Streamlit (Docker)	8501
2️⃣ Environment Variables

In both Render services:

PYTHON_VERSION = 3.10


For backend, also add:

MODEL_PATH = ./models/log_model.pkl

3️⃣ Update Frontend URL

After backend deploy, copy its Render URL and update in st_app.py:

API_URL = "https://your-backend.onrender.com/classify"


Then commit & push:

git add .
git commit -m "Updated backend API URL"
git push origin main


Render will automatically rebuild and redeploy your frontend service.

📊 Example Input & Output
source	log_message
app1	Connection failed due to timeout
app2	FileNotFoundError: dataset.csv missing

Predicted Output:

source	log_message	target_label
app1	Connection failed due to timeout	NetworkError
app2	FileNotFoundError: dataset.csv missing	IOError
🧾 Logging

The system logs:

API requests and responses

Model inference times

Confidence thresholds and fallback logic

Logs appear in your Render dashboard or local Docker console.

🧠 Tech Stack
Category	Tools Used
Language	Python
Frameworks	FastAPI, Streamlit
ML/NLP	Sentence-Transformers, Scikit-learn
Data Viz	Plotly, Matplotlib
Deployment	Docker, Render
Version Control	Git & GitHub
👨‍💻 Author

Aditya Mangal
💼 Data Science & ML Developer
🔗 LinkedIn

📂 GitHub