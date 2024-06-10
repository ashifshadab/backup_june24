# Pandas DataFrame describe()

Pandas describe() is used to view some basic statistical details like percentile, mean, std, etc. of a data frame or a series of numeric values. When this method is applied to a series of strings, it returns a different output.

<p>
    <strong style="font-size:20x">
        <span style="color:black;">Syntax:</span> DataFrame.describe(percentiles=None, include=None, exclude=None)
    </strong>
    <div><strong>Parameters: </strong></div>
    <div>
        <ul>
            <li><strong>percentile:</strong> list like data type of numbers between 0-1 to return the respective percentile</li> 
            <li><strong>include:</strong> List of data types to be included while describing dataframe. Default is None</li> 
            <li><strong>exclude:</strong> List of data types to be Excluded while describing dataframe. Default is None </li>
        </ul>
    </div>
    <div><strong>Return type:</strong> Statistical summary of data frame.</div>
    
    
</p>