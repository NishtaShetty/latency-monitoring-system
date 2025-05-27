import subprocess
import time

def ping(host: str, count: int = 4):
    response = subprocess.run(['ping', '-c', str(count), host], capture_output=True, text=True)
    print(response.stdout)
    return response.returncode == 0

if __name__ == "__main__":
    while True:
        success = ping("8.8.8.8")
        print("Ping success" if success else "Ping failed")
        time.sleep(5)
