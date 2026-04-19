import pandas as pd
import os

# ================================
# LOAD CLEANED DATA
# ================================
file_path = os.path.join("data", "processed", "cleaned_poll_data.csv")
df = pd.read_csv(file_path)

print("🔍 Data Preview:")
print(df.head())

# ================================
# BASIC DATA OVERVIEW
# ================================
print("\n📊 Dataset Shape:", df.shape)
print("\n📊 Columns:", df.columns.tolist())

# ================================
# KPI METRICS
# ================================
total_responses = len(df)
avg_satisfaction = df["Satisfaction_Score"].mean()

top_tech = df["Primary_Tech_Stack"].value_counts().idxmax()
top_tech_count = df["Primary_Tech_Stack"].value_counts().max()

print("\n📌 KEY METRICS:")
print(f"Total Responses: {total_responses}")
print(f"Average Satisfaction: {avg_satisfaction:.2f}")
print(f"Top Technology: {top_tech} ({top_tech_count} votes)")

# ================================
# PERCENTAGE DISTRIBUTION
# ================================
tech_distribution = df["Primary_Tech_Stack"].value_counts(normalize=True) * 100

print("\n📊 Tech Stack Distribution (%):")
print(tech_distribution)

# ================================
# REGION-WISE ANALYSIS
# ================================
region_analysis = df.groupby("Region")["Satisfaction_Score"].mean().sort_values(ascending=False)

print("\n🌍 Region-wise Average Satisfaction:")
print(region_analysis)

# ================================
# AGE GROUP ANALYSIS
# ================================
age_analysis = df.groupby("Age_Group")["Satisfaction_Score"].mean().sort_values(ascending=False)

print("\n🎂 Age Group Satisfaction:")
print(age_analysis)

# ================================
# WORK SETUP ANALYSIS
# ================================
work_analysis = df.groupby("Work_Setup_Preference")["Satisfaction_Score"].mean()

print("\n🏠 Work Setup Satisfaction:")
print(work_analysis)

# ================================
# TREND ANALYSIS (OVER TIME)
# ================================
df["Date"] = pd.to_datetime(df["Date"])
daily_trend = df.groupby("Date").size()

print("\n📈 Daily Response Trend:")
print(daily_trend.head())

# ================================
# SAVE SUMMARY (OPTIONAL)
# ================================
summary_path = os.path.join("outputs", "reports", "analysis_summary.txt")

with open(summary_path, "w") as f:
    f.write("=== POLL ANALYSIS SUMMARY ===\n\n")
    f.write(f"Total Responses: {total_responses}\n")
    f.write(f"Average Satisfaction: {avg_satisfaction:.2f}\n")
    f.write(f"Top Technology: {top_tech}\n\n")

    f.write("Tech Distribution (%):\n")
    f.write(str(tech_distribution) + "\n\n")

    f.write("Region Satisfaction:\n")
    f.write(str(region_analysis) + "\n\n")

print(f"\n✅ Analysis summary saved at: {summary_path}")