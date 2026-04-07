def format_result(ip, is_online):
    icon = "✅" if is_online else "❌"
    state = "ONLINE" if is_online else "OFFLINE"
    return f"{icon} Host {ip}: {state}"