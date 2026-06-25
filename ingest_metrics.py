import pandas as pd
import sqlite3

#loading files
loadshedding_df = pd.read_csv("data/loadshedding.csv")
jobs_df = pd.read_csv("data/jobs.csv")

#Temporary
print(loadshedding_df.head())
print(jobs_df.head())

merged_df = pd.merge(loadshedding_df, jobs_df, on="date")  #Merging data

# clean column names
merged_df = merged_df.rename(columns={
    "date": "log_date",
    "stage": "loadshedding_stage"
})


# Remote Percentage
merged_df["remote_percentage"] = (
    merged_df["remote_jobs"] / merged_df["total_jobs"]
) * 100

merged_df["remote_percentage"] = merged_df["remote_percentage"].round(2)


# if total jobs = 0, I might get division errors
# Will fix that later

