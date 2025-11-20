import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv")

# Content characteristics (e.g., duration, hashtags, sounds)
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

# Average engagement rate by platform
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='engagement_rate')
plt.title("Average Engagement Rate by Platform")
plt.ylabel("Engagement Rate")
plt.xlabel("Platform")
plt.show()

# Average video duration by platform
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='duration_sec')
plt.title("Average Video Duration by Platform")
plt.ylabel("Duration (sec)")
plt.xlabel("Platform")
plt.show()