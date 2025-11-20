import pandas as pd
import os
file_path = r"C:/Users/jaece/dataset-files/youtube_shorts_tiktok_trends_2025.csv"

try:
    df = pd.read_csv(
        file_path,
        encoding='utf-8',
        sep=',',
        quotechar='"',
        escapechar='\\',
        engine='python',
        on_bad_lines='skip'
    )
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

print("\n🔍 RAW DATA OVERVIEW")
print(df.info())
print("\nFirst 5 rows of raw data:")
print(df.head())

# Create copy for cleaning
df_copy = df.copy()

#⃣Remove duplicate rows
initial_rows = len(df_copy)
df_copy.drop_duplicates(inplace=True)
removed = initial_rows - len(df_copy)
print(f"\n✅ Removed {removed} duplicate rows.")

# Clean text columns (trim, normalize, remove junk)
text_cols = df_copy.select_dtypes(include=['object']).columns
for col in text_cols:
    df_copy[col] = (
        df_copy[col]
        .astype(str)
        .str.strip()
        .str.replace(r'\s+', ' ', regex=True)
        .str.replace(r'[^A-Za-z0-9#@_\-\s]', '', regex=True)
        .str.title()
    )
print("\n🧽 Cleaned text columns for consistency.")

# Handle missing values
for col in df_copy.columns:
    if df_copy[col].dtype == 'object':
        df_copy[col] = df_copy[col].replace(['', 'Nan', 'NaN'], 'Unknown')
        df_copy[col] = df_copy[col].fillna('Unknown')
    else:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
print("\n🩹 Missing values handled successfully.")

# Keep only the most relevant columns for analysis
important_columns = [
    "platform", "country", "region", "language", "category", "hashtag", "title_keywords",
    "sound_type", "music_track", "duration_sec", "views", "likes", "comments", "shares",
    "saves", "engagement_rate", "trend_duration_days", "engagement_velocity",
    "upload_hour", "publish_dayofweek", "event_season", "device_type", "creator_tier",
    "engagement_total", "like_rate", "comment_ratio", "share_rate", "completion_rate",
    "avg_watch_time_sec"
]

existing_cols = [c for c in important_columns if c in df_copy.columns]
df_copy = df_copy[existing_cols]
print(f"\nFiltered to {len(existing_cols)} important analytical columns.")

# Standardize column names
df_copy.columns = [c.strip().lower().replace(' ', '_') for c in df_copy.columns]
print("\n🏷Standardized column names.")

# Save cleaned dataset
cleaned_path = r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv"
df_copy.to_csv(cleaned_path, index=False, encoding='utf-8-sig')

print(f"\nCleaned & filtered dataset saved as: {cleaned_path}")

# Summary comparison
print("\n📊 Comparison Summary:")
print(f"Rows before: {len(df)}, after cleaning: {len(df_copy)}")
print(f"Columns before: {len(df.columns)}, after: {len(df_copy.columns)}")
print(f"\nColumns now: {list(df_copy.columns)}")

print("\n✅ Data Cleaning Completed Successfully!")

# Preview cleaned data
print("\nPreview of cleaned data:")
print(df_copy.head())
