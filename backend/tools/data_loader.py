import pandas as pd

def load_dataset(file):
    df=pd.read_csv(file)
    return df


def dataset_info(df):
    info={
        "columns":list(df.columns),
        "rows":df.shape[0],
        "missing_values":df.isnull().sum().to_dict()
    }

    return info
