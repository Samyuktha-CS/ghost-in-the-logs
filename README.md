# 👻 Ghost in the Logs: Privacy-First Local AI Security & Anomaly Detective

Built for the Hacktoberfest 2026 Open-Source AI Challenge (Week 4: Ghost in the Machine).

## 💡 Overview
In cybersecurity and cloud administration, pasting sensitive server, authentication, or firewall logs into third-party cloud chatbots creates severe data exfiltration and compliance risks. 

*Ghost in the Logs* solves this by running an open-weight language model (llama3.2:1b) *100% locally via Ollama*. It features two modes:
* 🕯️ *Ghost in the Machine Mode:* Personifies security anomalies and server bugs as a spooky ghost story before explaining the fix.
* 🛡️ *SOC Cybersecurity Audit Mode:* Delivers a structured threat severity rating, plain-English anomaly breakdown, and actionable remediation steps.

## ⚙️ Architecture
System / Auth Logs ➔ Streamlit Web UI (Python) ➔ Local Ollama API (localhost:11434) ➔ Llama 3.2 (1B) Open-Weight Model

## 🚀 How to Run Locally
1. Install [Ollama](https://ollama.com) and pull the lightweight open-weight model:
   ```bash
   ollama pull llama3.2:1b
