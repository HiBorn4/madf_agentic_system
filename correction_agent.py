import pandas as pd
from fuzzywuzzy import process

VALID_COUNTRIES = [
    "United States", "Canada", "United Kingdom", "Australia", "India",
    "Germany", "France", "Japan", "China", "Brazil"
]

def correct_data(df: pd.DataFrame, issues: list):
    """
    Fix:
      - Standardize names (title case).
      - Drop exact duplicates.
      - Correct country via fuzzy match.
    Returns:
      cleaned_df, logs
    """
    logs = []

    # Work on a copy to avoid SettingWithCopyWarning
    df = df.copy()

    # Standardize names
    df.loc[:, 'name'] = df['name'].str.title()

    # Drop duplicates
    before = len(df)
    df = df.drop_duplicates(subset=['name', 'email', 'country']).copy()
    dropped = before - len(df)
    if dropped:
        logs.append(f"Dropped {dropped} duplicate row(s)")

    # Correct country
    def fix_country(c):
        if pd.isna(c):
            return c
        match, score = process.extractOne(c, VALID_COUNTRIES)
        return match if score >= 80 else c

    df.loc[:, 'country_corrected'] = df['country'].apply(fix_country)
    for idx, (orig, corr) in df[['country', 'country_corrected']].iterrows():
        if orig != corr:
            logs.append(f"Row {idx}: country '{orig}' → '{corr}'")

    df.loc[:, 'country'] = df['country_corrected']

    df = df.drop(columns=['country_corrected'])

    return df, logs
