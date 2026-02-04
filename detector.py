
import re
from urllib.parse import urlparse

def calculate_risk_score(url):
    score = 0

    # Rule 1: Long URL
    if len(url) > 75:
        score += 1

    # Rule 2: IP address instead of domain
    if re.search(r'\d+\.\d+\.\d+\.\d+', url):
        score += 2

    # Rule 3: Suspicious keywords
    suspicious_words = [
        "login", "verify", "update", "secure",
        "account", "bank", "confirm", "signin"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Rule 4: Too many subdomains
    domain = urlparse(url).netloc
    if domain.count('.') > 3:
        score += 1

    return score


def detect_phishing(url):
    score = calculate_risk_score(url)

    if score >= 3:
        return "⚠️ Likely Phishing"
    else:
        return "✅ Likely Safe"


if __name__ == "__main__":
    print("Phishing URL Detector")
    print("---------------------")

    url = input("Enter a URL: ").strip()
    result = detect_phishing(url)

    print("\nResult:", result)
