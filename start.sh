#!/bin/bash

# Start FastAPI backend (port 8080)
echo "🚀 Starting FastAPI server..."
uvicorn api.server:app --host 0.0.0.0 --port 8080 &

# Start Streamlit dashboard (port 8501)
echo "📊 Starting Streamlit dashboard..."
streamlit run dashboard/st_app.py --server.port=8501 --server.address=0.0.0.0
