import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv(r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv")


# -------------------- SOP 1: Platform Differences --------------------
print("\n📌 SOP 1: Platform Differences Analysis")

# Content characteristics
content_stats = df.groupby('platform').agg({
    'duration_sec': ['mean', 'median'],
    'hashtag': lambda x: x.nunique(),
    'music_track': lambda x: x.nunique(),
    'title_keywords': lambda x: x.nunique(),
    'views': 'mean',
    'likes': 'mean',
    'comments': 'mean',
    'shares': 'mean',
    'saves': 'mean',
    'engagement_rate': 'mean'
}).reset_index()
print("\nContent & engagement characteristics by platform:")
print(content_stats)

# Creator activity (if creator_tier exists)
if 'creator_tier' in df.columns:
    creator_stats = df.groupby(['platform', 'creator_tier']).agg({
        'views': 'mean',
        'likes': 'mean',
        'comments': 'mean',
        'shares': 'mean'
    }).reset_index()
    print("\nCreator activity by platform and tier:")
    print(creator_stats)

# Visualizations
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='engagement_rate')
plt.title("Average Engagement Rate by Platform")
plt.ylabel("Engagement Rate")
plt.xlabel("Platform")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='duration_sec')
plt.title("Average Video Duration by Platform")
plt.ylabel("Duration (sec)")
plt.xlabel("Platform")
plt.show()

# -------------------- SOP 2: Language & Regional Influence --------------------
print("\n📌 SOP 2: Language & Regional Influence")

# Engagement by language
lang_stats = df.groupby('language').agg({
    'views': 'mean',
    'engagement_rate': 'mean',
    'likes': 'mean',
    'comments': 'mean',
    'shares': 'mean'
}).sort_values('views', ascending=False).reset_index()
print("\nAverage engagement metrics by language:")
print(lang_stats.head(10))

plt.figure(figsize=(12,6))
sns.barplot(data=lang_stats.head(10), x='language', y='engagement_rate')
plt.title("Top 10 Languages by Engagement Rate")
plt.ylabel("Engagement Rate")
plt.xlabel("Language")
plt.xticks(rotation=45)
plt.show()

# Engagement by country
country_stats = df.groupby('country').agg({
    'views': 'mean',
    'engagement_rate': 'mean',
    'likes': 'mean',
    'comments': 'mean',
    'shares': 'mean'
}).sort_values('views', ascending=False).reset_index()
print("\nAverage engagement metrics by country:")
print(country_stats.head(10))

plt.figure(figsize=(12,6))
sns.barplot(data=country_stats.head(10), x='country', y='engagement_rate')
plt.title("Top 10 Countries by Engagement Rate")
plt.ylabel("Engagement Rate")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.show()

# -------------------- SOP 3: Algorithmic Contribution to Regional Variations --------------------
print("\n📌 SOP 3: Algorithmic Influence on Regional Trends")

# Trend duration and engagement velocity by platform & country
algo_stats = df.groupby(['platform', 'country']).agg({
    'trend_duration_days': 'mean',
    'engagement_velocity': 'mean',
    'views': 'mean',
    'engagement_rate': 'mean'
}).sort_values(['platform', 'trend_duration_days'], ascending=False).reset_index()
print("\nTrend duration & engagement velocity by platform and country:")
print(algo_stats.head(10))

# Visualize trend duration by platform
plt.figure(figsize=(12,6))
sns.barplot(data=algo_stats.head(10), x='country', y='trend_duration_days', hue='platform')
plt.title("Top 10 Countries: Average Trend Duration by Platform")
plt.ylabel("Trend Duration (days)")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.show()

# Visualize engagement velocity by platform
plt.figure(figsize=(12,6))
sns.barplot(data=algo_stats.head(10), x='country', y='engagement_velocity', hue='platform')
plt.title("Top 10 Countries: Engagement Velocity by Platform")
plt.ylabel("Engagement Velocity")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.show()

print("\n✅ All SOP analyses completed successfully!")
