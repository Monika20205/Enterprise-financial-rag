FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Install CPU-only PyTorch
RUN pip install --no-cache-dir \
    torch==2.2.2+cpu \
    torchvision==0.17.2+cpu \
    torchaudio==2.2.2+cpu \
    --index-url https://download.pytorch.org/whl/cpu

# Install remaining packages without upgrading torch
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --no-deps sentence-transformers==2.7.0
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]