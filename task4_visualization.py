import pandas as pd
import matplotlib.pyplot as plt
import os
# Load analysed data from Task 3
file_path = "data/trends_analysed.csv"

df = pd.read_csv(file_path)

print("Data loaded successfully")

if not os.path.exists("outputs"):
    os.makedirs("outputs")
  
top_stories = df.nlargest(10, "score")

top_stories["short_title"] = top_stories["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)
plt.figure(figsize=(8,6))

plt.barh(top_stories["short_title"], top_stories["score"], color="skyblue")

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

plt.tight_layout()

plt.savefig("outputs/chart1_top_stories.png")
print("chart1_top_stories.png")

plt.close()
category_counts = df["category"].value_counts()
plt.figure(figsize=(6,5))

plt.bar(
    category_counts.index,
    category_counts.values,
    color=["red","blue","green","orange","purple"]
)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.tight_layout()

plt.savefig("outputs/chart2_categories.png")
print("chart2_categories.png")

plt.close()
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]
plt.figure(figsize=(6,5))

plt.scatter(
    popular["score"],
    popular["num_comments"],
    color="green",
    label="Popular"
)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    color="red",
    label="Not Popular"
)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

plt.legend()

plt.tight_layout()

plt.savefig("outputs/chart3_scatter.png")
print("chart3_scatter.png")

plt.close()
fig, axes = plt.subplots(1, 3, figsize=(15,5))

# Chart 1
axes[0].barh(top_stories["short_title"], top_stories["score"], color="skyblue")
axes[0].set_title("Top 10 Stories")

# Chart 2
axes[1].bar(category_counts.index, category_counts.values,
            color=["red","blue","green","orange","purple"])
axes[1].set_title("Stories per Category")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"],
                color="green", label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"],
                color="red", label="Not Popular")

axes[2].set_title("Score vs Comments")
axes[2].legend()


fig.suptitle("TrendPulse Dashboard")

plt.tight_layout()

plt.savefig("outputs/dashboard.png")
print("dashboard.png (bonus)")
plt.close()