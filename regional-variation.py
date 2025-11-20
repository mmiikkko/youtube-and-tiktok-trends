#--FOR SOP3--
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv")

# Trend Behavior Differences by Region (Velocity & Duration)
regional_trend_stats = df.groupby(["platform", "country"]).agg({
    "trend_duration_days": "mean",
    "engagement_velocity": "mean",
    "views": "mean",
    "engagement_rate": "mean",
    "avg_watch_time_sec": "mean"
}).reset_index()

print("\n=== REGIONAL TREND BEHAVIOR (Velocity & Duration) ===")
print(regional_trend_stats)

# --- Plot: Engagement Velocity by Region ---
plt.figure(figsize=(12,6))
sns.barplot(data=regional_trend_stats, x="country", y="engagement_velocity", hue="platform")
plt.title("Engagement Velocity by Country and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Plot: Trend Duration by Region ---
plt.figure(figsize=(12,6))
sns.barplot(data=regional_trend_stats, x="country", y="trend_duration_days", hue="platform")
plt.title("Trend Duration Across Regions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Regional Engagement Patterns (how algorithms spread trends)

regional_engagement_stats = df.groupby(["platform", "country"]).agg({
    "views": ["mean", "median"],
    "likes": "mean",
    "comments": "mean",
    "shares": "mean",
    "engagement_rate": "mean",
    "completion_rate": "mean"
}).reset_index()

print("\n=== REGIONAL ENGAGEMENT PATTERNS ===")
print(regional_engagement_stats)


# --- Plot: Engagement Rate Across Regions ---
plt.figure(figsize=(12,6))
sns.barplot(data=regional_trend_stats, x="country", y="engagement_rate", hue="platform")
plt.title("Engagement Rate by Country and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Regional Language Influence (platform–region–language)
language_region_stats = df.groupby(["platform", "country", "language"]).agg({
    "views": "mean",
    "engagement_rate": "mean",
    "trend_duration_days": "mean",
    "engagement_velocity": "mean",
}).reset_index()

print("\n=== LANGUAGE × REGION × PLATFORM SUMMARY ===")
print(language_region_stats)

# --- Plot: Language Engagement by Platform ---
plt.figure(figsize=(14,6))
sns.barplot(data=language_region_stats, x="language", y="engagement_rate", hue="platform")
plt.title("Engagement Rate by Language and Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Posting Behavior Regional Differences
plt.figure(figsize=(14,6))
sns.boxplot(data=df, x="country", y="upload_hour", hue="platform")
plt.title("Regional Upload Time Patterns by Platform")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Category popularity across regions
plt.figure(figsize=(14,6))
sns.countplot(data=df, x="country", hue="category")
plt.title("Category Preferences by Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
