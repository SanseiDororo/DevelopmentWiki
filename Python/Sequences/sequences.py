import streamlit as st

s = "This is a string"
series = "Monthy Python"
langauage = "Python"


def sequences():
    st.header("Sequences")
    st.write("")
    st.write(
        """
            This section covers most important aspects of specific type of containers
            called sequences.  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Types"):
        st.write(
            """

            We have three types of sequences in Python: tuples, lists and strings.
            They share most of the attributes, but they have idiosycratic purpose
            as well. This is overall atributtes list:
            
            |  Tuples       | Lists                  | Strings                   | 
            |---------------|------------------------|---------------------------|
            | indexable     | indexable              | indexable                 |       
            | homo / hetero | homo / hetero          | homogeneous               |    
            | iterable      | iterable               | iterable                  |    
            | indexable     | indexable              | indexable                 | 
            | immutable     | mutable                | mutable                   |                      
            | fixed length  | arbitrary length       | fixed length              |                      
            | fixed order   | arbitrary order        | fixed order               |
            

            """
        )

    with st.expander("Strings"):
        st.write(
            f"""
            
            Strings are mutable indexable and iterable sequences. They maintain left to right order.
            Strings can represent various types of data from characters to byte arrays and similar.
            There are several built in methods for dealing with strings.

            1. SEQUENCE OPERATIONS

                s = "This is a string"                
                
                * Check the length of the string
                   
                    len(s) = {len(s)}

                * Retrieve the first and the last item
                
                    s[0] = {s[0]}

                    s[-1] = {s[-1]}

                * Retrieve all characters past third
                
                    s[2:] = {s[2:]}

                * Replace specific part

                    s.replace('This', 'That') = {s.replace('This', 'That')}

                * Make characters upper

                    s.upper = {s.upper()}

                * Split on delimeter into a list of substrings

                    s.split(' ') = {s.split(' ')}

            2. STRING FORMATTING

                Python offers various ways for formatting strings. 
                
                * C like

                '%s was named after %s' % ('Python', 'Monthy Python') = {'%s was named after %s' % ('Python', 'Monthy Python')}

                * .format

                {r'{} was named after {}'}.format('Monthy', 'Monthy Python') = {'{} was named after {})'.format('Monthy', 'Monthy Python')}) 

                * F string

                By putting f before a string we can inject python variables, operations etc into strings, separating the items with the curly
                brackets.

                * Number formating

                2.946263:.2f = {2.946263:.2f}
                

                
                
                More practical examples can be found here:

                [Python String formatting](https://pyformat.info/)

            """
        )

    with st.expander("Tuples"):
        st.write(
            """
            Tuples are immutable containers of elements with non-arbitrary positional relevance.
            They can be homogeneous (storing elements of the same type) or heterogeneous
            (storing elements of a different types). Content of a tuple is iterable. 

            According to the non-arbitrary relevance of the elements in the tuple, they are very
            useful for storing various types of data.

            For example:

            * 2D coordinates (x: x axis, y: y axis, z: z axis)
            * Entities (person: name, surname, age | city: name, country, population)

                    #Packing variables into tuple:
                    philosopher = 'Jeremy', 'Bentham', 'Utilitarist'

                    #Unpacking tuple values:
                    name, age, occupation = philosopher

            [Example](https://colab.research.google.com/drive/17nVp9YrOiehbJY64r5G4x5n-E-uK8cYX?usp=sharing)
            """
        )
