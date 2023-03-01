import streamlit as st


def basic_syntax():
    st.header("SQL Basic Syntax")
    st.write(
        """
    
        This section covers basic SQL syntax.   
    
    """
    )
    st.write("")
    st.write("")

    with st.expander("Alter Table Clause"):
        st.write(
            """
              The ALTER TABLE clause is a SQL command used to modify the structure of an existing table 
              in a database. It allows you to add, delete or modify columns, change the data type of a 
              column, rename a table or a column, add or drop constraints, and perform other modifications
              to the table's structure.

              Example
              ```
              ALTER TABLE table_name action statement
              ALTER TABLE table_name ADD column_name data_type;

              ```

            """
        )
        

    with st.expander("Beetween Operator"):
        st.write(
            """   
            The BETWEEN clause is a SQL operator that allows you to select values within 
            a range of values. It is commonly used in SQL queries to filter data based on 
            a specified range of values.

            Example:

            ```
            SELECT column_name(s) 
            FROM table_name 
            WHERE column_name BETWEEN value1 AND value2;
            ```

            """
        )

    with st.expander("Table Schema"):
        st.write(
            """
        
                
            """
        )

    
