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

    with st.expander("CREATE TABLE"):
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

    with st.expander("ALTER TABLE"):
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
        

    with st.expander("DELETE"):
        st.write(
            """
            The DELETE clause in SQL is used to delete one or more rows from a table. 
            It is commonly used to remove old or unwanted data from a database or to correct errors 
            in existing data.

            Example:

            ```
            DELETE FROM table_name WHERE condition;
            ```

            To delete table or database, we use DROP command

            ```
            DROB table table_name;
            DROP DATABASE database_name;
            ```

            """
        )

    with st.expander("SELECT"):
        st.write(
            """   
            SELECT is a SQL statement used to retrieve data from one or more tables 
            in a database. It is one of the most commonly used statements in SQL and is 
            used to retrieve data for reporting, analysis, or other purposes.

            Example:

            ```
            SELECT column1, column2, ... columnN FROM table_name;

            ```

            """
        )
    with st.expander("BETWEEN"):
        st.write(
            """   
            CREATE TABLE is a SQL statement used to create a new table in a database. 
            It specifies the table's name, the columns it will contain, and the data 
            type of each column.

            Example:

            ```
            CREATE TABLE table_name (
            column1 datatype PRIMARY KEY,
            column2 datatype [optional_parameters],
            columnn datatype [optional_parameters],
            );
            ```

            ```
            CREATE TABLE users (
            id INT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE,
            age INT
            );
            ```

            """
        )

    with st.expander("COUNT"):
        st.write(
            """
            COUNT is a SQL aggregate function used to count the number of rows that meet 
            a specified condition in a table. It is commonly used in SQL queries to calculate 
            the number of records in a table or the number of records that meet certain criteria.

            Example:

            ```
            SELECT COUNT(*) 
            FROM users 
            WHERE age >= 18;
            ```
                
            """
        )

    
