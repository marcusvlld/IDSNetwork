from collections import defaultdict
from datetime import datetime
from logger import save_log


# Armazena portas acessadas por IP
connection_tracker = defaultdict(list)

# Configurações
PORT_SCAN_THRESHOLD = 100


def detect_port_scan(src_ip, dst_port):

    current_time = datetime.now()

    # Adiciona porta acessada
    connection_tracker[src_ip].append({
        "port": dst_port,
        "time": current_time
    })

    # Remove conexões antigas (opcional futuramente)

    # Pega portas únicas
    unique_ports = {
        conn["port"]
        for conn in connection_tracker[src_ip]
    }

    # Detecta scan
    if len(unique_ports) >= PORT_SCAN_THRESHOLD:

        print(
            f"\n[ALERTA] Possível Port Scan detectado!"
            f"\nIP suspeito: {src_ip}"
            f"\nPortas acessadas: {len(unique_ports)}\n"
        )

        # Limpa após alerta
        connection_tracker[src_ip].clear()
