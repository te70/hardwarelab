
# Hardware lab

## Overview
Data exfiltration is the unauthorized transfer or theft of sensitive data from a system or network, usually carried out by cybercriminals or malicious insiders. In this case, data saved on an SQL server beloging to a small company was exfiltrated.

The objective of this lab was to demonstrate how data can be exfiltrated from a small network. The network was setup using docker. The network comprised of a web server, ftp server, MySQL database and an IDS; Suricata. The attacker used Kali Linux to conduct the attack and exfiltrated data to a malicious server running on Flask. 

The attack utilized a python script which did an SQL injection attack using sqlmap, a denial of service attack using hping and the data collected by sqlmap was exfiltrated to the malicious server. The packets were also captured by Wireshark. 

On Wireshark, I was able to filter packets using SQL, TCP and IP addresses. The IDS was able to capture malicious signatures.

Finally, I encountered challenges in setting up the web server since it utilized php, so I had to add php-fpm and the right connections to MySQL. Moreover, before implementing sqlmap and hping, I had attempted to do the injection and DoS attack manually which was tiresome. In future, I hope to refine the attack to run on a larger network and automate tasks using AI. 

## Run Locally

Clone the project

```bash
  git clone https://github.com/te70/hardwarelab.git
```

Go to the project directory

```bash
  cd hardwarelab
```

Pull the images (make sure you have docker installed)

```bash
  sudo docker compose build
```

Start 

```bash
  sudo docker compose up
```


## Running Tests

To run tests, open the Kali container, move the root directory, the attack script is already mounted, run;

```bash
  python3 attack.py
```
One shold see sqlmap, hping and data exfiltration running on Kali (takes a while so be patient) and capture packets on Wireshark

## License

[MIT](https://choosealicense.com/licenses/mit/)

