import pandas as pd
import numpy as np


def features_split(train: pd.DataFrame):
    NON_FEATURES = ["lead_id", "user_id", "target",'assignment_ts', 'assignment_date']

    features = [
        idx for idx in train.columns if idx not in NON_FEATURES
    ] 

    numeric = [
        idx for idx in train.columns if pd.api.types.is_numeric_dtype(train[idx]) and idx not in NON_FEATURES
    ]
    category = [
        idx for idx in train.columns if idx not in numeric and idx not in NON_FEATURES
    ]

    return features, numeric, category




def train_val_split(train:pd.DataFrame, train_size=0.8):
    
    features, numeric, category = features_split(train=train)


    train = train.sort_values(by=["assignment_ts"]).reset_index(drop=True)


    idx_val_train = int(np.ceil(len(train)*train_size))
    train_v1 = train[:idx_val_train].reset_index(drop=True)
    val_v1 = train[idx_val_train:].copy().reset_index(drop=True)

    Y_train = train_v1["target"]
    X_train = train_v1[features]
    Y_val = val_v1["target"]
    X_val = val_v1[features]
    X_train = X_train.loc[:, ~X_train.columns.duplicated()]
    X_val = X_val.loc[:, ~X_val.columns.duplicated()]
    return X_train, X_val, Y_train, Y_val, val_v1