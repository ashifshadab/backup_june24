# Pandas
Pandas is an open-source library that is built on top of NumPy library.

# Why Use Pandas?
<ul>
    <li>Fast and efficient for manipulating and analyzing data.</li>
    <li>Data from different file objects can be easily loaded.</li>
    <li>Flexible reshaping and pivoting of data sets</li>
    <li>Provides time-series functionality.</li>
</ul>

# What can you do using Pandas?
<ul>
    <li>Data set cleaning, merging, and joining.</li>
    <li>Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data.</li>
    <li>Columns can be inserted and deleted from DataFrame and higher dimensional objects.</li>
    <li>Powerful group by functionality for performing split-apply-combine operations on data sets.</li>
    <li>Data Visulaization</li>
</ul>

# Pandas Data Structures
Pandas generally provide two data structures for manipulating data, They are: 
<ol>
    <li>Series</li>
    <li>DataFrame</li>
</ol>

# Series
Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). 
The axis labels are collectively called indexes.

Pandas Series is nothing but a column in an Excel sheet. Labels need not be unique but must be a hashable type. The object supports both integer and label-based indexing and provides a host of methods for performing operations involving the index.

![](/assets/SERIES-300x97.png)

# DataFrame
Pandas DataFrame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). 

A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. 

Pandas DataFrame consists of three principal components: -
<ol>
    <li>data</li>
    <li>rows</li>
    <li>columns</li>
</ol>

![](/assets/pandas-dataframe.png)

# The syntax of creating dataframe is:
<h1 align="middle">pandas.DataFrame(data, index, columns)</h1>
<ol>
<li><b style="font-size:20px">data:</b> It is a dataset from which dataframe is to be created. It can be list, dictionary, scalar value, series, ndarrays, etc.</li>

<li><b style="font-size:20px">index:</b> It is optional, by default the index of the dataframe starts from 0 and ends at the last data value(n-1). It defines the row label explicitly.</li>

<li><b style="font-size:20px">columns:</b> This parameter is used to provide column names in the dataframe. If the column name is not defined by default, it will take a value from 0 to n-1.</li>
</ol>

# Pandas from_records() function
Pandas from_records() function of DataFrame changes structured data or records into DataFrames. It converts a structured ndarray, tuple or dict sequence, or DataFrame into a DataFrame object.

# The DataFrame.from dict() method
The DataFrame.from dict() method in Pandas builds DataFrame from a dictionary of the dict or array type. By using the dictionary’s columns or indexes and allowing for Dtype declaration, it builds a DataFrame object.

# json_normalize() 
Pandas have a nice inbuilt function called json_normalize() to flatten the simple to moderately semi-structured nested JSON structures to flat tables.

# Pandas Series
Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).

Pandas Series is nothing but a column in an excel sheet.
Labels need not be unique but must be a hashable type. The object supports both integer and label-based indexing and provides a host of methods for performing operations involving the index.

![](/assets/dataSER-1.png)

# Accessing element of Series
There are two ways through which we can access element of series, they are :
<ol>
    <li>Accessing Element from Series with Position</li>
    <li>Accessing Element Using Label (index)</li>
</ol>

