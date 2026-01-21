# GDPR-Compliance-Toolkit

A lightweight Python toolkit to **analyze datasets for personal data**, generate **GDPR compliance reports**, and visualize risk trends in a dashboard.

---

## Features
- Detect personal data: emails, IPs, phone numbers
- Risk analysis and reporting (JSON)
- Dashboard visualization of detected issues
- Sample dataset included
- Optional: data anonymization and DSAR simulation



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

```mermaid
flowchart LR
    A[Dataset Files] --> B[Dataset Parser]
    B --> C[GDPR Analyzer]
    C --> D[JSON Report]
    C --> E[Flask Dashboard]
    E --> F[Charts & Tables]
    D --> F
    B --> G[Optional: Anonymization / DSAR Simulation]

