import pandas as pd

# making data frame 
df = pd.read_csv('assets/Sample.csv')
print("Csv Data:",df)

ser = pd.Series(df['Name']) 
data = ser.head(10)
print("\n Series elements:",data)

def help_print(txt,data):
    print("\n",txt,"\n")
    print(data)
    return

def example():    
    # using indexing operator
    help_print("Print only Name starting from 3 and end at 5:",data[3:6])

    return

# This function selects data by refering the explicit index . 
# The df.loc indexer selects data in a different way than just the indexing operator. 
# It can select subsets of data.
def example1():    
    # # using .loc[] function
    help_print("Print only Name starting from 3 and end at 6, using loc:",data.loc[3:6])
    
    return

# The df.iloc indexer is very similar to df.loc 
# but only uses integer locations to make its selections.
def example2():
    # # using .iloc[] function
    help_print("Print only Name starting from 3 and end at 5 ," 
               "using iloc:",data.iloc[3:6])
    return

# Access the element of series using index operator [ ]
example()

# Indexing a Series using .loc[ ] :
example1()

# Indexing a Series using .iloc[ ] :
example2()
