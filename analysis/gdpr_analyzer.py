import pandas as pd
import re
import json

PERSONAL_DATA_PATTERNS = {
    'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    'ip': r'\b\d{1,3}(?:\.\d{1,3}){3}\b',
    'phone': r'\+?\d[\d\s-]{7,15}',
}

def analyze_personal_data(df):
    report = {'total_rows': len(df), 'issues': []}
    for idx, row in df.iterrows():
        row_issues = {}
        for col, val in row.items():
            if pd.isna(val):
                continue
            for data_type, pattern in PERSONAL_DATA_PATTERNS.items():
                if re.search(pattern, str(val)):
                    row_issues[col] = data_type
        if row_issues:
            report['issues'].append({'row': idx, 'fields': row_issues})
    report['risk_score'] = len(report['issues']) / len(df) * 100
    return report

def save_report(report, file='results/gdpr_report.json'):
    with open(file, 'w') as f:
        json.dump(report, f, indent=4)
