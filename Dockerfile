FROM python:3.10-slim

# FFmpeg इंस्टॉल करें
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn pydantic requests

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
