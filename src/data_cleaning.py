import pandas as pd
import os

# ================================
# FILE PATHS
# ================================
input_path = os.path.join("data", "raw", "poll_data.csv")
output_path = os.path.join("data", "processed")
os.makedirs(output_path, exist_ok=True)

# ================================
# LOAD DATA
# ================================
df = pd.read_csv(input_path)

print("🔍 Original Data Preview:")
print(df.head())

print("\n📊 Original Data Info:")
print(df.info())

# ================================
# REMOVE DUPLICATES
# ================================
initial_rows = len(df)
df = df.drop_duplicates()
print(f"\n🧹 Removed {initial_rows - len(df)} duplicate rows")

# ================================
# HANDLE MISSING VALUES
# ================================
print("\n❓ Missing Values Before:")
print(df.isnull().sum())

# Drop rows with critical missing values
df = df.dropna(subset=["Primary_Tech_Stack", "Satisfaction_Score"])

# Fill non-critical missing values
df["Feedback"] = df["Feedback"].fillna("No feedback provided")

print("\n❓ Missing Values After:")
print(df.isnull().sum())

# ================================
# STANDARDIZE TEXT DATA
# ================================
df["Primary_Tech_Stack"] = df["Primary_Tech_Stack"].str.strip().str.title()
df["Region"] = df["Region"].str.strip().str.title()
df["Work_Setup_Preference"] = df["Work_Setup_Preference"].str.strip().str.title()

# ================================
# CONVERT DATA TYPES
# ================================
df["Satisfaction_Score"] = pd.to_numeric(df["Satisfaction_Score"], errors="coerce")
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

# ================================
# CREATE NEW FEATURES
# ================================
df["Date"] = df["Timestamp"].dt.date
df["Feedback_Length"] = df["Feedback"].astype(str).apply(len)

# ================================
# FINAL CHECK
# ================================
print("\n📊 Cleaned Data Info:")
print(df.info())

print("\n🔍 Cleaned Data Preview:")
print(df.head())

# ================================
# SAVE CLEANED DATA
# ================================
cleaned_file = os.path.join(output_path, "cleaned_poll_data.csv")
df.to_csv(cleaned_file, index=False)

print(f"\n✅ Cleaned dataset saved at: {cleaned_file}")