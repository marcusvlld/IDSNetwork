import json
from datetime import datetime


LOG_FILE = "logs/alerts.json"


def save_log(event_type, source_ip, destination_ip, severity):

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event": event_type,
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "severity": severity
    }

    try:

        with open(LOG_FILE, "a") as file:
            file.write(json.dumps(log_entry) + "\n")

    except Exception as error:
        print(f"Erro ao salvar log: {error}")

