import pandas as pd
import numpy as np

## Pandas Series
# Pandas Series is a one-dimensional labeled array capable of holding data of 
# any type (integer, string, float, python objects, etc.).
# Pandas Series is nothing but a column in an excel sheet.

def printseries(txt,ser):
    # Printing the Text
    print(txt,"\n")

    # Printing th element o Series
    print(ser,"\n")

    return

def example():
    ser = pd.Series()

    # Print Series elements
    printseries('Creating empty series:',ser)
    return

def example1():
    
    # # simple array
    data =[1,2,3,4,5]

    # Creating a series from array
    ser = pd.Series(data)

    # Print Series elements
    printseries('Creating a series from array:',ser)

    return

def example2():
    data = np.array(['Ashif','Shadab','Python','Numpy','Pandas'])

    # Creating a series from numpy array
    ser = pd.Series(data)

    # Print Series elements
    printseries('Creating a series from numpy array:',ser)
    return

def example3():

    data = np.array(['Ashif','Shadab','Python','Numpy','Pandas'])

    
    index=[10, 11, 12, 13, 14]

    # providing an index
    ser = pd.Series(data, index)

    # Print Series elements
    printseries('Creating a series from array with an index:',ser)    

    return

def example4():
    # a simple dictionary
    dict = {'Apple': 10,
        'Mango': 20,
        'Grapes': 30}
 
    # create series from dictionary
    ser = pd.Series(dict)
    # Print Series elements
    printseries('Creating a series from Dictionary:',ser)   
    return

def example5():
    # giving a scalar value with index
    index=[0, 1, 2, 3, 4, 5]
    ser = pd.Series(10, index)
    # Print Series elements
    printseries('Creating a series from Scalar value: ',ser)  
    return

def example6():
    ser=pd.Series(range(10))
    # Print Series elements
    printseries('Creating a Series using range function: ',ser) 
    return

def example7():
    #Creating a Series using for loop and list comprehension
    ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
    # Print Series elements
    printseries('Creating a Series using for loop and list comprehension: ',ser) 
    return

def example8():
    nparr=np.arange(10,15)
    ser=pd.Series(data=nparr*5,index=nparr)
    # Print Series elements
    printseries('Creating a Series using mathematical expressions: ',ser) 
    return

def example9():
    data = np.array(['One','Two','Three','Four','Five','Six','Seven',
                     'Eight','Nine','Ten'])
    
    ser = pd.Series(data)

    printseries('Element of Series: ',ser) 

    printseries('First element of Series: ',ser[0]) 
    printseries('Fourth element of Series: ',ser[3]) 
    printseries('Five elements of Series: ',ser[:5])

    return

def example10():
    data = np.array(['One','Two','Three','Four','Five','Six','Seven',
                     'Eight','Nine','Ten'])
    ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19])
  
    # Accessing a element using index element
    printseries('Accessing a element using index element: ',ser[11])

    return


# Creating empty series
example()

# Creating a series from array
example1()

# Creating a series from numpy array
example2()

# Creating a series from array with an index
example3()

# Creating a series from Dictionary
example4()

# Creating a series from Scalar value
example5()

# Creating a Series using range function
example6()

# Creating a Series using for loop and list comprehension
example7()

# Creating a Series using mathematical expressions:
example8()

# Accessing Element from Series with Position
example9()

# Accessing a element using index element
example10()
