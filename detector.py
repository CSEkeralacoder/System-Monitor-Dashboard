import psutil
import time
import json
from datetime import datetime

LOG_FILE = "detections.log"

def get_system_stats():
    """Collect CPU, memory, and process information."""
    stats = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "process_count": len(psutil.pids())
    }
    return stats

def log_stats(stats):
    """Write collected stats to detections.log as JSON."""
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(stats) + "\n")

def monitor_system():
    """Continuously monitor system metrics."""
    print("[*] Detector started. Monitoring system performance...")
    print("[*] Press Ctrl + C to stop.\n")

    while True:
        stats = get_system_stats()
        log_stats(stats)
        print(f"[{stats['timestamp']}] CPU: {stats['cpu_percent']}% | "
              f"Memory: {stats['memory_percent']}% | "
              f"Processes: {stats['process_count']}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()

