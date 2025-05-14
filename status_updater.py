import socket
import json

SERVICES = {
    "Основной сайт ASTRACAT": "astracat.vercel.app",
    "ASTRACAT DNS": "astracat-dns.vercel.app",
    "Генератор Xray VPN": "vpngen.vercel.app",
    "WARP Бот Телеграмм": "https://warpxc-56ul.onrender.com"
}

def check_status(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except:
        return False

statuses = {
    name: {
        "hostname": host,
        "online": check_status(host)
    }
    for name, host in SERVICES.items()
}

with open("status.json", "w", encoding="utf-8") as f:
    json.dump(statuses, f, ensure_ascii=False, indent=2)
