# GDPR-Compliance-Toolkit

A lightweight Python toolkit to **analyze datasets for personal data**, generate **GDPR compliance reports**, and visualize risk trends in a dashboard.

---

## Features
- Detect personal data: emails, IPs, phone numbers
- Risk analysis and reporting (JSON)
- Dashboard visualization of detected issues
- Sample dataset included
- Optional: data anonymization and DSAR simulation

##Dashboard Preview
| Row | Column | Detected Type |
| --- | ------ | ------------- |
| 0   | email  | email         |
| 0   | phone  | phone         |
| 1   | email  | email         |
| 3   | phone  | phone         |

Detected Personal Data: Shows rows containing sensitive data

Risk Score: Percentage of dataset flagged with personal data

---

## Project Structure
GDPR-Compliance-Toolkit/
├─ ingestion/
├─ analysis/
├─ dashboard/
│ └─ templates/
├─ logs/
├─ results/
├─ run_gdpr_analysis.py
├─ requirements.txt
└─ README.md


---
## Architecture Diagram
Diagram explanation:

Dataset Files: CSV or JSON datasets containing user information

Parser: Reads and loads datasets

Analyzer: Detects personal data and calculates risk

JSON Report: Stores detected issues and risk score

Dashboard: Displays detected issues and risk visually

Optional: Simulate anonymization or DSAR actions


## Architecture Diagram

```mermaid
flowchart LR
    A[Dataset Files] --> B[Dataset Parser]
    B --> C[GDPR Analyzer]
    C --> D[JSON Report]
    C --> E[Flask Dashboard]
    E --> F[Charts & Tables]
    D --> F
    B --> G[Optional: Anonymization / DSAR Simulation]


