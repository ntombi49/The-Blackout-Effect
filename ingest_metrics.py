import pandas as pd
import sqlite3

#loading files
loadshedding_df = pd.read_csv("data/loadshedding.csv")
jobs_df = pd.read_csv("data/jobs.csv")

#Temporary
print(loadshedding_df.head())
print(jobs_df.head())

merged_df = pd.merge(loadshedding_df, jobs_df, on="date")  #Merging data

