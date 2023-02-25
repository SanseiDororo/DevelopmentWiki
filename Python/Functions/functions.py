import streamlit as st


def functions():
    st.header("Functions in Python")
    st.write("")
    st.write(
        """
            This section covers most important segments of functions in Python. 
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Basics"):
        st.write(
            """
            Functions are callables which execute predefined set of code under it's own scope. 
            They can be parameterized. When we call a function with certain parametres, these parametres become arguments 
            of the given function. 
            
            Functions are Python's first class citizens which means they can be passed as arguments to 
            other functions or return another function. This functions are called higher order functions.
            [Functools](https://docs.python.org/3/library/functools.html) module stores various high-order
            function to perform specific tasks.

            Example: Return maximum value of an iterable with the reduce high level function from
            the functools module (built-in max function would do just the same).

                from functools import reduce
                a_list = [1,7,89,212]
                reduce(lambda x, y: x if x > y else y, a_list)
                

            

            Functions can take positional arguments which may or may have not default value. For
            example (def a_func(a,b=20)). Default values of the function can be retrieved with
            the **defaults** dunder method method. We can pass a tuple of remaining positional arguments to 
            function with *args. 

            Functions can as-well take keyword arguments which are returned as a dictionary of key-value
            pairs. Keyword parametres are defined by **kwargs. You can call *args and **kwargs as you like.

            """
        )
        st.write("")
        st.write(
            """

            | Positional Arguments                  | Keyword Arguments                            |
            |---------------------------------------|----------------------------------------------|
            | Can have default value                | Can have default value                       |
            | *args collects remaining values       | **kwarg collect key-value arguments          |
            | * end of positional arguments         |                                              |
            

            """
        )
        st.write("")
        st.write(
            """
            [Code Sample:](https://colab.research.google.com/drive/1HrwIlNfjwxE5XohQcK49pB3dvIR6MrAJ?usp=sharing)
        
        """
        )

    with st.expander("Documentation And Annotation"):
        st.write(
            """
            First line of every function, if it is a string, serves for the documentation purposes.
            One or multiline string gets stored into .__doc__ property of the function objects. 
            This helps anybody using function to know it's puprose and the mechanism. Docstring can be
            accessed with help() funtcion or by calling the objec.__doc__ property.

            We can as-well clarify parametres and function's returns with annotations. Annoations
            can be created after: for each parameter and after -> for returns. For example:

                def func_doc(a: 'A beautiful string', b:'int') -> 'str a multiplied b times':
                    return(a*b)

            Functions have properties and methods. We can inspect all the attributes that are available
            for the certain function with the dir() method. For example:

                dir(help)

            [PEP 257 - Docstring Convenctions](https://peps.python.org/pep-0257/)

            [PEP 3107 - Function Annotations](https://peps.python.org/pep-3107/)    
        
        """
        )

    with st.expander("Anonymous Functions"):
        st.write(
            """
            Anonymous functions in Python are single line expressions initialised with
            the keyword lambda. They can be stored in a variable or used as a parameter
            of another function. They can use only single expresseion and cannot be annotaded.

            Example:

                lambda x: x ** 3

                
        
        """
        )

    with st.expander("Closures"):
        st.write(
            """

            Since functions are first-class objects in Python it is posible to nest functions. We could
            define closure as inner function which shares variables with the outer function. Function
            becomes closure only if it has one free variable.

                def outer():
                    #this is enclosing function
                    free_variable = 10
                    
                    def inner_function():
                        print(free_variable)
                    
                    return inner_function

                We can assign outer function to variable.
                
                var_1 = outer
                var_1() => 10

            
            
        """
        )

    with st.expander("Decorators"):
        st.write(
            """
            
            Decorator function is a function which takes another function as an argument. Decorators
            can be stacked and parameterized. 

            Example:
                import inspect
                
                def introspection(fn):
                print(inspect.getdoc(fn))
                print(inspect.getsource(fn))
        
                @introspection
                def arb_func(a,b):
                    "This is an example of the function passed to another function"
                    sum = a + b
                    mul = a * b
                    return (sum, mul)

            [Resource](https://colab.research.google.com/drive/1r7a-eL2FSK1m_dxjvWiXQMTqNIG-D_--#scrollTo=dXYmO4XeIItu)

        """
        )

    with st.expander("Functools"):
        st.write(
            """
            
            Functools module contains set of higher-order functions to perform specific 
            operations on callable objects. It was introduced in Python 2.5 in 2006. Below is the
            list of some common functions:

            * Partial is callable which allows us to define fixed set of arguments and generate new
              function which can be passed as a signle argument to another function.

            * Partial method can be considered as partial for classes. It is not meant to be directly
              callable but integrated as a class method.

            * Wraps is function decorator used to wrap functions of the decorator.

            * Caching (lru_cache, cache, cached_property). List reacently use (lru) cache is used to
              save time when expensive function is called with the same arguments. Cache was introduced
              in Python 3.9. It is same as lru_cache but without maximum size. Cached property is very
              useful for thing that get calculated once and dont change over time. 

            * Reduce. Built in example is sum which reduce iterable to a single value. 
        

            [Functools documentation](https://docs.python.org/3/library/functools.html)

            [Martin Heinz Blog](https://martinheinz.dev/blog/52)

            [Examples](https://colab.research.google.com/drive/1O5OZevVVON68o2PCVtoXbjp2k8V1NBmP#scrollTo=bdouNM_WsPs9)

        """
        )
