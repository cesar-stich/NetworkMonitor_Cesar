from scanner import ping_host
from utils import format_result

# IPs de prueba (Google, la UNI, Cloudflare)
targets = ["8.8.8.8", "9.9.9.9", "1.1.1.1"]

print("--- 📡 INICIANDO MONITOREO DE RED UNI ---")

for ip in targets:
    esta_vivo = ping_host(ip)
    mensaje = format_result(ip, esta_vivo)
    print(mensaje)


print("")
