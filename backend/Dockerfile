FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

# Render assigns a dynamic PORT
ENV PORT=8000
EXPOSE $PORT

# ✅ Run via shell so $PORT expands correctly
CMD bash -c "uvicorn api.server:app --host 0.0.0.0 --port ${PORT}"
