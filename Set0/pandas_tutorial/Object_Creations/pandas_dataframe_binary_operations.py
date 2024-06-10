import pandas as pd

# creating a series
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
 
# creating a series
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
 
print("First Series: \n",data, "\n \n Second Series: \n", data1)

# adding two series using
add_result=data.add(data1, fill_value=0)
print("\n Result after adding: \n",add_result)

# subtracting two series
sub_result = data.subtract(data1, fill_value=0)
print("\n Result after Subtracting: \n",sub_result)