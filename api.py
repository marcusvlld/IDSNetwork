from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_FILE = "logs/alerts.json"


@app.get("/alerts")
def get_alerts():

    alerts = []

    try:

        with open(LOG_FILE, "r") as file:

            for line in file:

                line = line.strip()

                # Ignora linhas vazias
                if not line:
                    continue

                try:
                    alerts.append(json.loads(line))

                except json.JSONDecodeError:
                    # Ignora linhas corrompidas/parciais
                    continue

    except FileNotFoundError:

        return {
            "error": "Arquivo de logs não encontrado"
        }

    return alerts

@app.get("/stats")
def get_stats():

    alerts = []

    try:

        with open(LOG_FILE, "r") as file:

            for line in file:
                alerts.append(json.loads(line))

    except FileNotFoundError:

        return {
            "error": "Arquivo não encontrado"
        }

    return {
        "total_alerts": len(alerts)
    }

@app.get("/health")
def health():

    return {
        "status": "online"
    }

app.mount("/", StaticFiles(directory="dashboard", html=True), name="dashboard")
