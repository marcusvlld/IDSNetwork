from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP
from detector import detect_port_scan
from logger import save_log


def process_packet(packet):
    # Verifica se o pacote possui camada IP
    if packet.haslayer(IP):

        timestamp = datetime.now().strftime("%H:%M:%S")

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "OTHER"
        src_port = "N/A"
        dst_port = "N/A"

        # Verifica se é TCP
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            print(f"Detectando porta: {dst_port}")
            detect_port_scan(src_ip, dst_port)

            save_log(
                event_type="PORT_SCAN",
                source_ip=src_ip,
                destination_ip=dst_ip,
                severity="HIGH"
            )

        # Verifica se é UDP
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        # Verifica se é ICMP
        elif packet.haslayer(ICMP):

            icmp_type = packet[ICMP].type
            if icmp_type == 8:
                protocol = "ICMP ECHO REQUEST"

                print(
                    f"\n[ALERTA] Ping detectado!"
                    f"\nOrigem: {src_ip}"
                    f"\nDestino: {dst_ip}\n"
                )

                save_log(
                    event_type="PING_DETECTED",
                    source_ip=src_ip,
                    destination_ip=dst_ip,
                    severity="LOW"
                )

            elif icmp_type == 0:
                 protocol = "ICMP ECHO REPLY"

            else:
                protocol = "ICMP"

        print(
	    f"[{timestamp}] "
            f"[{protocol}] "
            f"{src_ip}:{src_port} -> "
            f"{dst_ip}:{dst_port}"
        )


print("Iniciando captura de pacotes...\n")

sniff(filter="tcp or icmp", prn=process_packet, store=False)
