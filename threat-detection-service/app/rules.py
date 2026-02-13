SUSPICIOUS_IPS = ["192.168.1.100", "10.0.0.66"]
FAILED_LOGIN_THRESHOLD = 5


def is_suspicious_ip(ip: str) -> bool:
    return ip in SUSPICIOUS_IPS


def is_brute_force_attempt(failed_attempts: int) -> bool:
    return failed_attempts >= FAILED_LOGIN_THRESHOLD


def is_malicious_payload(payload: str) -> bool:
    keywords = ["DROP TABLE", "SELECT *", "<script>", "UNION SELECT"]
    return any(keyword.lower() in payload.lower() for keyword in keywords)
