#!/bin/bash

# Use the same port Render provides
PORT=${PORT:-10000}

# Start FastAPI in the background (same port)
echo "🚀 Starting FastAPI server..."
uvicorn api.server:app --host 0.0.0.0 --port $PORT &

# Start Streamlit on the same port (Render exposes only one port)
echo "📊 Starting Streamlit dashboard..."
streamlit run dashboard/st_app.py --server.port=$PORT --server.address=0.0.0.0
