import streamlit as st


def functions():
    st.header("Functions in GO")
    st.write(
        """
        Functions are one of the most important segments of each programming language. They
        represent callable and reusable block of code. In GO every function starts with func
        keyword followed by the function name and executable code block. Each function has it's
        own scope. Variables or values are not accessible outside the function scope.

        ```
            //Function in GO has the following structure

            func name (parameter1 type, parameter2 type){
            
                code block

            }


            func multiply(a, b int) int {

	            return a * b

            }

        ``` 

        The most important function of every package is main function which reprepresents the entry
        point of the program's main thread.
        
    
        """
    )
    st.write("")
    st.write("")

    with st.expander("Pointers"):
        st.write(
        
        """
            Pointers are variables which store memory address of a certain value. You can use pointers
            to manipulate values indirectly.
        """
        )

   