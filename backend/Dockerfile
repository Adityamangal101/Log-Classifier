FROM python:3.10-slim

# Install system dependencies (needed for torch + some Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install PyTorch CPU wheels
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install all other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy your app source code
COPY . .

# Render/Railway assigns PORT at runtime
ENV PORT=8000
EXPOSE 8000

# Use exec form, no bash needed
CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]
