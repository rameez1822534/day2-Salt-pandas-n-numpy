import argparse
import pandas as pd
import re

# Define arguments
parser = argparse.ArgumentParser(description="Clean CSV column names from special characters.")
parser.add_argument('--input', required=True, help='Path to input CSV file')
parser.add_argument('--output', required=True, help='Path to save cleaned CSV')

# Parse arguments
args = parser.parse_args()

# Example usage with the arguments
print(f"Reading from: {args.input}")
print(f"Saving to: {args.input}")

# Read CSV
df = pd.read_csv(args.input)

# Clean column names by removing all non-alphanumeric characters (including underscores)
def clean_column_name(col):
    return re.sub(r'[^A-Za-z0-9]', '', col)

df.columns = [clean_column_name(col) for col in df.columns]

# Save cleaned CSV
df.to_csv(args.output, index=False)

print("Column names cleaned (all special characters and underscores removed) and file saved.")