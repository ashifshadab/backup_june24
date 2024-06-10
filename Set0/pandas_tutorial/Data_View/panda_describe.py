import pandas as pd

data = pd.read_csv("assets/Sample.csv")

def example_describe1():
    print(data.describe())
    return


def example_describe2():
    # The dropna() method removes the rows that contains NULL values.
    # The dropna() method returns a new DataFrame object 
    # unless the inplace parameter is set to True, 
    # in that case the dropna() method does the removing 
    # in the original DataFrame instead.
    data.dropna(inplace=True)

    # percentile list
    perc = [.20, .40, .60, .80]
 
    # list of dtypes to include
    include = ['object', 'float', 'int']
 
    # calling describe method
    desc = data.describe(percentiles=perc, include=include)

    print("\n",desc)

    return

def example_describe3():
    # removing null values to avoid errors
    data.dropna(inplace=True)
 
    # calling describe method
    desc = data["Name"].describe()

    print("\n",desc)
    return

# Using Describe function in Pandas
example_describe1()

# In this example, the data frame is described and [‘object’] is passed 
# to include a parameter to see a description 
# of the object series. [.20, .40, .60, .80] 
# is passed to the percentile parameter 
# to view the respective percentile of the Numeric series. 
example_describe2()

example_describe3()