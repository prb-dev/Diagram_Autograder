FROM python:3.12-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Set up the application environment
WORKDIR /app
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the SpaCy model
RUN python3 -m spacy download en_core_web_md

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]