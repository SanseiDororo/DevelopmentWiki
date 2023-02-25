import streamlit as st



def numpy():
    st.header("Numpy")
    st.write("")
    st.write(
        """
            NumPy is a powerful library for working with numerical data in Python. 
            It provides a wide range of functions and methods that allow you to manipulate 
            and analyze numerical data with ease.

            NumPy is particularly useful for working with large, multi-dimensional arrays of data. It provides a high-performance multidimensional array object, as well as tools for working with these arrays. This makes NumPy a useful tool for scientific computing, machine learning, and other fields that involve large amounts of numerical data.  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("DataTypes & Attributes"):
        st.write(
            """
                Numpy main object is ndarray which stands for n-dimensional array.

                Lists can be converted into ndarray with the np.array function.

                ```
                #CHANGING PYTHON LIST INTO ARRAY
                l = list(range(1,11)) 

                Change list into numpy array container

                array = np.array(l)

                ```

            """
        )

    with st.expander("Arrays"):
        st.write(
            """
                There are numerous ways to create arrays with numpy.

                Create arrays of zeros or ones:

                ```
                #Zeros array
                np.zeros([2,3])
                
                #Ones array
                np.ones([3,2])

                #Range array
                np.arange(start,stop,step)

                #Random array
                random_array = np.random.randint(1,25, size=(2,2))
                ```

                Numpy array contains only one data type and this is the major difference 
                between ordinary python lists and np arrays.

                To check what kind of data np array stores, we use:

                ```
                array.dtype
                ``` 

            """
        )

    with st.expander("Random"):
        st.write(
            """
                Numpy provides several methods for generating random numbers.

                The key for creating random numbers is defined by the seed.

                ```
                np.random.seed()

                ```
                To create random array of any shape, we can use

                ```
                np.random.random()

                ```

                To find unique values in array, we can use

                ```
                np.unique('given array')
                ```
                

            """
        )

    with st.expander("Matrices"):
        st.write(
            """
                One dimensional array is refered as a vector, while arrays of
                higher dimensions are refered as matrices.

                We can retrieve elements in matrices by indexing.

                ```
                array[0] => returns first row
                array[0][0] => returns first element of the first row
                array[:1,:1] => returns first element of the first row
                array[:3,:1] => returns first element for the first three rows
                ```

                

            """
        )
    with st.expander("Manipulation"):
        st.write(
            """
                Numpy allows vector operations. We can perform
                arithmetic operations for given n dimensional arrays.

                ```
                a_one = [1,2,3]
                a_ones = [1,1,1]

                a_one + a_ones = [2,3,4]
                a_one - a_ones = [0,2,3]

                #Squaring all the numbers
                np.square(a_one) = [1,4,9]

                ``` 

                When performing arithmetic operations on n dimensional array numpy uses
                broadcasting. It is extremely important to understand associated limitations.
                
                [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
                [Supported Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)

            """
        )

    with st.expander("Aggregation"):
        st.write(
            """
                Numpy provides several functions to aggreate items in n dimensional array.

                * np.sum() = sums items in array 
                * np.mean() = finds mean of the items in array
                * np.max() = finds item with max value in array
                * np.min() = finds item with minimal value in array
                * np.std() = finds standard deviation in array
                * np.var() = difference between numbers in array

                Standard deviation = square root of variance
                Standard deviation and variance are measurements for spread of data.
                
                Standard deviation is a statistical measure that describes how spread out a set of data is. It is calculated by taking the square root of the variance, which is the average of the squared differences from the mean.

                To calculate the standard deviation of a set of data, you first need to 
                calculate the mean, or average, of the data. Then, for each data point, 
                you subtract the mean and square the result. Finally, you take the average 
                    of these squared differences and take the square root of the result.
            """
        )
    with st.expander("Reshape & Transpose"):
        st.write(
            """
                Numpy provides functions to manipulate the shape of the n dimensional arrays.

                We can reshape array with:
                ```
                example = [3,2]
                example.reshape(3,2,1) 
                ```

                Transpose switch axisis.

                ```
                example.T
                ```
            """
        )

   