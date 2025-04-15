# main.py
# from scanner import scan_wifi # to scan real networks
from scanner_mock import scan_wifi # for mocked scanning
from detector import detect_threats
import json

#Get the WiFi Data (real or mocked)
wifi_data = scan_wifi(timeout=10)
print(f"[+] Found {len(wifi_data)} networks.\n")

#Send the data to Gemini for Analysis

print("[*] Sending data to Gemini for analysis...")
result = detect_threats(wifi_data)
print("\n[!] Gemini's Analysis:\n")
print(result)
