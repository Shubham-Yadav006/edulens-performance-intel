import pandas as pd
import matplotlib.pyplot as plt
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
# Analysis
# =====================================
def average_by_category(df, column):
    return df.groupby(column)["average_score"].mean().sort_values(ascending=False)


# =====================================
# Visualization
# =====================================
def save_bar_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(8, 5))
    data.plot(kind="bar", color="cornflowerblue")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()


# =====================================
# Main Function
# =====================================
def main():
    print("📊 Student Performance Analysis Started")

    df = load_data(DATA_PATH)
    df = preprocess_data(df)

    gender_avg = average_by_category(df, "gender")
    parental_avg = average_by_category(df, "parental level of education")
    lunch_avg = average_by_category(df, "lunch")
    prep_avg = average_by_category(df, "test preparation course")

    save_bar_chart(
        gender_avg,
        "Average Score by Gender",
        "Gender",
        "Average Score",
        "gender_analysis.png"
    )

    save_bar_chart(
        parental_avg,
        "Average Score by Parental Education",
        "Education Level",
        "Average Score",
        "parental_education_analysis.png"
    )

    save_bar_chart(
        lunch_avg,
        "Average Score by Lunch Type",
        "Lunch Type",
        "Average Score",
        "lunch_analysis.png"
    )

    save_bar_chart(
        prep_avg,
        "Impact of Test Preparation Course",
        "Test Preparation",
        "Average Score",
        "test_prep_analysis.png"
    )

    print("✅ Analysis completed successfully")
    print("📁 Results saved in insights/ folder")


if __name__ == "__main__":
    main()
