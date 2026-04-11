import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =====================================
# Paths
# =====================================
DATA_PATH = "../data/students.csv"
OUTPUT_DIR = "../insights"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================
# Load Data
# =====================================
def load_data(path):
    return pd.read_csv(path)

# =====================================
# Preprocess Data
# =====================================
def preprocess_data(df):
    df["total_score"] = (
        df["math score"]
        + df["reading score"]
        + df["writing score"]
    )
    df["average_score"] = df["total_score"] / 3
    return df

# =====================================
# Visualizations (Different Graph Types)
# =====================================

def gender_boxplot(df):
    plt.figure(figsize=(6, 4))
    sns.boxplot(x="gender", y="average_score", data=df)
    plt.title("Score Distribution by Gender")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "gender_boxplot.png"))
    plt.close()


def parental_barh(df):
    data = df.groupby("parental level of education")["average_score"].mean()
    plt.figure(figsize=(7, 5))
    data.sort_values().plot(kind="barh", color="teal")
    plt.title("Average Score by Parental Education")
    plt.xlabel("Average Score")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "parental_education_barh.png"))
    plt.close()


def test_prep_pie(df):
    data = df["test preparation course"].value_counts()
    plt.figure(figsize=(5, 5))
    data.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Test Preparation Course Participation")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "test_prep_pie.png"))
    plt.close()


def subject_line_chart(df):
    subjects = {
        "Math": df["math score"].mean(),
        "Reading": df["reading score"].mean(),
        "Writing": df["writing score"].mean(),
    }

    plt.figure(figsize=(6, 4))
    plt.plot(subjects.keys(), subjects.values(), marker="o")
    plt.title("Average Score by Subject")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "subject_line_chart.png"))
    plt.close()


def math_vs_reading_scatter(df):
    plt.figure(figsize=(6, 4))
    sns.scatterplot(
        x="math score",
        y="reading score",
        data=df
    )
    plt.title("Math vs Reading Score Relationship")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "math_vs_reading_scatter.png"))
    plt.close()

# =====================================
# Main Function
# =====================================
def main():
    print("📊 Student Performance Analysis Started")

    df = load_data(DATA_PATH)
    df = preprocess_data(df)

    gender_boxplot(df)
    parental_barh(df)
    test_prep_pie(df)
    subject_line_chart(df)
    math_vs_reading_scatter(df)

    print("✅ Analysis completed successfully")
    print("📁 Results saved in insights/ folder")


if __name__ == "__main__":
    main()