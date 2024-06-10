import pandas as pd

# making data frame
data = pd.read_csv("assets/Sample.csv")

def example_head():
    # # calling head() method
    data_result = data.head()

    print("Default behavior of head: \n",data_result)
    

    data_result1 = data.head(2)

    print("\n Only Two row by head: \n",data_result1)

    data1 = data["Name"]

    data_result2 = data1.head(2)

    print("\n Again Only Two row by head: \n",data_result2)

    return

def example_tail():
    data_result = data.tail()

    print("Default behavior of tail: \n",data_result)

    data_result1 = data.tail(2)

    print("\n Only Two records via tail: \n",data_result1)

    data1 = data["Name"]

    data_result2 = data1.tail(2)

    print("\n Only Two records via tail but only Name: \n",data_result2)


    return


# Pandas head() method is used to return top n 
# (5 by default) rows of a data frame or series.
example_head()

# Pandas tail() method is used to return bottom n 
# (5 by default) rows of a data frame or series.
example_tail()