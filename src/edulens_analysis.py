import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    """Load student performance dataset"""
    return pd.read_csv(path)

def basic_overview(df):
    """Display basic information about the dataset"""
    print("Dataset Preview:")
    print(df.head(), "\n")

    print("Statistical Summary:")
    print(df.describe())

def performance_distribution(df):
    """Visualize score distribution"""
    plt.figure(figsize=(6, 4))
    plt.hist(df["math_score"], bins=10, edgecolor="black")
    plt.title("Distribution of Math Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data_path = "data/students.csv"
    df = load_data(data_path)
    basic_overview(df)
    performance_distribution(df)
