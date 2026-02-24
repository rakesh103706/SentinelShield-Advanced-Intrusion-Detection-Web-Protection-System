import re

ATTACK_PATTERNS = {
    "SQL Injection": r"(union|select|insert|drop|--|;)",
    "XSS": r"(<script>|</script>|alert\()",
    "LFI": r"(\.\./|\.\.\\)",
    "Command Injection": r"(;|\|\||&&)",
}

def detect_attack(data):
    for attack, pattern in ATTACK_PATTERNS.items():
        if re.search(pattern, data, re.IGNORECASE):
            return attack
    return None