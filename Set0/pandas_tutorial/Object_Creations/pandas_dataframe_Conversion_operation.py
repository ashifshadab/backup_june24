import pandas as pd 

# reading csv file from url  
data = pd.read_csv("assets/Sample.csv") 

# dropping null value columns to avoid errors 
data.dropna(inplace = True)

def example1(data):
    # storing dtype before converting 
    before = data.dtypes 
   
    # converting dtypes using astype 
    data["Salary"]= data["Salary"].astype(int) 
    data["Number"]= data["Number"].astype(str) 
   
    # storing dtype after converting 
    after = data.dtypes 
   
    # printing to compare 
    print("BEFORE CONVERSION\n", before, "\n") 
    print("AFTER CONVERSION\n", after, "\n") 
    return

def example2(data):
    # storing dtype before operation 
    dtype_before = type(data["Salary"]) 
   
    # converting to list 
    salary_list = data["Salary"].tolist() 
   
    # storing dtype after operation 
    dtype_after = type(salary_list) 
   
    # printing to compare 
    print("\n Data Type BEFORE CONVERSION: ", dtype_before, "\n") 
    print(" Data Type AFTER CONVERSION: ", dtype_after, "\n")
    
   
    # displaying list 
    print("\n Salary List \n",salary_list )
    return

example1(data)

example2(data)