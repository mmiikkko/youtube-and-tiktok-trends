import pandas as pd
import numpy as np

# Load the cleaned dataset
cleaned_path = r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv"
df = pd.read_csv(cleaned_path)

print("🔍 VALIDATING CLEANED DATASET...")
print(f"Loaded file: {cleaned_path}")
print(f"Total Rows: {len(df)}, Columns: {len(df.columns)}\n")

# Show all attribute names in paragraph format
attributes = ", ".join(df.columns)
print(f"📌 Dataset Attributes:\n{attributes}\n")

# Check for missing values
missing = df.isnull().sum()
if missing.any():
    print("⚠️ Missing values still found in:")
    print(missing[missing > 0])
else:
    print("✅ No missing values detected.\n")

# Check for duplicate rows
duplicates = df.duplicated().sum()
if duplicates > 0:
    print(f"⚠️ {duplicates} duplicate rows still exist.")
else:
    print("✅ No duplicate rows detected.\n")

# Check for inconsistent text formatting
# (like mixed case or leading/trailing spaces)
text_cols = df.select_dtypes(include=['object']).columns
text_issues = {}
for col in text_cols:
    # Check for leading/trailing spaces or non-title case
    inconsistent = df[col][
        (df[col].str.strip() != df[col]) |
        (~df[col].str.match(r'^[A-Z][a-zA-Z0-9\s]*$', na=False))
    ]
    if not inconsistent.empty:
        text_issues[col] = len(inconsistent)

if text_issues:
    print("⚠️ Text inconsistencies found in:")
    for col, count in text_issues.items():
        print(f"   - {col}: {count} potential issues")
else:
    print("✅ No text inconsistencies detected.\n")

# Check for invalid or unexpected data types
print("📋 Column Data Types:")
print(df.dtypes)
print()
invalid_types = df.columns[df.dtypes == 'object']
if len(invalid_types) > 0:
    print(f"⚠️ Columns still stored as 'object' type: {list(invalid_types)}")
    print("   → Consider converting to numeric or datetime if appropriate.\n")
else:
    print("✅ All columns have valid data types.\n")

# Check for outliers in numeric columns
num_cols = df.select_dtypes(include=[np.number]).columns
outlier_summary = {}
for col in num_cols:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    if not outliers.empty:
        outlier_summary[col] = len(outliers)

if outlier_summary:
    print("⚠️ Potential outliers found in numeric columns:")
    for col, count in outlier_summary.items():
        print(f"   - {col}: {count} outlier values")
else:
    print("✅ No significant outliers detected.\n")

print("🎯 DATA VALIDATION SUMMARY")
print("-----------------------------")
print(f"Missing Values: {'❌  Found' if missing.any() else '✅ None'}")
print(f"Duplicates: {'❌ Found' if duplicates > 0 else '✅ None'}")
print(f"Text Issues: {'❌ Found' if text_issues else '✅ None'}")
print(f"Data Type Issues: {'❌ Found' if len(invalid_types) > 0 else '✅ None'}")
print(f"Outliers: {'❌ Found' if outlier_summary else '✅ None'}")
print("-----------------------------")
print("Validation complete.\n")
