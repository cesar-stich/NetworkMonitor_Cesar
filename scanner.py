import os

def ping_host(ip):
    # Ejecuta un ping silencioso (-n 1 envía solo un paquete)
    status = os.system(f"ping -n 1 {ip} > nul")
    return status == 0