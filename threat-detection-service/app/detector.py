from app.rules import (
    is_suspicious_ip,
    is_brute_force_attempt,
    is_malicious_payload,
)


def detect_threat(log_event: dict) -> dict:
    alerts = []

    ip = log_event.get("ip")
    failed_attempts = log_event.get("failed_attempts", 0)
    payload = log_event.get("payload", "")

    if ip and is_suspicious_ip(ip):
        alerts.append("Suspicious IP detected")

    if is_brute_force_attempt(failed_attempts):
        alerts.append("Possible brute force attack")

    if payload and is_malicious_payload(payload):
        alerts.append("Malicious payload detected")

    return {
        "threat_detected": len(alerts) > 0,
        "alerts": alerts
    }
