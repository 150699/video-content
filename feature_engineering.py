import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def encode_categorical(df, categorical_cols):
    """One-hot encode categorical columns."""
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded = encoder.fit_transform(df[categorical_cols])

    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))

    df = df.drop(categorical_cols, axis=1)
    df = pd.concat([df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

    return df

def scale_numeric(df, numeric_cols):
    """Scale numeric columns using StandardScaler."""
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def preprocess_features(df, categorical_cols, numeric_cols):
    """Full feature engineering pipeline."""
    df = encode_categorical(df, categorical_cols)
    df = scale_numeric(df, numeric_cols)
    return df

if __name__ == "__main__":
    print("Feature engineering module loaded.")