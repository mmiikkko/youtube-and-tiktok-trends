import pandas as pd
import os

# ============================================
# 📊 DATASET EVALUATION SCRIPT (No Modification)
# Compares cleaned vs uncleaned datasets
# ============================================

# 🔹 File paths (update if needed)
uncleaned_path = r"C:/Users/jaece/dataset-files/youtube_shorts_tiktok_trends_2025.csv"
cleaned_path = r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv"

# 1️⃣ Load both datasets safely
try:
    df_raw = pd.read_csv(uncleaned_path, encoding='utf-8', sep=',', engine='python', on_bad_lines='skip')
    df_clean = pd.read_csv(cleaned_path, encoding='utf-8', sep=',', engine='python', on_bad_lines='skip')
    print("✅ Both datasets loaded successfully!\n")
except Exception as e:
    print(f"❌ Error loading datasets: {e}")
    exit()

# 2️⃣ Basic info
print("========== RAW DATA OVERVIEW ==========")
print(df_raw.info())
print("\nNumber of rows:", len(df_raw))
print("Number of columns:", len(df_raw.columns))
print("Columns:", list(df_raw.columns))
print("\n=======================================")

print("\n========== CLEANED DATA OVERVIEW ==========")
print(df_clean.info())
print("\nNumber of rows:", len(df_clean))
print("Number of columns:", len(df_clean.columns))
print("Columns:", list(df_clean.columns))
print("\n===========================================")

# 3️⃣ Compare columns
raw_cols = set(df_raw.columns)
clean_cols = set(df_clean.columns)

removed_cols = raw_cols - clean_cols
new_cols = clean_cols - raw_cols
common_cols = raw_cols & clean_cols

print("\n📂 COLUMN COMPARISON:")
print(f"- Columns removed in cleaned data: {len(removed_cols)} → {list(removed_cols)}")
print(f"- New columns added in cleaned data: {len(new_cols)} → {list(new_cols)}")
print(f"- Common columns retained: {len(common_cols)}")

# 4️⃣ Compare shape (rows)
print("\n📏 ROW COMPARISON:")
print(f"- Rows in raw dataset: {len(df_raw)}")
print(f"- Rows in cleaned dataset: {len(df_clean)}")
row_diff = len(df_raw) - len(df_clean)
if row_diff > 0:
    print(f"⚠️ {row_diff} rows were removed (likely duplicates or invalid entries).")
elif row_diff < 0:
    print(f"⚠️ {abs(row_diff)} new rows were added (unexpected — check cleaning script).")
else:
    print("✅ Row count unchanged.")

# 5️⃣ Missing values check
print("\n🧩 MISSING VALUES (Top 10 Columns with Missing Data in RAW):")
print(df_raw.isnull().sum().sort_values(ascending=False).head(10))

print("\n🧩 MISSING VALUES (Top 10 Columns with Missing Data in CLEANED):")
print(df_clean.isnull().sum().sort_values(ascending=False).head(10))

# 6️⃣ Duplicate check
raw_dupes = df_raw.duplicated().sum()
clean_dupes = df_clean.duplicated().sum()

print("\n🔁 DUPLICATE CHECK:")
print(f"- Raw dataset duplicates: {raw_dupes}")
print(f"- Cleaned dataset duplicates: {clean_dupes}")

# 7️⃣ Data type consistency check
print("\n📘 DATA TYPE COMPARISON (for common columns):")
dtype_diff = {}
for col in common_cols:
    if df_raw[col].dtype != df_clean[col].dtype:
        dtype_diff[col] = (df_raw[col].dtype, df_clean[col].dtype)
if dtype_diff:
    print("⚠️ Columns with changed data types:")
    for col, types in dtype_diff.items():
        print(f"  - {col}: {types[0]} → {types[1]}")
else:
    print("✅ All common columns have consistent data types.")

# 8️⃣ Sample comparison preview
print("\n🔍 SAMPLE ROWS COMPARISON (FIRST 3 ROWS):")
print("\nRAW:")
print(df_raw.head(3))
print("\nCLEANED:")
print(df_clean.head(3))

print("\n✅ Evaluation completed! (No modifications made to any dataset)")
