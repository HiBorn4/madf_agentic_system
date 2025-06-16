import pandas as pd

def enrich_data(df: pd.DataFrame):
    """
    Add:
      - full_address by concatenating street, city, country
      - domain from email
    Returns: df with new columns, and list of enrichment actions.
    """
    logs = []
    # Full address
    if all(col in df.columns for col in ['street','city','country']):
        df['full_address'] = (
            df['street'].fillna('') + ', ' +
            df['city'].fillna('') + ', ' +
            df['country'].fillna('')
        ).str.strip(', ')
        logs.append("Added full_address column")

    # Email domain
    df['email_domain'] = df['email'].apply(lambda e: str(e).split('@')[-1] if '@' in str(e) else '')
    logs.append("Added email_domain column")

    return df, logs
