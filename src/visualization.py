import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from wordcloud import WordCloud

# ================================
# LOAD CLEANED DATA
# ================================
file_path = os.path.join("data", "processed", "cleaned_poll_data.csv")
df = pd.read_csv(file_path)

# Ensure output directory exists
output_dir = os.path.join("outputs", "charts")
os.makedirs(output_dir, exist_ok=True)

# ================================
# 1. BAR CHART — TECH STACK
# ================================
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Primary_Tech_Stack", palette="Set2")
plt.title("Technology Preference Distribution")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(os.path.join(output_dir, "tech_bar_chart.png"))
plt.show()

# ================================
# 2. PIE CHART — TECH SHARE
# ================================
tech_counts = df["Primary_Tech_Stack"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(tech_counts, labels=tech_counts.index, autopct="%1.1f%%")
plt.title("Technology Share (%)")

plt.savefig(os.path.join(output_dir, "tech_pie_chart.png"))
plt.show()

# ================================
# 3. LINE CHART — TREND
# ================================
df["Date"] = pd.to_datetime(df["Date"])
daily = df.groupby("Date").size()

plt.figure(figsize=(10,5))
daily.plot(marker="o")
plt.title("Daily Response Trend")
plt.xlabel("Date")
plt.ylabel("Responses")
plt.grid()

plt.savefig(os.path.join(output_dir, "trend_line_chart.png"))
plt.show()

# ================================
# 4. BOX PLOT — SATISFACTION
# ================================
plt.figure(figsize=(7,5))
sns.boxplot(x="Primary_Tech_Stack", y="Satisfaction_Score", data=df)
plt.title("Satisfaction Distribution by Tech Stack")
plt.xticks(rotation=30)

plt.savefig(os.path.join(output_dir, "boxplot.png"))
plt.show()

# ================================
# 5. WORD CLOUD — FEEDBACK
# ================================
text = " ".join(df["Feedback"].astype(str))

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Feedback Word Cloud")

plt.savefig(os.path.join(output_dir, "wordcloud.png"))
plt.show()

print("✅ All charts generated and saved in outputs/charts/")