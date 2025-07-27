# %% [markdown]
# # EDA Project 2: EDA with Student Performance Indicator 

# %% [markdown]
# # About Project/Dataset

# %% [markdown]
# # 1) Problem Statement
# * This project understand how the student's performance (test score) is affected by other variables such as Gender,REthinicity,Parental level of Education, Lunch and Test Prepration Course.

# %% [markdown]
# # 2) Data Collection
# * Dataset Source : https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
# * The Data consist of 8 column and 1000 rows

# %% [markdown]
# # 3) Dataset Information
# * gender : sex of students ->(Male/Female)
# * race/ethnicity : ehtinicity of student - > (Group A,B,C,D,E)
# * Parental level of education : Parent's final education -> (Bachelor's degree some college matter's degree associates degree high school)
# * lunch : having lunch before test(standard or free/reduced)
# * test prepration course: complete or not complete before test
# * math score
# * reading score
# * writing score

# %% [markdown]
# # i> import all necessary library

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# %% [markdown]
# # ii> Read the CSV File

# %%
df = pd.read_csv('stud.csv')

# %%
df.head()

# %%
df.shape

# %% [markdown]
# # Data Cleaning/Preprocessing

# %% [markdown]
# # iii> Data Checks to Perform
# * Check Missing Values
# * Check Duplicates
# * Check Datatype
# * Check the number of unique values of each column
# * Check statistics of data set
# * Check various categories present in the differnet categorical column

# %%
## iii.i> check missing Values
df.isnull().sum()

# %% [markdown]
# # Insights or Observation
# 
# There are no missing values

# %%
df.isna().sum()

# %%
## iii.ii> Check Duplicates
df.duplicated().sum()

# %% [markdown]
# * There are no duplicate value in the dataset

# %%
## iii.iii> Check Datatypes
df.info()

# %%
## iii.iv> Checking the number of unique value of each columns
df.nunique()

# %%
# iii.v> Check the statistics of the dataset
df.describe()

# %% [markdown]
# # Insights or Observation
# * From the above description of numerical data , all means are very close to each other-beween 66 and 69
# * All the standard daviation are also close-between 14.6-15.19
# * While there is a minimum of 0 for maths,other are having 17 and 10 value

# %%
## Explore more info about the data
df.head()

# %%
df.tail()

# %% [markdown]
# # Seperate Categorical Feature and numeric Feature

# %%
[feature for feature in df.columns if df[feature].dtype!='O']

# %%
numerical_feature = [feature for feature in df.columns if df[feature].dtype!='O']
categoical_feature = [feature for feature in df.columns if df[feature].dtype=='O']

# %%
numerical_feature

# %%
categoical_feature

# %% [markdown]
# # Insights from Categorical feature

# %%
df['gender'].value_counts()

# %%
df['race_ethnicity'].value_counts()

# %% [markdown]
# # Insights from Numerical Feature

# %%
df['total_score']=(df['math_score']+df['reading_score']+df['writing_score'])
df['average']= df['total_score']/3
df.head()

# %%
df.to_csv('updated_file.csv', index=False)

# %% [markdown]
# ## Explore More Visualization

# %% [markdown]
# # Insights : Count the average score & average stundent performance compare to it's gender

# %%
plt.figure(figsize=(10,6))
plt.subplot(121)
sns.histplot(data = df, x = 'average' , bins=30,kde = True, color = 'g')
plt.subplot(122)
sns.histplot(data = df, x = 'average' , bins = 30 , kde = True , hue ='gender')

# %% [markdown]
# # Insights or Observation: 
# * Female Student tend to perform well than male students

# %% [markdown]
# # Objective : Plot a graph of average of lunch 

# %%
plt.figure(figsize=(25,6))
plt.subplot(141)
sns.histplot(data = df, x = 'average' , bins=30,kde = True, hue = 'lunch')
plt.subplot(142)
sns.histplot(data = df[df.gender=='female'] , x= 'average' , kde =True , hue = 'lunch')
plt.subplot(143)
sns.histplot(data = df[df.gender=='male'] , x= 'average' , kde =True , hue = 'lunch')

# %% [markdown]
# # Insights or Observation:
# * Standard lunch help students perform well in exams
# * Standard lunch helps perform well in exams be it a male or female

# %% [markdown]
# # Objective : Plot a graph to showcase avearge counts based on parental_level_of_education 
# wheather in general case
# or on the basis of gender

# %%
plt.figure(figsize=(25,6))
plt.subplot(141)
sns.histplot(data = df, x = 'average' , bins=30,kde = True, hue = 'parental_level_of_education')
plt.subplot(142)
sns.histplot(data = df[df.gender=='female'] , x= 'average' , kde =True , hue = 'parental_level_of_education')
plt.subplot(143)
sns.histplot(data = df[df.gender=='male'] , x= 'average' , kde =True , hue = 'parental_level_of_education')

# %% [markdown]
# # Insigths or Observation:
# * In general parent's education don't help studnet perform well in exam
# * 3rd plot shows that parent's whose eduction is of associate's degree or master's degree there male child tend to perform well in exam
# * 2nd plot we can see there is no effect of parent's education on female students.

# %%
plt.figure(figsize=(25,6))
plt.subplot(141)
sns.histplot(data = df, x = 'average' , bins=30,kde = True, hue = 'race_ethnicity')
plt.subplot(142)
sns.histplot(data = df[df.gender=='female'] , x= 'average' , kde =True , hue = 'race_ethnicity')
plt.subplot(143)
sns.histplot(data = df[df.gender=='male'] , x= 'average' , kde =True , hue = 'race_ethnicity')

# %% [markdown]
# # Insights or Observation:
# * Students of group A and group B tends to perform poorly in exam
# * Students of grapup A and group B tends to perform poorly in exam irrespective of wheather they are male or female

# %% [markdown]
# # Objective : Show co-relation of numeric data

# %%
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')

# %%



