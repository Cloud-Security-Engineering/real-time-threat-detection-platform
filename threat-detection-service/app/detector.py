from app.rules import (
    is_suspicious_ip,
    is_brute_force_attempt,
    is_malicious_payload,
)


def detect_threat(log_event: dict):
    alerts = []

    # Rule 1: Brute force
    if log_event.get("failed_attempts", 0) > 3:
        alerts.append("Possible brute force attack")

    # Rule 2: Suspicious payload
    if "attack" in log_event.get("payload", "").lower():
        alerts.append("Suspicious payload detected")

    # Rule 3: Blacklisted IP
    blacklist = ["192.168.1.100"]
    if log_event.get("ip") in blacklist:
        alerts.append("Blacklisted IP detected")

    return {
        "threat_detected": len(alerts) > 0,
        "alerts": alerts
    }
