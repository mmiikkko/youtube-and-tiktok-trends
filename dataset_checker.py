# ============================================
# ⚠️ DATA QUALITY CHECK — UNCLEANED DATASET
# For: youtube_shorts_tiktok_trends_2025.csv
# ============================================

import pandas as pd
import numpy as np

# 1️⃣ Load the uncleaned dataset
raw_path = r"C:/Users/jaece/dataset-files/youtube_shorts_tiktok_trends_2025.csv"
df = pd.read_csv(raw_path)

print("🔍 ANALYZING RAW / UNCLEANED DATASET...")
print(f"Loaded file: {raw_path}")
print(f"Total Rows: {len(df)}, Columns: {len(df.columns)}\n")

# 2️⃣ Check for missing values
missing = df.isnull().sum()
if missing.any():
    print("⚠️ Missing values detected in:")
    print(missing[missing > 0])
else:
    print("✅ No missing values found.\n")

# 3️⃣ Check for duplicate rows
duplicates = df.duplicated().sum()
if duplicates > 0:
    print(f"⚠️ {duplicates} duplicate rows detected.")
else:
    print("✅ No duplicate rows detected.\n")

# 4️⃣ Check for inconsistent text formatting
text_cols = df.select_dtypes(include=['object']).columns
text_issues = {}
for col in text_cols:
    # Leading/trailing spaces
    spaces = df[col][df[col].astype(str).str.strip() != df[col].astype(str)]
    # Mixed casing (e.g., "hello" vs "Hello")
    inconsistent_case = df[col][df[col].astype(str).str.contains(r'[A-Z]') &
                                 df[col].astype(str).str.contains(r'[a-z]')]
    # Multiple spaces between words
    multi_spaces = df[col][df[col].astype(str).str.contains(r'\s{2,}')]

    total_issues = len(spaces) + len(inconsistent_case) + len(multi_spaces)
    if total_issues > 0:
        text_issues[col] = total_issues

if text_issues:
    print("⚠️ Text inconsistencies found in:")
    for col, count in text_issues.items():
        print(f"   - {col}: {count} potential issues (spacing/casing/etc.)")
else:
    print("✅ No major text inconsistencies detected.\n")

# 5️⃣ Check data types for suspicious or mixed entries
print("📋 Column Data Types:")
print(df.dtypes)
print()
object_cols = df.columns[df.dtypes == 'object']
if len(object_cols) > 0:
    print(f"⚠️ {len(object_cols)} columns are 'object' type: {list(object_cols)}")
    print("   → Some may need conversion to numeric or datetime.\n")
else:
    print("✅ All columns are proper numeric or datetime types.\n")

# 6️⃣ Detect outliers in numeric columns
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
    print("⚠️ Potential outliers detected in:")
    for col, count in outlier_summary.items():
        print(f"   - {col}: {count} outlier values")
else:
    print("✅ No significant outliers detected.\n")

# 7️⃣ Summary
print("📊 RAW DATA VALIDATION SUMMARY")
print("-----------------------------")
print(f"Missing Values: {'❌ Found' if missing.any() else '✅ None'}")
print(f"Duplicates: {'❌ Found' if duplicates > 0 else '✅ None'}")
print(f"Text Issues: {'❌ Found' if text_issues else '✅ None'}")
print(f"Data Type Issues: {'❌ Found' if len(object_cols) > 0 else '✅ None'}")
print(f"Outliers: {'❌ Found' if outlier_summary else '✅ None'}")
print("-----------------------------")
print("Validation complete.\n")
