# Python NumPy
NumPy is a general-purpose array processing package which provides tools for handling the n-dimensional arrays.

#
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called <b>ndarray</b>, it provides a lot of supporting functions that make working with ndarray very easy.

#
NumPy’s main object is the homogeneous multidimensional array.
It is a table of elements, all of the same type, indexed by a tuple of positive integers.
<b>In NumPy, dimensions are called axes. The number of axes is rank.</b>
An array can have any number of dimensions. When the array is created, you can define the number of dimensions by using the <b>ndmin</b> argument.

<p>
For example, the array for the coordinates of a point in 3D space, [1, 2, 1], has one axis. That axis has 3 elements in it, so we say it has a length of 3. 

In the example below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.

[[1., 0., 0.],
 [0., 1., 2.]]
</p>

# NumPy Creating Arrays
We can create a NumPy ndarray object by using the <b>array() function</b>

# Access Array Elements
We can access an array element by referring to its index number. The indexes in NumPy arrays start with 0.</br>
To access elements from n-D arrays we can use comma separated integers representing the dimension and the index of the element.
Think of n-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.</br>
Use negative indexing to access an array from the <b>end</b>.

# Slicing arrays
<p>
Slicing in python means taking elements from one given index to another given index.</br>
We pass slice instead of index like this: <label style="color:blue;">[start:end].</label></br>
We can also define the step, like this: <label style="color:blue;">[start:end:step].</label></br>
If we don't pass start its considered 0</br>
If we don't pass end its considered length of array in that dimension</br>
If we don't pass step its considered 1</br>
</p>


# Data Types in NumPy
NumPy refer to data types with one character, like i for integers, u for unsigned integers etc.
<p>
The NumPy array object has a property called <b>dtype</b> that returns the data type of the array.</br>
Below is a list of all data types in NumPy and the characters used to represent them.
<ul>
    <li>i - integer</li>
    <li>b - boolean</li>
    <li>u - unsigned integer</li>
    <li>f - float</li>
    <li>c - complex float</li>
    <li>m - timedelta</li>
    <li>M - datetime</li>
    <li>O - object</li>
    <li>S - string</li>
    <li>U - unicode string</li>
    <li>V - fixed chunk of memory for other type ( void )</li>
</ul>
</p>

# Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.