from collections import Counter
log_file = "sample_log.txt"
failed_ips = []
with open(log_file, "r") as file:
    for line in file:
        if "LOGIN FAILED" in line:
            ip = line.strip().split()[-1]
            failed_ips.append(ip)
failed_counts = Counter(failed_ips)
print("===LOG ANALYSIS REPORT ===")
for ip, count in failed_counts.items():
    if count >= 3:
        print(f"ALERT: suspicious IP {ip} - {count} failed login attempts")
    else:
        print(f"IP {ip} - {count} failed login attempt(s)")