import streamlit as st


def polars():
    st.header("Polars")
    st.write("")
    st.write(
        """
            Polars is Python library designed for data analysis and manipulation. 
            It is written in Rust and utilises Apache Arrow for the maximum performance.
            Python API on top allows seamingless operations and familiar ways to perform
            various operations. Polars are much more efficient than Pandas and provide
            more pythonistic approach to tabular data manipulation.  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Basics"):
        st.write(
            """
                IMPORT DECLARATION

                ```import polars as pd```
                
                CONFIGURATION

                Polars provide Config method through which, we can define several 
                configurations for polars, such as formatting floats, table row numbers
                and others. 
                
                ```pl.Config.set_table_rows```


                READING CSV FILE
                
                ```
                df_to_store = pl.read_csv('file.csv')

                Lazy mode in Polars defers the execution of operations until the results are actually needed. 
                This approach contrasts with the eager execution mode, where each operation is executed 
                immediately. Lazy evaluation can significantly optimize the performance of data processing tasks.
                
                ```

                READ IN LAZY MODE
                
                ```
                (
                    pl.scan_csv(csv_file.csv)
                )
                ```
                QUERY OPTIMISATION

                Polars provides us optimised query plan throught the explain() method.

                ```
                print(
                    pl.scan_csv(csv_file)
                    .group_by(["col1","col1"])
                    .agg(
                        pl.col("col3").count().alias("count")
                    )
                    .explain()
                )
                ```

                STREAMING DATA

                If the data object is larger than the memory size, polars provide data streaming option

                ```
                    (
                        pl.scan_csv(csv_file)
                        .filter(pl.col("ColName") > 50)
                        .group_by(["Col 1","Col 2"])
                        .agg(
                            pl.col("Col 1").count().alias("count")
                        )
                        .collect(streaming = True)
                    )
                ```

                DROPPING COLUMNS

                ```
                    df.drop(["col1", "col2"])
                ```

                CHANGING DATA TYPES

                ```
                    (
                        df
                        .cast(
                            {
                                cs.numeric():pl.Utf8
                            }
                        )
                        .head(2)
                    )
                ```

            """
        )

    with st.expander("Data Inspection"):
        st.write(
            """
                Some of the most common data inspection operations we perform on the data frame
                are:

                DATAFRAME OVERVIEW
                ```
                    df = pl.read_csv("csv_file.csv")

                    df.glimpse()
                    df.describe()
                    df.schema
                ```
                
                RENAMING COLUMN
                ```
                    df.rename({"ColumnOne":"Column_1"})
                ```

                INSPECTING THE SHAPE OF THE DATAFRAME
                ```
                    df.width
                    df.height
                ```

                CHECKING DATATYPES OF VALUES
                ```
                    df.dtype
                    df.["ColumnName"].dtype
                ```

                SUPERTYPES

                Polars also introduces the concept of supertypes. Supertypes come 
                into play when performing operations on columns with differing data types. 
                If these columns share a common supertype, they are cast to that supertype 
                to enable the operation.

                We can group the dtypes into groups:

                * integers e.g. pl.Int8,pl.Int16 etc
                * floats pl.Float32,pl.Float64
                * string pl.Utf8
                * boolean pl.Boolean
                * datetime pl.Datetime,pl.Date etc

                Supertypes are defined on a given pair of dtypes rather than being universal. Here are some simple examples:

                pl.Int8 & pl.Int16 -> pl.Int16
                pl.Float32 & pl.Float64 -> pl.Float64
                There are also rules in place for other combinations e.g.:

                pl.Int64 & pl.Boolean -> pl.Boolean
                pl.Int32 & pl.Float32 -> pl.Float64 (following a convention set by Numpy)
                any dtype & pl.Utf8 -> pl.Utf8 (any column can be cast to string)

                APACHE ARROW

                While pandas utilises numpy arrays to represent tabular data, Polars utilises 
                Apache Arrow Table. We can see this arrow by calling:

                ```
                    df.to_arrow()
                ```

            """
        )
    
    with st.expander("Importing Data"):
        st.write(
            """
            Importing messy data is the most common task. We first need
            to consolidate the data set before we can start deriving valuable information.

            We can import data from various sources: csv, excel, html. The methods are

            *  pl.read_csv("data.csv", separator="|")
            *  pl.read_excel('')
            *  pl.read_database('')   


            SKIPPING ROWS & DELETING UNWANTED ENTRIES

            ```pl.read_csv('filename.csv', skiprows = n)```


            """
        )    

    with st.expander("Dataframe Inspection"):
        st.write(
            """
            
                1.Get first ten rows
                
                ```df.head(n=10)```

                2.Get last 5 rows
                
                ```df.tail(n=5)```

                3.Gather aggregated data about the Dataframe

                ```df.describe()```

                4. Discover shape of the data DataFrame
                
                ```df.shape (returns number of rows and colums)```

            """
        )

    with st.expander("Selecting"):
        st.write(
            """
            
            FETCHING THE COLUMN

            ```
                df.["column_name"]

                (
                    df
                    .select(
                        pl.col("Age")
                    )
                )

            ```

            Returning first row
            ```
            df[0] 
            ```
            Returning value of the second column of row 1
            
            ```
            df[0,1]  
            ```
            

            ```
            Returns series of records from 0 to 10 and columns 1, 3, 4
            
            df[:10, [0,2,3]]  
            ``` 
            
            RENAMING COLUMN NAMES
            
            ```
            df.rename({"column1":"c1", "column2":"c2", "column3":"c3", "column3":"c3"})
            ```
            
            NUMERIC INDEXING

            ```
                df[:, 1:6].head(2)
            ```

            SELECTING WITH SELECT METHOD

            ```
                (
                    df
                    .select('Age')
                    #If we want to chage to series, we can add
                    .to_series()
                    .head(3)
                )
            ```

            SELECTING MULTIPLE ROWS AND PERFORMIN OPERATIONS ON THEM
            ```
            (
                df
                .select(
                    pl.col('Fare'),
                    pl.col('Fare').round(0).alias('roundedFare')
                )
                .head(3)
            )
            ```

            SOME ADDITIONAL METHODS IN THE CONTEXT OF .SELECT

            * pl.all()
            * pl.exclude([])
            * pl.max()

            POLARS PROVIDE SELECTOR API AS WELL

            ```
            (
                df
                .select(
                    cs.all()
                )
                .head(3)
            )
            ```

            ADDITIONAL METHODS
            
            * cs.numeric()
            * cs.by_name("col1", "col1")
            * cs.starts_with()
            * cs.mathes()
            * cs.string()

            CHECKING NUMBER OF UNIQUE VALUES

            ```
            df.n_unique()
            ```

            """
        ) 
    
    with st.expander("Statistics"):
        st.write(
            """
            
               DATAFRAME METHODS

                Returns basic statistics 
                
                ```df.describe()```  

                Basic statistics with percentiles
                ```df.describe(percentiles=(0.1,0.3,0.5,0.7,0.9))```       
                
               CALCULATING STATISTICS IN EXPRESSION
               
               ```
                (
                    df
                    .select(
                        pl.col('Fare').mean()
                    )
                )
               ```

                AVAILABLE METHODS


                * count
                * sum
                * product
                * min
                * median
                * mean
                * max
                * std (standard deviation)
                * var (variance)
                * skew
                * kurtosis
                * entropy

            --------------------------
               VALUE COUNTS

               ```
                df["Col"].value_counts()
                df["Col"].value_counts(sort=True)
                df["Col"].value_counts().sort("Col2")
               ```
            """
        )
    
    with st.expander("Series"):
        st.write(
            """
            
            PANDAS SERIES

            Pandas series is one-dimensional labeled array capable of holding data of any type.

            Example data frame

            |index | column1 | column2 | column2  |
            |------|---------|---------|--------- |
            |row 1 | value   | value   | value    |
            |row 2 | value   | value   | value    |
            |row 3 | value   | value   | value    |
            |row 4 | value   | value   | value    |

            
            CREATING PANDAS SERIES

            To create a series, we can isolate the values of a column and store it in the df.

            ```column1_values = df.column1.copy()```

            WE CAN EXECUTE METHODS IN ORDER TO GATHER BASIC STATISTICS.

            ```column1_values.describe()```


            VALUE COUNT METHOD

            column1_values.value_counts()


            GET RELATIVE FREQUENCES

            ```column1_values.value_counts(normalize = True)```


            SORT VALUES

            ```column1_values.sort_values()```
            
            arguments 
            
            *ascending: defines the order

            *inplace: defines if the result is stored in new df or not

            
            GET MAX VALUE IN THE INTEGER BASED SERIES
            
            ```column1_values.max()```


            Creating new pandas series from existing one

            ```new_series = (column1_values / 2)```


            Get unique values

            ```new_series.unique()```

            GET THE LARGEST AND SMALLEST VALUE

            retrieves the largest value of the series in ascending order
            
            ```dataset.nlargest(ascending=True)``` 

            We can stack methods

            ```
            #returns first 3
            
            datase.nlargest(ascending=True).head(3) 

            #returns 5 smallest values
            
            datase.nsmallest(ascending=True, n = 5) 
                
            ```
 


            """
        )

    with st.expander("Sorting"):
        st.write(
            """
                Sorting in polars can be performed with .sort() method

                EXAMPLE

                ```
                    df.sort("colm")

                ```

                PUTTING NULLS ON THE BOTTOM

                ```
                    df.sort("Col",nulls_last=True)
                
                ```

                SORTING IN REVERSE

                ```
                    df.sort("Col",descending=True)
                ```

                SORT ON MULTIPLE COLUMNS

                ```
                    df.sort(["Col1","Col2"])
                ```

                SORTING WITH EXPRESSION

                ```
                    (
                        df
                        .select(
                            pl.all().sort_by("Age")
                        )
                    )
                ```







            """
        ) 


    with st.expander("Quantiles & Bining"):
        st.write(
            """
                CREATING QUANTILES FOR A DATA SERIES

                ```
                    quantile_list = [0.1,0.5,0.9]
                    (
                        df
                        .select(
                            [
                                pl.col('Age').quantile(q).alias(f"Age_quantile_{q}") for q in quantile_list
                            ]
                        )
                    )
                ```

                PLOTTING BINS

                ```
                (
                    df
                    ["Age"]
                    .plot
                    .hist(bins=50)
                )
                ```
            
       
            """
        )  


    with st.expander("Custom Functions"):
        st.write(
            """
            CUSTOM FUNCTIONS 

            In polars we can execute custom functions via .pipe method

            ```
                def lowercase(df):
                    return (
                        df
                        .with_columns(
                            pl.col(pl.Utf8).str.to_lowercase()
                        )
                    )

                (
                    df
                    .pipe(lowercase)
                )
            ```

            """
        )  

    with st.expander("Filtering"):
        st.write(
            """
            
            FILTERING DATA

            Polars have different approach to filtering than Pandas which uses masks
            and other tricks. With Polars filtering is much more straight forward.

            SELECTING ROWS
            
            ```df[0]```

            SELECTING MULTIPLE ROWS

            ```df[[2,3]]```

            SLICING

            ```df[:2]```

            For data slicing there is .slice method provided as well

            ```
            (
                df
                .slice(0,4)
            )
            ```

            RANGE

            ```df[range(2,4)]```

            FILTERING WITH CONDITION

            ```
                (
                    df
                    .filter(
                        pl.col('Pclass') == 1
                    )
                    .head(2)
                )
            ```

            CONDITION AND PARTIAL DATA

            ```
                (
                    df
                    .filter(
                        pl.col('Parch').gt(1)
                    )
                    .select("PassengerId","Parch","SibSp")
                    .head(5)
                )
            ```

            FILTERING AND SORTING WITH CONTEXT MANAGER COLUMNS
            ```
            (
                df
                .with_columns(
                    age_below_30 = pl.col("Age") < 30
                )
                .filter(
                    pl.col("age_below_30")
                )
            )
            ```

            MULTICONDITIONAL FILTERING

            ```
                (
                    df
                    .filter(
                        (pl.col('Age') > 70) & (pl.col('Pclass') == 1)
                    )
                    .head(2)
                )

                OR

                (
                    df
                    .filter(
                        pl.col("Pclass") == 1,
                        pl.col("Age") > 70
                    )
                    .head(2)
                )
            ```

            """
        )  

    with st.expander("Grouping"):
        st.write(
            """
            Group by operation is very useful and important 
            in the data analysis process, since it returns aggregated data

            ```
            (
                df
                .group_by("Col")
                #Additiona aggregation functions
                .agg(
                    pl.col("Fare").mean()
                )
            )
            ```

            The methods we can all on GroupBy include:

            * first get the first element of each group
            * last get the last element of each group
            * n_unique get the number of unique elements in each group
            * count get the number of elements in each group
            * sum sum the elements in each group
            * min get the smallest element in each group
            * max get the largest element in each group
            * mean get the average of elements in each group
            * median get the median in each group
            * quantile calculate quantiles in each group
            """
        ) 
    with st.expander("Merging"):
        st.write(
            """
            We use three methods in order to merge dataframes:

            * vstack
            * rechunk
            * concat


            """
        )  

    with st.expander("Pivoting & Reshaping"):
        st.write(
            """
            For Pivoting we use .pivot method

            ```
            (
                df
                .pivot(
                    index='col1', 
                    columns='col2', 
                    values='values'
                )
            )
            ```
            """
        )  

    with st.expander("Visualisation & Plotting"):
        st.write(
            """
            Polars doesn't have built-in plotting features but relies heavily on hvplot.

            (hvplot documentation)["https://hvplot.holoviz.org/reference/index.html"]

            Other most popular options such as

            * Plotly
            * Altair
            * Matplotlib

            and others, are supported as well.


            """
        )      