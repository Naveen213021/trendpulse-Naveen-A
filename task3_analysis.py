import pandas as pd
import numpy as np
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)
print("Loaded data:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", round(avg_score,2))
print("Average comments:", round(avg_comments,2))
scores = df["score"].to_numpy()
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
print("\n--- NumPy Stats ---")
print("Mean score   :", mean_score)
print("Median score :", median_score)
print("Std deviation:", std_score)
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print("\nMost stories in:", top_category, f"({count} stories)")
max_comments_row = df.loc[df["num_comments"].idxmax()]

title = max_comments_row["title"]
num_comments = max_comments_row["num_comments"]

print("\nMost commented story:")
print("Title:", title)
print("Comments:", num_comments)
comments = max_comments_row["num_comments"]

df["is_popular"] = df["score"] > avg_score
output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print("\nSaved to", output_file)
