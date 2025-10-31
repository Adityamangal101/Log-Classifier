# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Install PyTorch (CPU-only) directly from official wheel index
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install your project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy and prepare startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose ports for FastAPI + Streamlit
EXPOSE 8080 8501

# Start both backend and frontend
CMD ["/start.sh"]
