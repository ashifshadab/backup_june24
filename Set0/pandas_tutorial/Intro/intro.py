import pandas as pd
import numpy as np

def my_series():
    # Creating empty Series
    ser = pd.Series()

    # Print Series
    print("Panda series: \n",ser)

    # Simple Array
    data = np.array(['a','s','h','i','f'])

    ser = pd.Series(data)

    print("Panda series: \n",ser)

    return


def my_dataframe():
    # Calling DataFrame constructor
    df = pd.DataFrame()

    print("DataFrame: \n",df)

    list = ['One','two','three','four','five','six','seven','eight','nine','ten']

    # Call DataFram constructor on list
    df = pd.DataFrame(list)

    print("DataFrame: \n",df)

    return

my_series()

my_dataframe()