import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """Load dataset from CSV file."""
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """Basic cleaning: remove duplicates, handle missing values."""
    df = df.drop_duplicates()
    df = df.fillna(0)   # You can change this based on your data
    return df

def split_data(df, target_column):
    """Split the data into train and test sets."""
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    path = "data.csv"          # Change if needed
    target = "revenue"         # Your target column name

    df = load_data(path)
    df = clean_data(df)

    X_train, X_test, y_train, y_test = split_data(df, target)

    print("Data Loaded Successfully!")
    print("Train Shape:", X_train.shape)
    print("Test Shape:", X_test.shape)