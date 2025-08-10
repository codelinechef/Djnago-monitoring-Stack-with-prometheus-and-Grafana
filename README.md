# 🚀 FinWatch — Django Monitoring Stack with Prometheus & Grafana

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.5-green?logo=django)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-orange?logo=prometheus)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?logo=grafana)](https://grafana.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-Creative%20Commons-lightgrey)]()

---

## 📊 About the Project

**FinWatch** is a monitoring-ready Django backend stack built for observability and reliability. It leverages **Prometheus** for scraping app metrics and **Grafana** for interactive dashboards, enabling a Site Reliability Engineer (SRE) mindset from Day 1.

> 🧠 Ideal for building production-grade APIs with monitoring baked in.

---

## 🛠️ Tech Stack

| Layer           | Tools & Services                                                                 |
|----------------|------------------------------------------------------------------------------------|
| Backend API     | ![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white) |
| Language        | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) |
| Monitoring      | ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?logo=prometheus&logoColor=white) |
| Dashboarding    | ![Grafana](https://img.shields.io/badge/-Grafana-F46800?logo=grafana&logoColor=white) |
| Containerization| ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white) |
| Database        | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white) |

---

## 📁 Project Structure

```bash
FinWatch_project/
│
├── app/                    # Django app
├── monitoring/
│   └── metrics/
│       └── prometheus.yml  # Prometheus configuration
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md

⚙️ How to Run Locally
🧰 Prerequisites
Docker & Docker Compose

Python 3.10+

Git

# 1️⃣ Clone the repo
git clone https://github.com/codelinechef/Djnago-monitoring-Stack-with-prometheus-and-Grafana.git
cd FinWatch_project

# 2️⃣ Create .env file
cp .env.example .env

# 3️⃣ Build and start services
docker-compose up --build

🔍 API Testing
After the app starts:

API base: http://localhost:8000/api/

Swagger (optional): http://localhost:8000/docs/

Use tools like:
Postman
cURL
httpie

📈 Monitoring Setup
🔥 Prometheus
Access Prometheus at: http://localhost:9090
Scrapes /metrics/ endpoint of Django app

📊 Grafana

Default credentials:
Username: admin
Password: admin
Visit: http://localhost:3000
Import dashboards or use JSON to customize

✅ Prometheus Metrics
Sample output from /metrics/ endpoint:

txt
Copy
Edit
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 1470.0
...

🌟 Features
🔐 Secure, production-ready Django stack

📡 Prometheus metrics ready-to-scrape

📊 Grafana dashboards for real-time insights

🐳 Fully containerized using Docker

⚙️ Environment-driven config using .env

🧠 Skills Demonstrated
Python 🐍

Django Framework ⚙️

Docker & Compose 🐳

Monitoring with Prometheus 🔥

Dashboarding with Grafana 📊

REST APIs / DevOps Practices 🛠️

Container Orchestration Fundamentals 🚢

🧳 Author
Anant Sharma
Software Developer | Backend | Python | AI-Driven Systems
