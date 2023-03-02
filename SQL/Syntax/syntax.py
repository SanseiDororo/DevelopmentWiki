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

    with st.expander("INSERT"):
        st.write(
            """
            Inserting data into a table is done with the INSERT clause which must follow
            the provided table schema, since otherwise engine will return an error.

            Example:

            ```
            INSERT INTO table_name (column1, column2...) 
            VALUES (value1, value2...);
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

    with st.expander("GROUP BY"):
        st.write(
            """
            GROUP BY clause in SQL is used to group rows with the same values 
            in one or more columns into summary rows, such as the total or average 
            of the values in another column. It is often used with aggregate functions 
            such as SUM, COUNT, AVG, MIN, and MAX.



            Example:

            ```
            SELECT column1, column2, aggregate_function(column3)
            FROM table_name
            WHERE condition
            GROUP BY column1, column2;
            ```
                
            """
        )

    with st.expander("HAVING"):
        st.write(
            """
            The HAVING clause is a clause in SQL that is used to filter the results of 
            a query based on a condition that applies to groups of rows. It is used in 
            conjunction with the GROUP BY clause to perform aggregate functions on the grouped 
            data and filter the results based on the results of those aggregate functions

            Example:

            ```
            SELECT column1, aggregate_function(column2)
            FROM table_name
            WHERE condition
            GROUP BY column1
            HAVING condition;

            ```

            ```
            SELECT product_name, SUM(sales_amount) AS total_sales
            FROM sales
            GROUP BY product_name
            HAVING SUM(sales_amount) > 1000;

            ```
                
            """
        )

    with st.expander("IN"):
        st.write(
            """
            The IN clause in SQL is used to specify a list of values to be matched in a
            WHERE clause or subquery. It allows you to retrieve rows that match any of 
            the values in the list.

            Example:

            ```
            SELECT column_name(s)
            FROM table_name
            WHERE column_name IN (value1, value2, ...);
            ```

            ```
            SELECT name, age
            FROM employees
            WHERE department_id IN (SELECT department_id FROM departments WHERE budget > 1000000);

            ```
                
            """
        )
  
    with st.expander("LIKE"):
        st.write(
            """
            In SQL, the LIKE clause is used to search for specific patterns in a column of text data. 
            It is often used in conjunction with the SELECT statement to filter rows based on certain 
            criteria.

            Example:

            ```
            SELECT column1, column2, ...
            FROM table_name
            WHERE column_name LIKE pattern;

            ```

            The pattern can contain wildcard characters that represent any character or set of 
            characters. The most commonly used wildcard characters are:

            * %: represents any sequence of zero or more characters
            * _: represents any single character

            ```
            SELECT * FROM customers
            WHERE customer_name LIKE 'J%';

            ```

            """
        )

    with st.expander("LIMIT"):
        st.write(
            """
            Limit clause in SQL limits the size of the output

            Example:

            ```
            SELECT column1, column2, ...
            FROM table_name
            LIMIT 5;

            ```
            This will limit the out to first 5 results
            """
        )

    with st.expander("ORDER BY"):
        st.write(
            """
            ORDER BY clause is used to sort the result set of a query in either 
            ascending or descending order based on one or more columns. 
            It is often used in conjunction with the SELECT statement to order the output of a query.
            
            Example:

            ```
            SELECT column1, column2, ...
            FROM table_name
            ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;

            ```

            """
        )    
    with st.expander("AGGREGATION FUNCTIONS"):
        st.write(
            """
            Aggregation functions are used to aggregate data. Mostly used are

            * AVG = returns average
            * MIN = returns minimum
            * MAX = maximum 
            * SUM = sum
            
            Example:

            ```
            SELECT AVG (column1) FROM table_name;

            ```

            """
        ) 

    with st.expander("CHECK CONSTRAINT"):
        st.write(
            """
            Check constraint sets the rule for the data input. For example, when we create the table
            we can set the constraint like this:

            Example:

            ```
            CREATE TABLE test (birth_date DATE 
            CHECK (birth_date > '1950-01-01'));

            ```

            """
        ) 

    with st.expander("CHECK CONSTRAINT"):
        st.write(
            """
            Check constraint sets the rule for the data input. For example, when we create the table
            we can set the constraint like this:

            Example:

            ```
            CREATE TABLE test (birth_date DATE 
            CHECK (birth_date > '1950-01-01'));

            ```

            """
        ) 

    with st.expander("UNION"):
        st.write(
            """
            In SQL, the UNION clause is used to combine the results of two 
            or more SELECT statements into a single result set. It is often 
            used to retrieve data from two or more tables with similar structures.

            Example:

            ```
            SELECT column1, column2, ...
            FROM table1
            WHERE condition
            UNION [ALL]
            SELECT column1, column2, ...
            FROM table2
            WHERE condition;

            ```

            """
        ) 

    with st.expander("UPDATE"):
        st.write(
            """
            Update clause is used to update the data in the table.

            Example:

            ```
            UPDATE table_name
            SET column1 = value1,
            column2 = value2;

            ```

            """
        ) 

    with st.expander("VIEW"):
        st.write(
            """
            A view is database object which is of a stored query type. It can be accessed as a
            virtual table since it is like a logical table that represents the data of one or more
            underlying tables.

            Example:

            ```
            #CREATE VIEW
            CREATE VIEW view_name AS query;
            ```

            ```
            #DELETE VIEW
            DROP VIEW view name;
            ```

            """
        ) 

    with st.expander("CHECK CONSTRAINT"):
        st.write(
            """
            Check constraint sets the rule for the data input. For example, when we create the table
            we can set the constraint like this:

            Example:

            ```
            CREATE TABLE test (birth_date DATE 
            CHECK (birth_date > '1950-01-01'));

            ```

            """
        ) 

    with st.expander("UNIQUE CONSTRAINT"):
        st.write(
            """
            Unique constraint is a type of constraint that can be applied to a column or
            a group of columns in a table to ensure that each value in the column(s) is unique, 
            meaning that it does not appear more than once in the table.

            Example:

            ```
            ALTER TABLE table_name
            ADD CONSTRAINT constraint_name UNIQUE (column1, column2, ...);

            ```

            """
        ) 

    with st.expander("JOINS"):
        st.write(
            """
            SQL Joins are used to combine data from two or more tables based on a related 
            column between them. There are several types of SQL Joins:

            1. INNER JOIN 

            An INNER JOIN returns only the rows from both tables that have a matching value 
            in the specified column. It includes only the rows where the joined column matches 
            in both tables.
            
            Example:

            ```
            SELECT table1.column1, table2.column2
            FROM table1
            INNER JOIN table2
            ON table1.columnX = table2.columnX;

            ```

            2. LEFT JOIN

            A LEFT JOIN returns all the rows from the left table and matching rows 
            from the right table, and NULL values for non-matching rows in the right table.

            ```
            SELECT table1.column1, table2.column2
            FROM table1
            RIGHT JOIN table2
            ON table1.columnX = table2.columnX;
            ```

            3.RIGHT JOIN

            A RIGHT JOIN returns all the rows from the right table and matching rows 
            from the left table, and NULL values for non-matching rows in the left table.

            ```
            SELECT table1.column1, table2.column2
            FROM table1
            RIGHT JOIN table2
            ON table1.columnX = table2.columnX;
            ```

            4. FULL OUTER JOIN
            
            A FULL OUTER JOIN returns all the rows from both tables, with NULL values for 
            non-matching rows on both sides.

            ```
            SELECT table1.column1, table2.column2
            FROM table1
            FULL OUTER JOIN table2
            ON table1.columnX = table2.columnX;

            ```

            5. CROSS JOIN

            A CROSS JOIN returns the Cartesian product of the two tables, 
            which means that it returns all possible combinations of rows from both tables.

            ```
            SELECT table1.column1, table2.column2
            FROM table1
            CROSS JOIN table2;

            ```

            """
        ) 