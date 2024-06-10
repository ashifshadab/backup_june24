import pandas as pd

# Creating an empty dataframe
def cereate_empty_dataframe():
    print("Creating an empty dataframe \n")
    # An Empty Dataframe is created just by calling a dataframe constructor. 
    df = pd.DataFrame()
    print(df)
    return

# Create a dataframe with list
def create_dataframe_via_list():
    print("\n Create a dataframe with list \n")
    # list of strings
    lst = ['Ashif', 'Shadab', 'Python', 'Pandas', 
            'numpy', 'dataframe', 'series']
  
    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst)
    print(df)
    return

# Dataframe using list with index and column names
def create_datafram_via_list_with_index_names():
    print("\n Dataframe using list with index and column names \n")
    # list of strings
    lst = ['Ashif', 'Shadab', 'Python', 'Pandas', 
            'numpy', 'dataframe', 'series']
    
    # Calling DataFrame constructor on list
    # with indices and columns specified
    df = pd.DataFrame(lst, index =['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                                              columns =['Names'])
    
    print(df)
    return

# DataFrame Using zip() for zipping two lists
# Two lists can be merged by using list(zip()) function.
def create_dataframe_via_zipping_two_lists():
    print("\n Create a dataframe with list \n")
    # list of strings
    lst = ['Ashif', 'Shadab', 'Python', 'Pandas', 
            'numpy', 'dataframe', 'series']
    # list of int
    lst2 = [11, 22, 33, 44, 55, 66, 77]
  
    # Calling DataFrame constructor after zipping
    # both lists, with columns specified
    df = pd.DataFrame(list(zip(lst, lst2)),
               columns =['Name', 'value'])
    
    print(df)
    return

# Creating DataFrame using multi-dimensional list
def create_dataframe_using_multi_dimenstional_list():
    print("\n Creating DataFrame using multi-dimensional list \n")
    # List1 
    lst = [['tom', 25], ['krish', 30],
       ['nick', 26], ['juli', 22]]
    
    df = pd.DataFrame(lst, columns =['Name', 'Age'])

    print(df)

    print("\n Using multi-dimensional list with column name and dtype specified \n")

    lst1 = [['tom', 'reacher', 25], ['krish', 'pete', 30],
       ['nick', 'wilson', 26], ['juli', 'williams', 22]]
    
    df1 = pd.DataFrame(lst1, columns =['FName', 'LName', 'Age'])

    print(df1)

    return

# Using lists in dictionary to create dataframe
def create_dataframe_using_list_in_dictionary():
    print("\n Using lists in dictionary to create dataframe \n")
    # list of name, degree, score
    nme = ["aparna", "pankaj", "sudhir", "Geeku"]
    deg = ["MBA", "BCA", "M.Tech", "MBA"]
    scr = [90, 40, 80, 98]
  
    # dictionary of lists 
    dict = {'name': nme, 'degree': deg, 'score': scr} 
    
    df = pd.DataFrame(dict)

    print(df)

    print("\n One more using dictionary \n")

    dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
    df = pd.DataFrame(dict)
 
    print(df)

    # Adding index to a dataframe explicitly
    print("\n Adding index to a dataframe explicitly \n")

    # dictionary of lists
    dict = {'name':['aparna', 'pankaj', 'sudhir', 'Geeku'],
        'degree': ['MBA','BCA', 'M.Tech', 'MBA'],
        'score':[90, 40, 80, 98]}
 
    df = pd.DataFrame(dict,index=['Rollno1','Rollno2','Rollno3','Rollno4'])
 
    print(df)

    return

# Creating DataFrame from dict narray / lists
def create_dataframe_from_dict_narray():
    print("\n Creating DataFrame from dict narray / lists \n")
    # initialise data of lists.
    data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
 
    # Create DataFrame
    df = pd.DataFrame(data)
 
    # Print the output.
    print(df)
    return


# Using from_dict() function
def Using_from_dict_function():
    print("\n Using from_dict() function \n")
    # dictionary of lists
    dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
    df = pd.DataFrame.from_dict(dict)
    print(df)
    return

cereate_empty_dataframe()    
create_dataframe_via_list()
create_datafram_via_list_with_index_names()
create_dataframe_via_zipping_two_lists()
create_dataframe_using_multi_dimenstional_list()
create_dataframe_using_list_in_dictionary()
create_dataframe_from_dict_narray()
Using_from_dict_function()