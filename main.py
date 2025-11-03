import os
import time
import psutil

def list_processes():
    print("\n" + "=" * 80)
    print(f"{'PID':<8} {'Name':<25} {'CPU%':<8} {'Memory%':<10} {'Executable Path'}")
    print("-" * 80)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'exe']):
        try:
            info = proc.info
            cpu = info['cpu_percent'] if info['cpu_percent'] is not None else 0.0
            mem = info['memory_percent'] if info['memory_percent'] is not None else 0.0
            exe = info['exe'] if info['exe'] else "N/A"
            print(f"{info['pid']:<8} {info['name']:<25} {cpu:<8.1f} {mem:<10.2f} {exe}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    while True:
        os.system("clear")
        print("Active Processes (Refreshing every 1 sec):\n")
        list_processes()
        time.sleep(1)


