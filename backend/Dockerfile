# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Install PyTorch (CPU-only) directly from official wheel index
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install your project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Render auto-detects)
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]