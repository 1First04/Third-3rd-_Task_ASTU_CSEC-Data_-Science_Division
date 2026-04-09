# Import Basic Library
import pandas as pd
import matplotlib.pyplot as plt

DST=pd.read_csv(r"C:\Users\hp\Desktop\dataset-2.csv")
# Show the whole the data set
DST

DST.head()

DST.info()

DST.describe()
#@@@@@@@@@@@@@@@@@@@@@@
# Step 2DAta Cleaning
#@@@@@@@@@@@@@@@@@@@@@
# Keep original copy 

df_clean = DST.copy()
print("Shape before cleaning:", df_clean.shape)
print(df_clean.isnull().sum())
#@@@@@@@@@@@@@@@@@@@@@@@@
# Handle Missing Values
#@@@@@@@@@@@@@@@@@@@@@@@@
# --- Age → median
age_median = df_clean["Age"].median()
df_clean["Age"] = df_clean["Age"].fillna(age_median)

# --- Embarked → mode
embarked_mode = df_clean["Embarked"].mode()[0]
df_clean["Embarked"] = df_clean["Embarked"].fillna(embarked_mode)

# --- Cabin → drop(too many missing / high cardinality)
if "Cabin" in df_clean.columns:
    df_clean = df_clean.drop(columns=["Cabin"])

# Remove Duplicates
df_clean = df_clean.drop_duplicates(keep="first")
#@@@@@@@@@@@@@@@@@@@@@@@@
#  Validation Checks
#@@@@@@@@@@@@@@@@@@@@@@@@
print("\nAfter Cleaning:")
print("Shape after cleaning:", df_clean.shape)
print(df_clean.isnull().sum())

#Convert categorical columns (memory + performance)
categorical_cols = ["Sex", "Embarked", "Pclass"] if set(["Sex","Embarked","Pclass"]).issubset(df_clean.columns) else []

for col in categorical_cols:
    df_clean[col] = df_clean[col].astype("category")
 
#save Clean Dataset
df_clean.to_csv("cleaned_dataset.csv", index=False)

print("\n Data cleaning completed successfully.")

# Step 3: Data Analysis
survival_by_gender = (
    df_clean
    .groupby("Sex")["Survived"]
    .mean()
    .sort_values(ascending=False)
)

print("Survival Rate by Gender:\n", survival_by_gender)

survival_by_class = (
    df_clean
    .groupby("Pclass")["Survived"]
    .mean()
    .sort_index()
)

print("\nSurvival Rate by Class:\n", survival_by_class)

#Average age per class

avg_age_per_class = (
    df_clean
    .groupby("Pclass")["Age"]
    .mean()
)

print("\nAverage Age per Class:\n", avg_age_per_class)

# Survival rate by age group

bins = [0, 12, 18, 35, 60, 100]
labels = ["Child", "Teen", "Young Adult", "Adult", "Senior"]

df_clean["Age_Group"] = pd.cut(df_clean["Age"], bins=bins, labels=labels)
survival_by_age_group = (
    df_clean
    .groupby("Age_Group")["Survived"]
    .mean()
    .sort_values(ascending=True)
)

print("\nSurvival Rate by Age Group:\n", survival_by_age_group)

#Step 4: Filtering

#Female passengers who survived
female_survivors = df_clean[
    (df_clean["Sex"] == "female") &
    (df_clean["Survived"] == 1)
]

print(female_survivors.head())

#Children who survived
children_survivors = df_clean[
    (df_clean["Age"] < 12) &
    (df_clean["Survived"] == 1)
]

print(children_survivors.head())

#Passengers in 1st class with high survival probability
first_class_survival_rate = (
    df_clean[df_clean["Pclass"] == 1]["Survived"].mean()
)

print("1st Class Survival Rate:", first_class_survival_rate)
