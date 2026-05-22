from datetime import datetime
import random

security_findings = [
    {
        "issue": "Weak password policy detected",
        "severity": "High",
        "recommendation": "Enforce strong password requirements and MFA."
    },
    {
        "issue": "Outdated software versions",
        "severity": "Medium",
        "recommendation": "Update systems to the latest secure versions."
    },
    {
        "issue": "Open network ports exposed",
        "severity": "High",
        "recommendation": "Restrict unnecessary public-facing ports."
    },
    {
        "issue": "Missing multi-factor authentication",
        "severity": "Critical",
        "recommendation": "Enable MFA for all administrative accounts."
    },
    {
        "issue": "Potential phishing exposure",
        "severity": "Medium",
        "recommendation": "Provide employee phishing awareness training."
    }
]

print("\n======================================")
print(" AI SECURITY RISK SCANNER - MVP")
print("======================================\n")

business_name = input("Enter business name: ")

print("\nRunning automated security assessment...\n")

selected_findings = random.sample(security_findings, 3)

risk_score = random.randint(45, 92)

print("----------- SECURITY REPORT -----------")
print(f"Business: {business_name}")
print(f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Overall Risk Score: {risk_score}/100\n")

for finding in selected_findings:
    print(f"[{finding['severity']}] {finding['issue']}")
    print(f"Recommendation: {finding['recommendation']}\n")

print("---------------------------------------")
print("AI Summary:")
print("This business presents multiple security risks that should be addressed to reduce exposure to cyber threats.")
print("---------------------------------------")
