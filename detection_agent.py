import re
import pandas as pd

def detect_issues(df: pd.DataFrame):
    """
    Scan for:
      - missing/malformed emails
      - duplicate rows
      - country values not in valid list
    Returns: df with added flags, and list of issues.
    """
    issues = []

    # Email check
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    df['email_valid'] = df['email'].apply(lambda e: bool(email_pattern.match(str(e))))
    for idx, valid in df['email_valid'].items():
        if not valid:
            issues.append((idx, 'email', df.at[idx, 'email']))

    # Duplicates
    df['is_duplicate'] = df.duplicated(subset=['name','email','country'], keep=False)
    dup_idxs = df.index[df['is_duplicate']].tolist()
    for idx in dup_idxs:
        issues.append((idx, 'duplicate', df.loc[idx].to_dict()))

    # Country check (list loaded later)
    df['country_valid'] = False  # to be filled after load
    # actual country check happens in correction agent

    return df, issues
