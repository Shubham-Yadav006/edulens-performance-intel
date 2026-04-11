import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================
# Configuration
# ==============================
DATA_PATH = "../data/students.csv"
OUTPUT_DIR = "../insights"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================
# Load Dataset
# ==============================
def load_data(path):
    df = pd.read_csv(path)
    return df


# ==============================
# Feature Engineering
# ==============================
def preprocess_data(df):
    df["total_score"] = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
    )
    df["average_score"] = df["total_score"] / 3
    return df


# ==============================
# Analysis Functions
# ==============================
def average_by_category(df, column):
    return df.groupby(column)["average_score"].mean().sort_values(ascending=False)


# ==============================
# Visualization
# ==============================
def plot_and_save(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(8, 5))
    data.plot(kind="bar", color="steelblue")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()


# ==============================
# Main Execution
# ==============================
def main():
    print("Loading data...")
    df = load_data(DATA_PATH)

    print("Preprocessing data...")
    df = preprocess_data(df)

    print("Analyzing performance trends...")

    gender_avg = average_by_category(df, "gender")
    parental_avg = average_by_category(df, "parental level of education")
    prep_avg = average_by_category(df, "test preparation course")
    lunch_avg = average_by_category(df, "lunch")

    print("Generating visual insights...")

    plot_and_save(
        gender_avg,
        "Average Score by Gender",
        "Gender",
        "Average Score",
        "gender_performance.png"
    )

    plot_and_save(
        parental_avg,
        "Average Score by Parental Education",
        "Education Level",
        "Average Score",
        "parental_education_performance.png"
    )

    plot_and_save(
        prep_avg,
        "Impact of Test Preparation Course",
        "Test Preparation",
        "Average Score",
        "test_prep_performance.png"
    )

    plot_and_save(
        lunch_avg,
        "Impact of Lunch Type on Performance",
        "Lunch Type",
        "Average Score",
        "lunch_performance.png"
    )

    print("✅ Analysis complete. Insights saved in /insights folder.")


if __name__ == "__main__":
    main()
