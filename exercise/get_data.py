import pandas as pd


def get_data(colum_name):
    df = pd.read_csv("exercise/happy.csv")
    colum_name = colum_name.lower()
    return df[colum_name]
