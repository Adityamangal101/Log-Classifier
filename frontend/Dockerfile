FROM python:3.10-slim


WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Render assigns PORT dynamically
ENV PORT=8501
EXPOSE 8501

# Exec form version of Streamlit command
CMD ["streamlit", "run", "dashboard/st_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
