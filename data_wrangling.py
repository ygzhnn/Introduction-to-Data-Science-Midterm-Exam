# Import necessary libraries
import pandas as pd
import numpy as np

# --- Step 0: Create the Dataset ---
initial_data = {
    'Student_ID': [1001, 1002, 1003, 1001, 1004, 1005],
    'Name': ['Alice Johnson', 'Bob Williams', 'Charlie Brown', 'Alice Johnson', 'Eve Davis', 'David Lee'],
    'Course_Grade': [88.5, 92.0, np.nan, 88.5, 75.2, 95.8],
    'Major': ['CS', 'Math', 'Physics', 'CS', 'biology', np.nan],
    'Enrollment_Status': ['Complete', 'In Progress', 'Complete', 'Complete', 'In Progress', 'Complete'],
    'Date_Enrolled': ['2023-08-25', '2023-08-27', '2023-09-01', '2023-08-25', '2023-09-05', '2023-09-10']
}
student_df = pd.DataFrame(initial_data)
print("="*25, "INITIAL DATA", "="*25)
print(student_df.to_string())
print("\\n")


# --- Step 1: Duplicate Handling ---
student_df.drop_duplicates(inplace=True)
print("="*20, "STEP 1: DUPLICATES REMOVED", "="*20)
print(student_df.to_string())
print("\\n")


# --- Step 2: Standardization ---
student_df['Major'] = student_df['Major'].str.lower().str.strip()
print("="*18, "STEP 2: 'MAJOR' STANDARDIZED", "="*18)
print(student_df.to_string())
print("\\n")


# --- Step 3: Missing Data Imputation ---
median_course_grade = student_df['Course_Grade'].median()
student_df['Course_Grade'] = student_df['Course_Grade'].fillna(median_course_grade)
print("="*15, "STEP 3: MISSING GRADES FILLED", "="*16)
print(f"Note: Missing grades were filled with the median value of {median_course_grade:.2f}")
print(student_df.to_string())
print("\\n")


# --- Step 4: Casting Data Types ---
student_df['Date_Enrolled'] = pd.to_datetime(student_df['Date_Enrolled'])
print("="*15, "STEP 4: 'DATE_ENROLLED' CAST", "="*16)
print("Note: 'Date_Enrolled' column converted to datetime objects.")
print(student_df.to_string())
print("\\nColumn Data Types:")
print(student_df.dtypes)
print("\\n")


# --- Step 5: Final Check ---
final_average_grade = student_df['Course_Grade'].mean()
print("="*24, "FINAL RESULT", "="*24)
print("Final Cleaned DataFrame:")
print(student_df.to_string())
print("\\n" + "-"*60)
print(f"  Final Mean of 'Course_Grade': {final_average_grade:.2f}")
print("-"*60)
