import pandas as pd

def get_data(f):
    """
    This is a function that takes a file path and read in data
    with pandas
    : f: filepath
    : df: resulting data
    """
    
    df = pd.read_csv(f)

    return df