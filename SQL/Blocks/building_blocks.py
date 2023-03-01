import streamlit as st


def building_blocks():
    st.header("Database Basic Building Blocks")
    st.write(
        """
    
        This section covers basic Database building blocks.   
    
    """
    )
    st.write("")
    st.write("")

    with st.expander("Data Typese"):
        st.write(
            """
            Most databases support the following built-in data types:

            * Integer - used for whole numbers (smallint, int, numeric ...)
            * Decimal/Float - used for decimal numbers with fractional parts (float, float8...)
            * Char/Varchar - used for storing strings of text
            * Date/Time - used for storing dates and times (date, time, timestamp, interval...)
            * Boolean - used for storing true/false values
            * Blob - used for storing binary data such as images or multimedia files.  
            
            The are many more other datatypes depending on specific database management system.
        """
        )
        

    with st.expander("Basic terminology"):
        st.write(
            """    

            * Tables - a collection of related data organized in rows and columns.
              Tables are the most common type of entity in a database, and they represent 
              the basic unit of storage for data.

            * Relationships - the way in which tables are linked to each other in a database. 
              Relationships can be one-to-one, one-to-many, or many-to-many, and they allow data 
              from different tables to be accessed and combined as needed.

            * Attributes - the characteristics or properties of an entity. Each attribute corresponds 
              to a column in a table, and it represents a specific type of data that can be stored in 
              the table.

            * Keys - a field or combination of fields in a table that uniquely identifies each record in 
              the table. Keys are used to ensure data integrity and to link records between tables.

            * Indexes - a data structure that improves the speed of data retrieval by providing quick 
              access to specific records in a table. Indexes are created on one or more columns of a table, and they can greatly improve the performance of large databases.

            * Views - a virtual table that is created by combining data from one or more tables in a 
              database. Views are used to simplify data access and to hide the complexity of the 
              underlying data model from end-users.
            

        """
        )

    with st.expander("Table Schema"):
        st.write(
            """
        
                A table schema, also known as a database schema or simply a schema, 
                is a logical structure that defines the organization of data in a database. 
                It defines the structure of the tables, the relationships between tables, and the 
                rules that govern the storage and retrieval of data.

                A table schema typically includes information such as the table name, 
                the column names and data types, the primary key and foreign key constraints, 
                and any indexes or other database objects associated with the table.

                In general, a well-designed table schema can improve the efficiency, 
                scalability, and maintainability of a database. It can also help to ensure 
                data integrity and consistency by enforcing constraints on the data that is 
                stored in the database.

        """
        )

    
