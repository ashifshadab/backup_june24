import pandas as pd

# Python code demonstrate to create a Pandas DataFrame 
# with lists of dictionaries as well as
# row and column indexes.
def example1():

    # Initialize lists data.
    data = [{'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}]
  
    # With two column indices, values same
    # as dictionary keys
    df1 = pd.DataFrame(data, index=['first','second'], columns=['a', 'b'])

    print("\n Pandas DataFrame with lists of dictionaries as well" 
          +" as row and column indexes.\n")
    print(df1)

    # With two column indices with
    # one index with other name
    df2 = pd.DataFrame(data, index=['first','second'], columns=['a', 'b1'])

    print("\n Pandas DataFrame with lists of dictionaries as well" 
          +" as row and column indexes 1.\n")
    print(df2)

    return


# Creating dataframe from series
def example2():
    # Initialize data to series.
    d =  pd.Series([10, 20, 30, 40])
    # creates Dataframe.
    df = pd.DataFrame(d)
  
    print("\n Creating dataframe from series \n")
    # print the data.
    print(df)

    return


# Creating DataFrame from Dictionary of series.
def example3():
    # Initialize data to Dicts of series.
    d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}
  
    # creates Dataframe.
    df = pd.DataFrame(d)

    print("\n Creating dataframe from Dictionary of series \n")
    # print the data.
    print(df)

    return

# Convert a list of dictionaries to a pandas DataFrame using from_records()
def example4():
    # Initialise data to lists.
    data = [{'Ashif': 'Shadab', 'Python': 'numpy', 'Pandas': 'list'},
        {'Ashif':10, 'Python': 20, 'Pandas': 30}]
 
    df = pd.DataFrame.from_records(data,index=['1', '2'])

    print("\n from_records \n")
    # print the data.
    print(df)
    return

# Convert a list of dictionaries to a pandas DataFrame using pd.DataFrame.from_dict()
def example5():
    # Initialise data to lists.
    data = [{'Ashif': 'Shadab', 'Python': 'numpy', 'Pandas': 'list'},
        {'Ashif':10, 'Python': 20, 'Pandas': 30}]                                   
 
    df = pd.DataFrame.from_dict(data)

    print("\n pd.DataFrame.from_dict() \n")
    
    # print the data.
    print(df)
    return

# Convert a list of dictionaries to a pandas DataFrame using pd.json_normalize
def example6():
    data = [{'Ashif': 'Shadab', 'Python': 'numpy', 'Pandas': 'list'},
        {'Ashif':10, 'Python': 20, 'Pandas': 30}]   
    
    df=pd.json_normalize(data)

    print("\n pd.json_normalize \n")
    
    # print the data.
    print(df)
    return

# Given a dictionary which contains format of cricket as keys 
# and list of top five teams as values.
def example7():
    # Define a dictionary containing ICC rankings
    rankings = {'test': ['India', 'South Africa', 'England',
                            'New Zealand', 'Australia'],
              'odi': ['England', 'India', 'New Zealand',
                            'South Africa', 'Pakistan'],
               't20': ['Pakistan', 'India', 'Australia', 
                              'England', 'New Zealand']}
  
    # Convert the dictionary into DataFrame
    rankings_pd = pd.DataFrame(rankings)
  
    # Increment the index so that index 
    # starts at 1 (starts at 0 by default) 
    rankings_pd.index += 1

    print("\n Increment the index \n")
    print(rankings_pd)
    return


example1()
example2()
example3()
example4()
example5()
example6()
example7()