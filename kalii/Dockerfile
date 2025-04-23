FROM kalilinux/kali-rolling

# Update system and install attack tools
RUN apt-get update -y && \
    apt-get install -y nmap sqlmap hydra metasploit-framework curl wget hping3 python3 python3-requests

# Copy the attack script
COPY attack.py ./kalii/attack.py

# Run the attack script automatically on startup
CMD ["python3", "./kalii/attack.py"]
