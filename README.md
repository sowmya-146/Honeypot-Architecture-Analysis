# 🛡️ Analyzing Honeypot Architecture Through an Anatomic Lens

> A Python-based honeypot system for detecting and analyzing real-time cyberattacks

## 📌 Overview

This project implements a custom Python honeypot that simulates vulnerable web services to attract, detect, and analyze cyberattacks. The system captures malicious payloads, logs attacker data in JSON format, and provides visual insights into attack patterns.

**Key Capabilities:**
- Detects SQL Injection, XSS, Command Injection, RFI/LFI, Directory Traversal, and Brute Force attacks
- Real-time terminal monitoring with live attack alerts
- JSON logging with timestamp, IP, and payload data
- Automatic visualization using Matplotlib
- Ngrok integration for remote access
- Runs in isolated VMware/VirtualBox environment

## 🏗️ System Architecture
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ Attacker │────▶│ Ngrok │────▶│ Honeypot │────▶│Detection │
│ Layer │ │ Tunnel │ │ Layer │ │ Layer │
└──────────┘ └──────────┘ └────┬─────┘ └────┬─────┘
│ │
▼ ▼
┌──────────────┐ ┌──────────────┐
│ Logger │ │Visualization │
│ (JSON) │ │ (Matplotlib) │
└──────────────┘ └──────────────┘

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core programming language |
| Socket & http.server | Network communication |
| Regex (re) | Attack pattern detection |
| JSON | Structured logging |
| Matplotlib | Data visualization |
| Ngrok | Remote access tunneling |
| VMware/VirtualBox | Isolated deployment |

## 🚀 Getting Started

### Prerequisites

```bash
- Python 3.8 or higher
- Ubuntu/Kali Linux (recommended)
- VMware or VirtualBox
- Ngrok account (free tier)
- 4GB RAM minimum

## Installation

# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/honeypot-architecture-analysis.git
cd honeypot-architecture-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure Ngrok (optional)
ngrok authtoken YOUR_AUTH_TOKEN

# 4. Run the honeypot
python src/honeypot.py

## Testing the Honeypot

# Test SQL Injection
curl "http://localhost:80/?id=1' OR 1=1--"

# Test XSS
curl "http://localhost:80/?q=<script>alert(1)</script>"

# Test Command Injection
curl "http://localhost:80/?cmd=; cat /etc/passwd"

## 📊 Results & Findings

Metric	Value
Total Interactions	10+
Attacks Detected	4+
Unique Attackers	Multiple IPs
Most Common Attack	SQL Injection & XSS
False Positives	        Zero

## Attack Distribution

SQL Injection      ████████████████████████████████████  40%
XSS                ██████████████████████████████        30%
Command Injection  ██████████████                        15%
Directory Traversal█████████                             10%
RFI/LFI            ████                                   5%

## Sample Log Entry

{
  "timestamp": "2025-11-15 14:23:45",
  "source_ip": "192.168.1.100",
  "source_port": 54321,
  "target_port": 80,
  "attack_types": ["SQL Injection"],
  "payload": "GET /?id=1' OR 1=1-- HTTP/1.1"
}


