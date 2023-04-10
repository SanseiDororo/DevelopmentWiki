import streamlit as st


def control_flows():
    st.header("Control Flows in GO")
    st.write(
        """
    
        In Go, control flow refers to the order in which the program's statements are executed. 
        It determines how the program will behave based on the conditions and decisions defined by 
        the programmer or the user. Go has various control flow statements that allow developers 
        to write programs with branching logic and looping constructs.

        The most basic structure of the control flow is:

        Initial state - Evaluation - Consequence

        We have two types of flows:

        * Conditional
        * Sequential   
    
    """
    )
    st.write("")
    st.write("")

    with st.expander("Conditionals"):
        st.write(
        
        """
        If/else statements allows developers to to test a condition and execute consequential 
        block of code. If statements in GO have the following structure:

        ```

            if condition {
                execute code block
            } else if {
                execute code block
            } else {
                execute code block
            }

        ```                           
            

        """
        )

    with st.expander("Loops"):
        st.write(
            """    
                GO provides various types of loops:

                ###### For loop

                For loop is used to repeat a block of code a certain number of times.   

                It consists of starting condition, final condition and stap.

                ```
                    for i = 0; i < 10; i ++ {
                        code block to execute
                    }

                ```
                ---
                ###### Range loop

                The range loop is used to iterate over arrays, slices, strings, maps and channels

                Example:

                ```
                    arr := []int{1, 2, 3, 4, 5}
                    for index, value := range arr {
                        execute code)
                    }

                ```
                ---
                ##### Infinite loop

                Infinite loop is a loop without end condition. It will run until
                program is stopped or reaches the break statement.

                Example:

                ```
                for {
                        fmt.Println("This is an infinite loop!")
                    }

                ```
           
            """
        )

    with st.expander("Switch"):
        st.write(
            """    
                In Go, the switch statement provides a way to execute 
                different code blocks based on the value of a given expression. 

                Example:

                ```
                fruit := "apple"

                switch fruit {
                case "apple":
                    fmt.Println("It's an apple!")
                case "banana":
                    fmt.Println("It's a banana!")
                default:
                    fmt.Println("It's some other fruit.")
                ```

                We can have multiple case switch statement:

                ```
                switch city {
                case "Zagreb", "Split":
                    fmt.Println("Croatia!")
                case "Berlin ", "Koln":
                    fmt.Println("Germany")
                default:
                    fmt.Println("No mans land")

                ```

        Example:

        ```
            if condition1, condition2 {
                execute code block
            } else if {
                execute code block
            } else {
                execute code block
            }

            """
        )

    with st.expander("Conditionals"):
        st.write(
        
        """
        If/else statements allows developers to to test a condition and execute consequential 
        block of code. If statements in GO have the following structure:

        ```

            if condition {
                execute code block
            } else if {
                execute code block
            } else {
                execute code block
            }

        ```                           

        """
        )

    with st.expander("Loops"):
        st.write(
            """    
                GO provides various types of loops:

                ###### For loop

                For loop is used to repeat a block of code a certain number of times.   

                It consists of starting condition, final condition and stap.

                ```
                    for i = 0; i < 10; i ++ {
                        code block to execute
                    }

                ```
                ---
                ###### Range loop

                The range loop is used to iterate over arrays, slices, strings, maps and channels

                Example:

                ```
                    arr := []int{1, 2, 3, 4, 5}
                    for index, value := range arr {
                        execute code)
                    }

                ```
                ---
                ##### Infinite loop

                Infinite loop is a loop without end condition. It will run until
                program is stopped or reaches the break statement.

                Example:

                ```
                for {
                        fmt.Println("This is an infinite loop!")
                    }

                ```
           
            """
        )

    with st.expander("Defer"):
        st.write(
            """    
                The defer statement in Go is used to schedule a function call to be executed 
                after the function that contains the defer statement completes. 
                The deferred function calls are executed in a last-in-first-out (LIFO) order. 
                This can be useful for performing cleanup actions, releasing resources, or 
                executing code that should always run after a function has completed, 
                regardless of whether an error occurred or not. 

                Example:

                ```
                package main

                import (
                	"fmt"
                )

                func main() {
                	defer fmt.Println("World!") // This statement will be executed last.
                	fmt.Println("Hello,") // This statement will be executed first.
                }

                ```
           
            """
        )

  