# Pandas series method:
<table>
  <tbody>
    <tr>
      <th>Function</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>
        <strong>Series()</strong>
      </td>
      <td>A pandas Series can be created with the Series() constructor method. This constructor method accepts a variety of inputs</td>
    </tr>
    <tr>
      <td>
        <strong>combine_first()</strong>
      </td>
      <td>Method is used to combine two series into one</td>
    </tr>
    <tr>
      <td>
        <strong>count()</strong>
      </td>
      <td>Returns number of non-NA/null observations in the Series</td>
    </tr>
    <tr>
      <td>
        <strong>size()</strong>
      </td>
      <td>Returns the number of elements in the underlying data</td>
    </tr>
    <tr>
      <td>
        <strong>name()</strong>
      </td>
      <td>Method allows to give a name to a Series object, i.e. to the column</td>
    </tr>
    <tr>
      <td>
        <strong>is_unique()</strong>
      </td>
      <td>Method returns boolean if values in the object are unique</td>
    </tr>
    <tr>
      <td>
        <strong>idxmax()</strong>
      </td>
      <td>Method to extract the index positions of the highest values in a Series</td>
    </tr>
    <tr>
      <td>
        <strong>idxmin()</strong>
      </td>
      <td>Method to extract the index positions of the lowest values in a Series</td>
    </tr>
    <tr>
      <td>
        <strong>sort_values()</strong>
      </td>
      <td>Method is called on a Series to sort the values in ascending or descending order</td>
    </tr>
    <tr>
      <td>
        <strong>sort_index()</strong>
      </td>
      <td>Method is called on a pandas Series to sort it by the index instead of its values</td>
    </tr>
    <tr>
      <td>
        <strong>head()</strong>
      </td>
      <td>Method is used to return a specified number of rows from the beginning of a Series. The method returns a brand new Series</td>
    </tr>
    <tr>
      <td>
        <strong>tail()</strong>
      </td>
      <td>Method is used to return a specified number of rows from the end of a Series. The method returns a brand new Series</td>
    </tr>
    <tr>
      <td>
        <strong>le()</strong>
      </td>
      <td>Used to compare every element of Caller series with passed series.It returns True for every element which is Less than or Equal to the element in passed series</td>
    </tr>
    <tr>
      <td>
        <strong>ne()</strong>
      </td>
      <td>Used to compare every element of Caller series with passed series. It returns True for every element which is Not Equal to the element in passed series</td>
    </tr>
    <tr>
      <td>
        <strong>ge()</strong>
      </td>
      <td>Used to compare every element of Caller series with passed series. It returns True for every element which is Greater than or Equal to the element in passed series</td>
    </tr>
    <tr>
      <td>
        <strong>
          eq()
        </strong>
      </td>
      <td>Used to compare every element of Caller series with passed series. It returns True for every element which is Equal to the element in passed series</td>
    </tr>
    <tr>
      <td>
        <strong>
          gt()
        </strong>
      </td>
      <td>Used to compare two series and return Boolean value for every respective element</td>
    </tr>
    <tr>
      <td>
        <strong>
          lt()
        </strong>
      </td>
      <td>Used to compare two series and return Boolean value for every respective element</td>
    </tr>
    <tr>
      <td>
        <strong>
          clip()
        </strong>
      </td>
      <td>Used to clip value below and above to passed Least and Max value</td>
    </tr>
    <tr>
      <td>
        <strong>
          clip_lower()
        </strong>
      </td>
      <td>Used to clip values below a passed least value</td>
    </tr>
    <tr>
      <td>
        <strong>
          clip_upper()
        </strong>
      </td>
      <td>Used to clip values above a passed maximum value</td>
    </tr>
    <tr>
      <td>
        <strong>
          astype()
        </strong>
      </td>
      <td>Method is used to change data type of a series</td>
    </tr>
    <tr>
      <td>
        <strong>
          tolist()
        </strong>
      </td>
      <td>Method is used to convert a series to list</td>
    </tr>
    <tr>
      <td>
        <strong>get()</strong>
      </td>
      <td>Method is called on a Series to extract values from a Series. This is alternative syntax to the traditional bracket syntax</td>
    </tr>
    <tr>
      <td>
        <strong>
          unique()
        </strong>
      </td>
      <td>Pandas unique() is used to see the unique values in a particular column</td>
    </tr>
    <tr>
      <td>
        <strong>
          nunique()
        </strong>
      </td>
      <td>Pandas nunique() is used to get a count of unique values</td>
    </tr>
    <tr>
      <td>
        <strong>value_counts()</strong>
      </td>
      <td>Method to count the number of the times each unique value occurs in a Series</td>
    </tr>
    <tr>
      <td>
        <strong>
          factorize()
        </strong>
      </td>
      <td>Method helps to get the numeric representation of an array by identifying distinct values</td>
    </tr>
    <tr>
      <td>
        <strong>map()</strong>
      </td>
      <td>Method to tie together the values from one object to another</td>
    </tr>
    <tr>
      <td>
        <strong>between()</strong>
      </td>
      <td>Pandas between() method is used on series to check which values lie between first and second argument</td>
    </tr>
    <tr>
      <td>
        <strong>apply()</strong>
      </td>
      <td>Method is called and feeded a Python function as an argument to use the function on every Series value. This method is helpful for executing custom operations that are not included in pandas or numpy</td>
    </tr>
  </tbody>
</table>

# Binary operation methods on series:
<table>
    <tbody>
        <tr>
            <th>Function</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><strong>add()</strong></td>
            <td>Method is used to add series or list like objects with same length to the caller series</td>
        </tr>
        <tr>
            <td><strong>sub()</strong></td>
            <td>Method is used to subtract series or list like objects with same length from the caller series</td>
        </tr>
        <tr>
            <td><strong>mul()</strong></td>
            <td>Method is used to multiply series or list like objects with same length with the caller series</td>
        </tr>
        <tr>
            <td><strong>div()</strong></td>
            <td>Method is used to divide series or list like objects with same length by the caller series</td>
        </tr>
        <tr>
            <td><strong>sum()</strong></td>
            <td>Returns the sum of the values for the requested axis</td>
        </tr>
        <tr>
            <td><strong>prod()</strong></td>
            <td>Returns the product of the values for the requested axis</td>
        </tr>
        <tr>
            <td><strong>mean()</strong></td>
            <td>Returns the mean of the values for the requested axis</td>
        </tr>
        <tr>
            <td><strong>pow()</strong></td>
            <td>Method is used to put each element of passed series as exponential power of caller series and returned the results</td>
        </tr>
        <tr>
            <td><strong>abs()</strong></td>
            <td>Method is used to get the absolute numeric value of each element in Series/DataFrame</td>
        </tr>
        <tr>
            <td><strong>cov()</strong></td>
            <td>Method is used to find covariance of two series</td>
        </tr>
    </tbody>
</table>

