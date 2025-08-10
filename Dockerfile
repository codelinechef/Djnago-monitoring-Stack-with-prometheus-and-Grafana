FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# ✅ Correct Gunicorn entry
CMD ["gunicorn", "FinWatch_project.wsgi:application", "--bind", "0.0.0.0:8000"]
