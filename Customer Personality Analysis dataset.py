import pandas as pd
import numpy as np

df = pd.read_csv("customer_segmentation.csv", sep=None, engine="python")

print("Dataset Shape:",df.shape)
print(df.head())
print(df.info())
print("Missing Values:\n",df.isnull().sum())

df.columns = df.columns.str.strip().str.lower()

print("Columns detected:", df.columns)

df["income"] = df["income"].fillna(df["income"].mode())

print("Duplicate Rows:",df.duplicated().sum())
df = df.drop_duplicates()

df.columns = df.columns.str.lower().str.replace(" ", "_")
print("Updated Column Names:\n", df.columns)
df["dt_customer"] = pd.to_datetime(df["dt_customer"], errors="coerce")

df["year_birth"] = df["year_birth"].astype(int)

df["age"] = 2025 - df["year_birth"]
print(df["age"].describe())

df["education"] = df["education"].str.lower()
df["marital_status"] = df["marital_status"].str.lower()


df.to_csv("cleaned_customer_personality_analysis.csv", index=False)

print("Cleaning completed successfully!")
