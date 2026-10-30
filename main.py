import streamlit as st
import ollama

st.set_page_config(page_title="Ghost in the Logs", page_icon="👻", layout="centered")

st.title("👻 Ghost in the Logs: Local AI Security & Anomaly Detective")
st.caption("🔒 100% Offline Open-Weight AI (Llama 3.2 via Ollama) — Zero Cloud Data Exfiltration")

sample_log = """2026-10-30 03:14:07 WARN [AuthService] 5 failed SSH login attempts for user 'admin' from IP 185.220.101.4
2026-10-30 03:14:09 ERROR [Database] Unauthorized query attempt on table 'user_credentials'
2026-10-30 03:14:12 CRITICAL [Firewall] Outbound connection blocked on anomalous port 6660"""

log_input = st.text_area("Paste System, Server, or Terminal Logs:", value=sample_log, height=140)

mode = st.radio(
    "Select Analysis Mode:",
    ["🕯️ Ghost in the Machine (Spooky Hackathon Mode)", "🛡️ SOC Cybersecurity Audit (Resume/Technical Mode)"]
)

if st.button("Analyze Logs Locally 🔮"):
    with st.spinner("Running local open-weight model inference..."):
        if "Ghost" in mode:
            prompt = (
                f"You are a ghost haunting a computer server. Read these logs and first tell a spooky 3-sentence "
                f"ghost story about the intruder or bug inside the machine. Then give 3 clear bullet points explaining "
                f"the actual security issue and how to fix it:\n\n{log_input}"
            )
        else:
            prompt = (
                f"You are a Cloud & Information Security Analyst. Analyze these logs locally. Provide: "
                f"1) Threat Severity (Low/Medium/High), 2) Plain-English explanation of the anomaly, and "
                f"3) 3 actionable remediation steps:\n\n{log_input}"
            )
        try:
            response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": prompt}])
            st.subheader("📜 Local AI Diagnostic Report")
            st.write(response["message"]["content"])
        except Exception as e:
            st.error(f"Make sure Ollama is running! Details: {e}")