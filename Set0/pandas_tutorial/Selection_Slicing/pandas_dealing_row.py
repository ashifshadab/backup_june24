import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)

def example_select_cloumns():

    # select two columns
    print("\n Selecting Two Cloumns \n")
    print(df[['Name', 'Qualification']])

    # select all rows 
    # and second to fourth column
    print("\n Selecting all rows and second to fourth column \n")
    print(df[df.columns[1:4]])

    # select three rows and two columns
    print("\n Selecting three rows and two columns \n")
    print(df.loc[1:3, ['Name', 'Qualification']])

    # select two rows and 
    # column "name" to "Address"
    # Means total three columns
    print("\n Selecting two rows and column 'name' to 'Address'"
          "Means total three columns \n")
    print(df.loc[0:1, 'Name':'Address'])

    # .loc DataFrame method
    # filtering rows and selecting columns by label
    # format
    # df.loc[rows, columns]
    # row 1, all columns
    print("\n Filtering rows and selecting columns by label\n")
    print(df.loc[0, :])


    # select all rows 
    # select first two column

    print("\n select all rows and select first two column\n")
    print(df.iloc[:, 0:2])

    # iloc[row slicing, column slicing]
    print("\n Select all or some columns, one to another using .iloc.\n")
    print(df.iloc [0:2, 1:3])

    # select all rows and 0 to 2 columns 
    #print("\n Select all or some columns, one to another using .ix.\n")
    #print(df.ix[:, 0:2])
    return


example_select_cloumns()