# 🛡 Mini SIEM Tool - Python

A simple security monitoring tool built using Python. It simulates basic SIEM functionalities like:

-  Real-time failed login detection from log files
-  File tampering detection using SHA-256 hashing
-  Multi-threaded operation for concurrent monitoring

##  How it works

- **Log Monitor**: Watches a log file and alerts if an IP fails login multiple times.
- **File Hash Monitor**: Continuously checks if a file's hash has changed (detects tampering).

##  Features

- Real-time detection of brute force attempts
- Tamper detection for critical files
- Beginner-friendly and lightweight

##  Run it

```bash
python mini_siem.py
## Author

[Joseph Rithin](https://www.linkedin.com/in/joseph-rithin-4a5388321/)

