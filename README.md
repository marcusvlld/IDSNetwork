# SentinelNet IDS

> **Um sistema leve de Intrusion Detection System (IDS) desenvolvido em Python para monitoramento de tráfego de rede em tempo real, detecção de ameaças e observabilidade com Grafana + Loki.**

---

## Visão Geral

O **SentinelNet IDS** é um projeto focado em cibersegurança desenvolvido para simular o comportamento de um IDS leve capaz de:

- Capturar pacotes de rede em tempo real
- Detectar atividades suspeitas
- Gerar logs estruturados de segurança
- Agregar logs utilizando Loki
- Visualizar eventos de segurança no Grafana
- Disparar alertas baseados em comportamento suspeito

> Projeto criado com foco em aprendizado prático e portfólio nas áreas de **Cibersegurança**, **Blue Team**, **SOC**, **Observabilidade** e **DevSecOps**.

---

## Funcionalidades

### 📡 Captura de Pacotes
Utilizando **Scapy** para capturar:
- Tráfego TCP
- Pacotes SYN
- Pacotes ICMP

### Detecção de Ameaças
| Ameaça | Status |
|---|---|
| Port Scan | Implementado |
| Ping ICMP (Reconhecimento) | Implementado |
| Monitoramento de Pacotes SYN | Implementado |
| SYN Flood | Planejado |
| ICMP Flood | Planejado |
| Brute Force | Planejado |

### Logging Estruturado
Todos os eventos são armazenados em **logs JSON estruturados**:

```json
{
  "timestamp": "2026-05-21 18:22:10",
  "event": "PORT_SCAN",
  "source_ip": "192.168.0.15",
  "destination_ip": "192.168.0.1",
  "severity": "HIGH"
}
```

### Stack de Observabilidade
Integração completa com:
- **Grafana** — Dashboards e visualizações
- **Loki** — Agregação de logs
- **Promtail** — Coleta de logs
- **Docker Compose** — Orquestração dos serviços

---

## Arquitetura

```
Tráfego de Rede
       ↓
 Scapy Sniffer
       ↓
Engine de Detecção
       ↓
Logs JSON Estruturados
       ↓
   Promtail
       ↓
     Loki
       ↓
Dashboard Grafana
```

---

## Estrutura de Pastas

```
/project
│
├── sniffer.py
├── logger.py
├── api.py
├── docker-compose.yml
│
├── logs/
│   └── alerts.json
│
├── loki/
│   └── local-config.yaml
│
└── promtail/
    └── config.yml
```

---

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento do IDS |
| Scapy | Captura de pacotes |
| FastAPI | API REST |
| Docker | Containerização |
| Grafana | Dashboards e observabilidade |
| Loki | Agregação de logs |
| Promtail | Coleta de logs |
| JSON | Logging estruturado |

---

## Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/marcusvlld/IDSNetwork.git
cd IDSNetwork
```

### 2. Instalar dependências Python
```bash
pip install -r requirements.txt
```

### 3. Iniciar Grafana, Loki e Promtail
```bash
docker compose up -d
```

### 4. Executar o IDS
```bash
sudo python3 sniffer.py
```

### 5. Abrir o Grafana
Acesse: [http://localhost:3000](http://localhost:3000)

```
Usuário: admin
Senha:   admin
```

---

## Lógica de Detecção

### Detecção de Port Scan
O IDS monitora pacotes **TCP SYN** e identifica comportamento suspeito quando múltiplas portas são acessadas por um mesmo IP em um curto período de tempo.

### Detecção ICMP
O IDS detecta **ICMP Echo Requests (Ping)** para identificar possíveis tentativas de reconhecimento de rede.

---

## Dashboards Grafana

Os dashboards disponíveis incluem:

- **Total de Eventos de Segurança**
- **Monitoramento de Port Scan**
- **Eventos por Severidade**
- **Timeline de Ataques**
- **IPs mais Ativos**
- **Eventos Críticos de Segurança**

---

## Queries Loki

**Total de Eventos:**
```logql
count_over_time({job="sentinelnet"}[5m])
```

**Detecção de Port Scan:**
```logql
sum(
  count_over_time({job="sentinelnet", event="PORT_SCAN"}[5m])
)
```

**Eventos de Alta Severidade:**
```logql
{job="sentinelnet", severity="HIGH"}
```

---

## Screenshots

<img width="1919" height="942" alt="Captura de tela 2026-05-21 163956" src="https://github.com/user-attachments/assets/31fe3fcd-47b8-4920-bcb8-1f5acf20f25d" />

--

<img width="1274" height="843" alt="Captura de tela 2026-05-21 164024" src="https://github.com/user-attachments/assets/7d78835d-6c3a-4de6-87e6-5642abad47ac" />

--
 
<img width="1274" height="847" alt="Captura de tela 2026-05-21 164046" src="https://github.com/user-attachments/assets/4bb076e3-91f9-4f00-8a24-087e6b4f51ff" />

--

<img width="1278" height="846" alt="Captura de tela 2026-05-21 164105" src="https://github.com/user-attachments/assets/979a4893-5eac-487b-af04-d91545e31e5c" />

--

<img width="1274" height="848" alt="Captura de tela 2026-05-21 164119" src="https://github.com/user-attachments/assets/48cb38b1-928d-4489-bc6b-c8fe1213afe8" />

--

<img width="1274" height="845" alt="Captura de tela 2026-05-21 164132" src="https://github.com/user-attachments/assets/5804f646-32dd-4482-907b-5ce56db4dfce" />

--

<img width="1272" height="847" alt="Captura de tela 2026-05-21 164148" src="https://github.com/user-attachments/assets/50ea0ecd-743d-494e-8112-a77fdfb526df" />


---

## Melhorias Futuras

- [ ] Detecção de SYN Flood
- [ ] Detecção de ICMP Flood
- [ ] Detecção de Brute Force
- [ ] Integração com SQLite/PostgreSQL
- [ ] Streaming em tempo real com WebSockets
- [ ] Detecção de anomalias com Machine Learning
- [ ] Sistema de regras customizadas

---

## Objetivos de Aprendizado

Este projeto contribuiu para o desenvolvimento prático de habilidades em:

- Análise de tráfego de rede
- Fundamentos TCP/IP
- Inspeção de pacotes
- Detecção de ameaças
- Monitoramento de segurança
- Agregação de logs
- Observabilidade
- Docker
- Operações Blue Team
- Engenharia de Segurança

---

<div align="center">
  <sub>Desenvolvido com foco em aprendizado prático em Cibersegurança e Blue Team.</sub>
</div>
