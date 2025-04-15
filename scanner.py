# original codebase to show how the script would be laid out to capture actual realtime data on a network.
from scapy.all import sniff
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt
from collections import defaultdict

def scan_wifi(timeout=15):
    ap_list = defaultdict(dict)

    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            ssid = pkt[Dot11Elt].info.decode(errors="ignore")
            bssid = pkt[Dot11].addr3
            try:
                dbm = pkt.dBm_AntSignal
            except:
                dbm = "N/A"
            channel = int(ord(pkt[Dot11Elt:3].info))
            ap_list[bssid] = {
                "ssid": ssid,
                "bssid": bssid, 
                "signal": dbm,
                "channel": channel,
            }

    print(f"[*] Scanning for WiFi access points...")
    sniff(iface="wlan0mon", prn=packet_handler, timeout=timeout, monitor=True) #wlan0mon will need to be replaced with a monitor-mode interface

    return list(ap_list.values())
