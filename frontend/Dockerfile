FROM python:3.10-slim

WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Render dynamically assigns the PORT env variable, default to 8501 for local dev
ENV PORT=8501

EXPOSE $PORT

# Streamlit must use the assigned Render port
CMD ["streamlit", "run", "dashboard/st_app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]