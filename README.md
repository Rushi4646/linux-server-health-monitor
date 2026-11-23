# Linux Server Health Monitor

A Python tool that checks the health of a Linux server and logs the results.

## Features
- Monitors CPU, memory and disk usage
- Checks if important services (ssh, cron) are running
- Writes results and alerts to monitor.log
- Runs automatically every 5 minutes using cron

## Requirements
- Linux (tested on Kali Linux)
- Python 3 and psutil

## Setup
python3 -m venv venv
source venv/bin/activate
pip install psutil
python monitor.py

## Run automatically with cron
*/5 * * * * cd /path/to/server-monitor && ./venv/bin/python monitor.py >> cron.out 2>&1

## Sample Output
![Sample output](screenshot.png)

## Note
Service names differ between Linux families: use `ssh` and `cron` on Kali/Debian, and `sshd` and `crond` on RHEL/Rocky. Change the SERVICES list in monitor.py accordingly.

## Author
Rushikesh Hindule
