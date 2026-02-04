Phishing URL Detector (Rule-Based)

📌 Overview
This project is a beginner-friendly **rule-based phishing URL detection tool** built using Python.  
It analyzes URL characteristics commonly associated with phishing attacks and classifies links as **Likely Safe** or **Likely Phishing**.

This project focuses on **understanding security logic**, not machine learning.



⚙️ Features
- Detects IP-based URLs
- Checks URL length
- Identifies suspicious phishing keywords
- Analyzes excessive subdomains
- Simple and explainable risk scoring



🛠️ Tech Stack
- Python
- Regular Expressions
- `urllib.parse`



🚀 How It Works
Each URL is analyzed using multiple rules:
- Longer URLs increase risk
- IP addresses instead of domains increase risk
- Phishing-related keywords increase risk
- Too many subdomains increase risk

If the total score exceeds a threshold, the URL is flagged as phishing.



▶️ How to Run

```bash
python detector.py
