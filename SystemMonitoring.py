import psutil

def monitor_system():
    """
    Monitors system resources like CPU, RAM, and battery.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    battery = psutil.sensors_battery()

    report = f"""
    🔥 CPU Usage: {cpu_usage}%
    🏗 Memory Usage: {memory.percent}%
    🔋 Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else '(Not Charging)'}
    """
    return report

print(monitor_system())
