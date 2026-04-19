import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# ================================
# CREATE OUTPUT DIRECTORY
# ================================
output_dir = os.path.join("data", "raw")
os.makedirs(output_dir, exist_ok=True)

# ================================
# CONFIGURATION
# ================================
NUM_RECORDS = 800

regions = ["Asia-Pacific", "Europe", "North America", "Middle East", "Africa"]
age_groups = ["18-24", "25-34", "35-44", "45+"]
genders = ["Male", "Female"]
occupations = ["Student", "Software Engineer", "Data Analyst", "Manager", "Researcher"]

tech_stacks = ["Python", "JavaScript", "Java", "C++", "R"]
work_setups = ["Remote", "Hybrid", "On-site"]

# Feedback categories
positive_feedback = [
    "Very useful and easy to use",
    "Great experience",
    "Loved the flexibility",
    "Highly efficient tool",
    "Very satisfied with the results"
]

neutral_feedback = [
    "It's okay",
    "Average experience",
    "Can be improved",
    "Nothing special",
    "Works fine"
]

negative_feedback = [
    "Needs improvement",
    "Not very user friendly",
    "Had some issues",
    "Poor experience",
    "Not satisfied"
]

# ================================
# RANDOM DATE FUNCTION
# ================================
def generate_random_timestamp(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 4, 30)

# ================================
# DATA GENERATION
# ================================
data = []

for i in range(NUM_RECORDS):
    respondent_id = f"R{i+1:04d}"

    region = random.choice(regions)
    age = random.choices(age_groups, weights=[40, 30, 20, 10])[0]
    gender = random.choice(genders)
    occupation = random.choice(occupations)

    tech = random.choices(tech_stacks, weights=[40, 25, 15, 10, 10])[0]
    setup = random.choices(work_setups, weights=[45, 35, 20])[0]

    # ================================
    # REALISTIC SATISFACTION LOGIC
    # ================================
    if tech == "Python":
        satisfaction = random.randint(4, 5)
        feedback = random.choice(positive_feedback)

    elif tech == "JavaScript":
        satisfaction = random.randint(3, 5)
        feedback = random.choice(positive_feedback + neutral_feedback)

    elif tech == "Java":
        satisfaction = random.randint(2, 4)
        feedback = random.choice(neutral_feedback)

    else:
        satisfaction = random.randint(1, 3)
        feedback = random.choice(negative_feedback + neutral_feedback)

    timestamp = generate_random_timestamp(start_date, end_date)

    data.append([
        respondent_id,
        timestamp,
        region,
        age,
        gender,
        occupation,
        tech,
        setup,
        satisfaction,
        feedback
    ])

# ================================
# CREATE DATAFRAME
# ================================
df = pd.DataFrame(data, columns=[
    "Respondent_ID",
    "Timestamp",
    "Region",
    "Age_Group",
    "Gender",
    "Occupation",
    "Primary_Tech_Stack",
    "Work_Setup_Preference",
    "Satisfaction_Score",
    "Feedback"
])

# ================================
# SAVE DATASET
# ================================
file_path = os.path.join(output_dir, "poll_data.csv")
df.to_csv(file_path, index=False)

# ================================
# OUTPUT
# ================================
print("✅ Dataset generated successfully!")
print(f"📁 File saved at: {file_path}")
print("\n🔍 Preview:")
print(df.head())