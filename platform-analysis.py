#--FOR SOP1--
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/Users/jaece/dataset-files/cleaned_youtube_tiktok_trends.csv")


# CONTENT CHARACTERISTICS
content_stats = df.groupby('platform').agg({
    'duration_sec': ['mean', 'median'],
    'views': ['mean', 'median'],
    'likes': ['mean', 'median'],
    'comments': ['mean', 'median'],
    'shares': ['mean', 'median'],
    'saves': ['mean', 'median'],
    'engagement_rate': ['mean', 'median'],
    'avg_watch_time_sec': ['mean', 'median'],
    'completion_rate': ['mean', 'median'],
    'hashtag': lambda x: x.nunique(),
    'music_track': lambda x: x.nunique(),
    'title_keywords': lambda x: x.nunique(),
}).reset_index()

print("\n=== CONTENT & ENGAGEMENT CHARACTERISTICS BY PLATFORM ===")
print(content_stats)


# CREATOR ACTIVITY (creator_tier)
if 'creator_tier' in df.columns:
    creator_stats = df.groupby(['platform', 'creator_tier']).agg({
        'views': ['mean', 'median'],
        'likes': ['mean', 'median'],
        'comments': ['mean', 'median'],
        'shares': ['mean', 'median'],
        'engagement_rate': ['mean', 'median'],
        'creator_tier': 'count'
    }).rename(columns={'creator_tier': 'num_videos'})

    print("\n=== CREATOR ACTIVITY BY PLATFORM AND TIER ===")
    print(creator_stats)



# PLATFORM DYNAMICS: Engagement & Duration

plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='engagement_rate')
plt.title("Average Engagement Rate by Platform")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='duration_sec')
plt.title("Average Video Duration by Platform")
plt.show()


# TREND BEHAVIOR (velocity, duration)
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='engagement_velocity')
plt.title("Engagement Velocity by Platform")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='platform', y='trend_duration_days')
plt.title("Trend Duration Across Platforms")
plt.show()

# CONTENT TYPES (sound, category)
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='platform', hue='sound_type')
plt.title("Sound Type Usage by Platform")
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, x='platform', hue='category')
plt.title("Category Distribution by Platform")
plt.show()

# CREATOR TIER DISTRIBUTION
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='platform', hue='creator_tier')
plt.title("Creator Tier Distribution by Platform")
plt.show()

# VIEWER BEHAVIOR (watch time, completion)
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='avg_watch_time_sec')
plt.title("Average Watch Time by Platform")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=df, x='platform', y='completion_rate')
plt.title("Completion Rate by Platform")
plt.show()

# POSTING PATTERNS (hour, day)
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='platform', y='upload_hour')
plt.title("Upload Hour Distribution by Platform")
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, x='platform', hue='publish_dayofweek')
plt.title("Posting Day of Week by Platform")
plt.show()
