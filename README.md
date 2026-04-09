# Customer_Personality_Analysis
Task 1: Data Cleaning and Preprocessing
Customer Personality Analysis – Data Cleaning & Preprocessing

Objective:
The objective of this task is to clean and preprocess a raw dataset containing missing values, duplicate records, inconsistent formats, and incorrect data types using Python (Pandas).

Dataset Used:
Customer Personality Analysis Dataset (Kaggle)

Tools Used:
- Python
- Pandas Library
- GitHub

Steps Performed:
1. Loaded dataset using Pandas
2. Checked dataset structure using ".info()" and ".head()"
3. Identified missing values using ".isnull()"
4. Replaced missing values in income column using median value
5. Removed duplicate rows
6. Standardized column names (lowercase format)
7. Converted dt_customer column into datetime format
8. Corrected datatype of year_birth
9. Created new feature age
10. Standardized categorical text columns:
- education
- marital_status
11. Exported cleaned dataset

Output Files Included:
- Original dataset
- Python cleaning script

Result:
The dataset is now cleaned, structured, and ready for further analysis and machine learning tasks.
