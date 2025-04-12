import os
import hashlib
import threading
import time

def get_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def monitor_file_hash(file_path, interval=5):
    og_hash = get_hash(file_path)
    if og_hash is None:
        print("File not found")
        return
    print(f"Monitoring {file_path} for tampering\n")
    while True:
        if og_hash != get_hash(file_path):
            print(f"ALERT: The file {file_path} has been tampered")
            break
        time.sleep(interval)

def monitor_log(file_path, threshold=3):
    failed_login = {}
    print(f"Monitoring {file_path} for failed login")
    try:
        with open(file_path, "r") as file:
            file.seek(0, os.SEEK_END)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)
                    continue
                if "Failed login" in line:
                    ip = line.strip().split(" - ")[0]
                    failed_login[ip] = failed_login.get(ip, 0) + 1
                    if failed_login[ip] == threshold:
                        print(f"ALERT: IP:{ip} has {threshold} failed attempts")
    except FileNotFoundError:
        print(f"File {file_path} does not exist")

def run_mini_siem(log_file, hash_file):
    log_thread = threading.Thread(target=monitor_log, args=(log_file,))
    hash_thread = threading.Thread(target=monitor_file_hash, args=(hash_file,))
    log_thread.start()
    hash_thread.start()
    log_thread.join()
    hash_thread.join()

run_mini_siem("system_logs.txt", "system_logs.txt")
