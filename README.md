# SentinelAI

**AI-Powered Wireless Threat Detection System**

SentinelAI is an AI-enhanced cybersecurity tool that scans WiFi and cellular environments to detect rogue access points, spoofed SSIDs, and other wireless anomalies. It uses Google's Gemini API for intelligent analysis and threat scoring based on real-time network data.

---

## 🔍 Features

- 📡 Scans WiFi networks for duplicate SSIDs and suspicious signal patterns
- 🤖 Uses Gemini API for anomaly detection and threat analysis
- 🚨 Flags rogue access points and provides human-readable recommendations
- 💻 CLI-based prototype with support for mocked and real data (Linux-based scanning)
- 🔐 MIT Licensed and open for extension and integration

---

## 🚀 Quick Start

> **Note:** Scanning WiFi networks requires a Linux machine and monitor-mode enabled interface.

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/SentinelAI.git
   cd SentinelAI
2. ** Install Dependencies:**
   ```bash
   pip install -r requirements.txt
3. ** Add your Gemini API key to .env or .sources file:
   ```bash
   GEMINI_API_KEY=your_key_here
4. ** Run version for demo/testing
   ```bash
   python main.py

## 🧠 How It Works
SentinelAI uses scapy to capture WiFi access point data and analyzes it for anomalies using the Gemini AI model. It detects:
Multiple BSSIDs with same SSID on different channels
Signal strength anomalies suggesting spoofing
Potential rogue APs with unusually strong signals
   
** Example Anlaysis:
''' json 
{
  "ssid": "Free_Wifi",
  "anomaly": "Signal strength variance",
  "threat_level": "Moderate",
  "recommendation": "Investigate strong APs for legitimacy."
}


## 🛠️ Tech Stack
Python 3.12+
Scapy (for packet sniffing)
Google Gemini API (AI analysis)
dotenv (for API key management)

## 📜 License
MIT License — see LICENSE for details.

## 💡 Future Plans
Cellular tower scanning (Android device integration or SDR)
Real-time dashboard
Threat scoring history and logging
Deployment as Raspberry Pi perimeter sensor

 ## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

## 🔗 Credits
Google Generative AI (Gemini)
Scapy
