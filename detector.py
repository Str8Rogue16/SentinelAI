# detector.py
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def detect_threats(wifi_data):
    prompt = f"""
    You are an AI cybersecurity agent.

    Analyze the following WiFi scan data and identify:
    - Rogue access points
    - Spoofing attempts
    - Signal anomalies
    - Any suspicious or high-risk signals


    Respond in JSON:
    {{
      "suspicious_devices": [...],
      "anomalies": [...],
      "threat_level": "Low/Moderate/High",
      "recommendation": "..."
    }}

    WiFi Data:
    {wifi_data}
    """

    response = model.generate_content(prompt)
    return response.text
