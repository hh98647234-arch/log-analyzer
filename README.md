# Python log analyzer
A sample cybersecurity tool built with python to analyze login logs and detect suspicious IP addresses based on repeated failed login attempts.
## Features
- Reads login activity from a log file
- Detects failed login attempts
- Extracts IP addresses automaticlly
- Counts failed attempts for each IP
- Flags an IP as suspicious after 3 or more failed attempts
  ## Technologies Used
- Python
- Python collections(counter)
- Log Analysis
- Basic security monitoring
  ## Project files
- `Log_analyzer.py` - main python program
- `Sample_log.txt` - sample login log data
  ## Example output
  ```text
  ===ALERT: Suspicious IP 192.168.1.25 - 3 failed login attempts
IP 10.0.0.8 - 1 failed login attempts (s)
 ## Cybersecurity concepts
 this project demonstrates basic SOC and cybersecurity concepts including log analysis, suspicious activity detection, IP monitoring, and failed-login analysis.
  ## Disclaimer
  this project is for educational and cybersecurity learning purposes.
