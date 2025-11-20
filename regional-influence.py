#--FOR SOP2--
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv(r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv")

# ------------------------------------------------------------
# 1. ENGAGEMENT BY LANGUAGE
# ------------------------------------------------------------

language_stats = df.groupby(["platform", "language"]).agg({
    "views": "mean",
    "likes": "mean",
    "comments": "mean",
    "shares": "mean",
    "engagement_rate": "mean",
    "avg_watch_time_sec": "mean",
    "completion_rate": "mean",
}).reset_index()

print("\n=== ENGAGEMENT BY LANGUAGE & PLATFORM ===")
print(language_stats)

plt.figure(figsize=(12,6))
sns.barplot(data=language_stats, x="language", y="engagement_rate", hue="platform")
plt.title("Engagement Rate by Language and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 2. VIEWERSHIP BY REGION (COUNTRY)
# ------------------------------------------------------------

region_stats = df.groupby(["platform", "country"]).agg({
    "views": "mean",
    "likes": "mean",
    "comments": "mean",
    "shares": "mean",
    "engagement_rate": "mean",
    "trend_duration_days": "mean",
    "engagement_velocity": "mean",
}).reset_index()

print("\n=== REGIONAL VIEWERSHIP & ENGAGEMENT BY COUNTRY ===")
print(region_stats)

plt.figure(figsize=(12,6))
sns.barplot(data=region_stats, x="country", y="views", hue="platform")
plt.title("Average Views by Country and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 3. CATEGORY PREFERENCES BY REGION
# ------------------------------------------------------------

plt.figure(figsize=(12,6))
sns.countplot(data=df, x="country", hue="category")
plt.title("Category Distribution by Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 4. LANGUAGE vs WATCH-TIME + COMPLETION
# ------------------------------------------------------------

plt.figure(figsize=(10,6))
sns.barplot(data=df, x="language", y="avg_watch_time_sec", hue="platform")
plt.title("Watch Time by Language and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df, x="language", y="completion_rate", hue="platform")
plt.title("Completion Rate by Language and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 5. REGIONAL POSTING PATTERNS (Upload hour)
# ------------------------------------------------------------

plt.figure(figsize=(12,6))
sns.boxplot(data=df, x="country", y="upload_hour", hue="platform")
plt.title("Upload Hour Patterns by Country and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 6. SUMMARY TABLE (language + region combined)
# ------------------------------------------------------------

combined_stats = df.groupby(["platform", "language", "country"]).agg({
    "views": "mean",
    "likes": "mean",
    "comments": "mean",
    "engagement_rate": "mean",
    "avg_watch_time_sec": "mean",
    "trend_duration_days": "mean",
    "engagement_velocity": "mean",
}).reset_index()

print("\n=== LANGUAGE + REGION MULTIVARIATE SUMMARY ===")
print(combined_stats)
