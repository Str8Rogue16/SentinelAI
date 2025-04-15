# mock data to show the scanner_mock.py should work in theory
from collections import defaultdict

def scan_wifi(timeout=15):
    ap_list = defaultdict(dict)

    # Mocked WiFi Data (simulating scan results)
    ap_list['00:14:22:01:23:45'] = {  # Rogue AP: Same SSID, suspicious BSSID
        "ssid": "Free_Wifi",
        "bssid": "00:14:22:01:23:45", 
        "signal": "-45",
        "channel": 1
    }
    ap_list['00:14:22:01:23:46'] = {  # Duplicate SSID, different BSSID
        "ssid": "Free_Wifi",
        "bssid": "00:14:22:01:23:46", 
        "signal": "-50",
        "channel": 6
    }
    ap_list['00:14:22:01:23:47'] = {  # Another real AP for diversity
        "ssid": "Home_Network",
        "bssid": "00:14:22:01:23:47", 
        "signal": "-60",
        "channel": 11
    }
    ap_list['00:14:22:01:23:48'] = {  # Rogue AP with strong signal
        "ssid": "Free_Wifi", 
        "bssid": "00:14:22:01:23:48", 
        "signal": "-20",  # Stronger signal, suspicious
        "channel": 1
    }

    print(f"[*] Mocked WiFi Access Points:\n")
    for ap in ap_list.values():
        print(ap)

    return list(ap_list.values())
