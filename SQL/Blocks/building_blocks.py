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

    with st.expander("Naming Convections"):
        st.write(
            """
        
            Identifying names in Python are **case-sensitive**. Rules how to use it are precisely
            defined in the [PEP 8](https://peps.python.org/pep-0008/) Style Guide. 

            **CONVENCTIONS**

            * They must star with a letter or the underscore.
            * Can not be reserved words.
            * When identifier starts with the single underscore, 
              it means that it is considered as a _private object.
            * When identifier starts with the double underscore,
              it is used to "mangle" the class attributes.
            * When identifier is enclosed with double underscores,
              it means that is reserved, system-defined name.  
            *

            
            **PEP 8 Style Guides**


            | Entity    | Convection                                            |
            |----------|--------------------------------------------------------|
            | Packages  | Lowercase, short, no underscores                      |
            | Modules   | Lowercase, short, underscores allowed                 |
            | Classes   | Upper CamelCase                                       |
            | Functions | Lowercase, words separated with underscores           |
            | Variables | Same as functions                                     |
            | Constants | Uppercase, words separated with underscore            |
            

            

        """
        )

    with st.expander("Variables"):
        st.write(
            """
        
         Python is dynamically typed langugae meaning that variables are memory references. 
         They point to the certain addresses in the memory.
         When we create the variable age = 19, we create an object in the memory and
         the reference to this object is variable name i.d. age. In the strict sense age is not
         equal to the 19 but only points or references to the specific memory slot, 
         which holds the object 19. With provided libraries we can count references pointing 
         to the certain memory address.
        
        """
        )
        st.write("")
        st.write(
            """
            In Python we can check the memory address for the specific object with
            the id() function.
        """
        )
        memory_input = st.number_input(
            "Please chose the random number", step=1, max_value=100
        )
        st.write(
            f"""
            The memory address for your number is:
            {hex(id(memory_input))}
        
        """
        )
        st.write("")
        st.write(
            """
            **VARIABLE EQUALITY**:

            We can check if two variables are referencing the same memory address
            with the **is** identity operator.

            To check equality of the internal object state we use **==** operator.
            It is important to know that this are two very different things.
        
        """
        )

    with st.expander("Scopes"):
        st.write(
            """
           We could define scope as the level of object availability. Every scope level has it's own
           namespace. In Python there is no true cross module or app global scope. 
           The highest scope level is built-in scope which defines objects such as
           True, False, None, print etc. which are available on every level of Python code.

           Built-in scope encloses modules scopes which have their own namespaces. If Python interpreter
           doesn't find reference to a given object on the level of the given scope it searches in the enclosing scope
           to find it there. If the object doesn't exist in any scope Python returns name error.

           For example: print is a built-in function which means it is stored on the highest 
           level scope. But we can override it on the module level scope by assigning new object to
           the print reference.

            print = lambda x,y: x+y
            print(5,2) => 7 

        Every python file represents it's own scope defined with the namespace of the file, which
        defines __name__ attribute.
           
            import filename
            filename.__name__ => filename

        Functions creates local scopes which get created when the function is called. For example
        variables and operations exists only inside the function or function scope. When function is 
        called this scope is created.

            def local_scope(a):
                print = (a * 10)
                return print

            local_scope('ten') => tententen...

        We can always modify objects on the global level by using the **global** keyword.

            value = 10
            def change_value_globally():
                global value 
                value = 1000

        If we need to modify objects from the level of nested function, we can use **nonlocal** keyword.

            def level_1():
                value = "level1"
                def level_2():
                    nonlocal value
                    value "override level1"
                    print (value)
                level_2()
            
            level_1() will return overrided level1 string.
                    

        Main scopes in Python:

        * Global scope (built-in objects)
        * Module scope (objects inside the module)
        * Local scope (objects inside the functions)
        
        """
        )

    with st.expander("Modules"):
        st.write(
            """
            Modules are instances of the data type Module. They have their own execution space
            associated with the specific namespace. Namespace is defined by the globals() dictionary.
            
            Importmodule('module_name') function from the importlib package takes care for the importing proces.
            When modules are imported they get stored in the sys.module cache. 
            
            Modules get loaded or imported from a file. In general modules represent containers
            of a global variables, which can be checked with the:

                globals()

                a = 10
                globals()['a'] => 10

            Property, which defines which object from the module can be imported is:

                __all__ = ['func1', 'func2'...] 

            Dunder all is a list of strings, representing symbols which will be exported
            when module gets imported.
        
            [Example](https://colab.research.google.com/drive/1WMyDksP-w-39vG6Gls62U8i3CrdHzu6G?usp=sharing)

        """
        )

    with st.expander("Packages"):
        st.write(
            """
            Packages are folders which contain several python modules. If we want to change
            a folder into a package, we need to add initialisation file in it:

                __init__.py file

            Init file stores imports of the modules which belong to a package. This way it is 
            easier to import nested modules. Example of the __init__.py

                from .modulename import object
                from .modulename1 import *

            Python supports implicit or **namespace** packages as well. In comparison to ordinary
            packages, they don't contain an __init__.py and can be spreaded accross various folders.

            Namespace packages are covered in:

            [PEP 420](https://peps.python.org/pep-0420/)

            IMPORTING ZIPPED MODULES

            Python supports importing zipped modules. 

                import sys
                sys.path.append('./module_name.zip')
                import module

        """
        )

    with st.expander("Dunder methods and Attributes"):
        st.write(
            """
            Below is the non-extensive list of some useful dunder methods and their main usage:

            | Method / Attribute   | Usage                                                 |
            |----------------------|-------------------------------------------------------|
            | __all__              | List of strings defining which symbols of the module gets exported at the import|
            | Modules   | Lowercase, short, underscores allowed                 |
            | Classes   | Upper CamelCase                                       |
            | Functions | Lowercase, words separated with underscores           |
            | Variables | Same as functions                                     |
            | Constants | Uppercase, words separated with underscore            |

        """
        )

    with st.expander("Resources"):
        st.write(
            """
            * [Variable Referencing](https://colab.research.google.com/drive/1iVJ5R5jaI5zmyhofeadwhtvyfpWC6414?usp=sharing)
            * [PEP 8](https://peps.python.org/pep-0008/)
        
        """
        )
