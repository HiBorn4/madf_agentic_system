import argparse
import pandas as pd
from utils import setup_logger
from detection_agent import detect_issues
from correction_agent import correct_data
from enrichment_agent import enrich_data

def run_pipeline(input_csv, output_csv, log_file):
    logger = setup_logger(log_file)
    df = pd.read_csv(input_csv)

    # 1. Detection
    df, det_issues = detect_issues(df)
    logger.info("Detection Agent found %d issues", len(det_issues))
    for idx, field, detail in det_issues:
        logger.info(f"  Issue at row {idx}: {field} → {detail}")

    # 2. Correction
    df, corr_logs = correct_data(df, det_issues)
    logger.info("Correction Agent applied fixes:")
    for msg in corr_logs:
        logger.info("  " + msg)

    # 3. Enrichment
    df, enr_logs = enrich_data(df)
    logger.info("Enrichment Agent did:")
    for msg in enr_logs:
        logger.info("  " + msg)

    # Save final
    df.to_csv(output_csv, index=False)
    logger.info(f"Cleaned data written to {output_csv}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Mini Agent-Based Data Fixing")
    p.add_argument("--input",  "-i", required=True, help="Input CSV path")
    p.add_argument("--output", "-o", required=True, help="Cleaned CSV path")
    p.add_argument("--log",    "-l", required=True, help="Agent log file")
    args = p.parse_args()
    run_pipeline(args.input, args.output, args.log)
