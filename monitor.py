import subprocess
import psutil
from datetime import datetime

SERVICES = ["ssh", "cron"]

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

line = f"{now} CPU={cpu}% MEM={mem}% DISK={disk}%"
print(line)

alerts = []
if cpu > 80:
    alerts.append("CPU usage is high")
if mem > 80:
    alerts.append("Memory usage is high")
if disk > 80:
    alerts.append("Disk is almost full")

for name in SERVICES:
    result = subprocess.run(["systemctl", "is-active", name],
                            capture_output=True, text=True)
    status = result.stdout.strip()
    print(f"Service {name}: {status}")
    if status != "active":
        alerts.append(f"Service {name} is not running")

with open("monitor.log", "a") as f:
    f.write(line + "\n")
    for a in alerts:
        f.write(f"{now} ALERT: {a}\n")
        print("ALERT:", a)
