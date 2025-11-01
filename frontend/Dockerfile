FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Render dynamically assigns the PORT variable
ENV PORT=8501
EXPOSE $PORT

# ✅ Shell command so ${PORT} expands
CMD bash -c "streamlit run dashboard/st_app.py --server.port=${PORT} --server.address=0.0.0.0"
