
#%%
from enum import unique

import pandas as pd
import matplotlib.pyplot as plt

# %%
input_csv = input("Enter the absolute file path for the csv")

# %%
data = pd.read_csv(input_csv, index_col='student_id')
data.head()

# %%
# Explore columns and it's data types
data.columns

# %%
data.dtypes
# %%

# which columns are discrete
data.describe()
# %%
data['gender'].unique()
# %%
data['parental_education'].unique()
# %%
sum([job == 'Yes' for job in data['part_time_job']])

# %%
sum([job == 'No' for job in data['part_time_job']])
# %%
sum([act == 'Yes' for act in data['extracurricular_activities']])
# %%
sum([act == 'No' for act in data['extracurricular_activities']])
# %%
sum([edu for edu in data['parental_education']])
# %%
data['parental_education'].value_counts(normalize=True)
# %%
data['parental_education'].value_counts(normalize=True).map(lambda x: f"{x: .1%}")
# %%
plt.hist(data['final_exam_score'])
plt.title('Final Exam Score')
plt.xlabel('Score')
plt.ylabel('Frequency (# of students)')
# %%
plt.hist(data['study_time_hours'])
plt.xlabel('Study Time (hours)')
plt.ylabel('Frequency (# of students)')
# %%
plt.hist(data['sleep_hours'])
plt.xlabel('Sleep Time (hours)')
plt.ylabel('Frequency (# of students)')

#%%
# Remember - Histograms require continuous data.
# Histograms shouldn't be used with discrete or categorical data

# Bar Chart

#%%
import seaborn as sns
# sns.barplot(data, x='parental_education', y='student_id') # wrong usage with y-axis
# sns.barplot(data, x='parental_education', y='final_exam_score') # may be not right
# sns.barplot(data, x='parental_education')
data['parental_education'].value_counts().plot(kind='bar')

# %%
data['parental_education'].value_counts(normalize=True).plot(kind='bar')
# %%
data['gender'].value_counts().plot(kind='bar')
# %%
sns.barplot(data, x=data['study_time_hours'], y=data['parental_education'])
# %%
