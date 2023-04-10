import streamlit as st


def building_blocks():
    st.header("Go Building Blocks")
    st.write(
        """
    
        This section covers basic Go building blocks. It
        can serve as a quick Go refresher. Knowing fundamentals is
        always best approach to building complex ontologies.  
    
    """
    )
    st.write("")
    st.write("")

    with st.expander("Data Types"):
        st.write(
            """
            Go supports the following built-in data types:

            | Numbers                   | Collections                               | Callables                 | Constants             |
            |---------------------------|-------------------------------------------|---------------------------|-----------------------|
            | Int(Signed integers)      | Array (Fixed size, same type data )       | User Defined Functions    | Boolean (true | false)|     
            | Uint (Unsigned integers)  | Slice (Dynamic size, same type data)      | Built-in-Functions        | iota ()               |
            | float32 (32bit floats)    | Strings (Sequence of character)           | Built-in-Methods          |                       |
            | float64 (64bit floats)    | Struct (Collection of named fields, )     | Instance Methods          |                       |
            |                           | Channels (syncronisation mechanism)       |                           |                       |
            |                           | Map (Unordered collecyion of key-values)  |                           |                       |
            

        """
        )
        st.write("")
        st.write("")

    with st.expander("Data mutability"):
        st.write(
            """    

            Objects in Go fall into the two groups:

            | Mutable     | Immutable                                              |
            |------------ |--------------------------------------------------------|
            | Slices      | Strings                                                |
            | Maps        | Struct                                                 |
            | Arrays      |                                                        |
         
                                               
            

        """
        )

    with st.expander("Naming Convections"):
        st.write(
            """
        
            Rules how to use naming in Go are precisely
            defined in the [document](https://go.dev/doc/effective_go#names). 

            **CONVENCTIONS**

            * Use mixedCaps for variables
            * Use short names in the function scope
            * Use all capitals for acronyms such as fastAPI
            * Use CamelCase for multi-word names and package scope items.
            * Interface names consists of method names plus er. For example Formatter.
            * There are many reserved identifiers in go such as var, type, defer break etc.
              You cannot use reserved names as a variables.
            * Names should start with a letter or underscore.
            
        
        """
        )

    with st.expander("Variables"):
        st.write(
            """
        
                Go is statically typed langugae meaning that variables are named storage location in 
                memory that holds a value of a certain type. Strictly speaking we have two types of
                identifiers in go: variables and types. Identifiers in go must be a sequence of letters.

                ##### Declaration 

                In go you can declare a variable with the var key word followed by the name of the variable
                and the corresponding type

                Example:

                ```
                var age int = 32
                var name string = "John"
                ```
                If you declare a variable without a value, 0 is assigned automatically.

                When assigning new value to a already declared value, we use = 

                Example:
                ```
                age = 64
                ```

                We use declaration when: 
                
                * We don't know the initial value of a variable.
                * We need a package scoped variable.
                * When grouping variables for greater readability

                Grouping related variables example:

                ```
                var (
                    customer string
                    name string
                    surname string
                    address string
                )
                ```
            """)
        st.write("---")
        st.write(
            
                """
                ##### Short declaration operator

                You can also use the := operator for a shorter way to declare and 
                initialize a variable with inferred type:

                Example:

                ```
                surname := "Doe"
                ```

                We use short declaration when:

                * If you know initial value of the variable.
                * When you want to have consise code.
                * For redeclaration
            """)
        st.write("---")
        st.write(
            
            """
                #### Type conversion

                If we want to change type of a variable, we use type(value) declaration. We can actualy
                convert value of a given type to other type.

                For example:

                ```
                package main

                import (
                	"fmt"
                )

                func main() {
                
                	var doubled int
                	height := 1.5
                	number := 2

                	fmt.Println(height)
                	fmt.Println(number)

                	doubled = int(float64(number) * height)
                	fmt.Println(doubled)

                }    
                ```
            """
        )
        st.write("---")
        st.write(
            """
            In Go, you can check the memory address of an object using the **&** operator followed by the variable name. 
            This returns a pointer to the memory address of the variable.
            
            Example:

            ```
            package main

            import "fmt"

            func main() {
            	var x int = 10
            	fmt.Println("Memory address of y variable:", &x)
            }

            ```

        
            """
        )
        
        st.write("")
        st.write(
            """
            **VARIABLE EQUALITY**:

            We can check if two variables are referencing the same memory address
            with the **&** identity operator.

            Example:

            ```
            package main

            import "fmt"

            func main() {
            
            	var x int = 20
            	var y int = 20
            	var ptr1 *int = &x
            	var ptr2 *int = &y

            	if ptr1 == ptr2 {
            		fmt.Println("ptr1 and ptr2 are pointing to the same object")
            	} else {
            		fmt.Println("ptr1 and ptr2 are pointing to different objects")
            	}
            }



            ```

            To check equality of the internal object state we use **==** operator.
            
            ```
            package main

            import "fmt"

            func main() {
            
            	var x int = 20
            	var y int = 20

            	if x == y {
            		fmt.Println("x and y are equal")
            	} else {
            		fmt.Println("x and y are not equal")
            	}
            }
            ```
        
        """
        )
        st.write("---")

        st.write('''
        
            ##### CODING EXAMPLES

            * [Assigning variables](https://play.golang.org/p/-LYS4_vrIjT)
            * [Creating different types and asign default value](https://play.golang.org/p/A6S1em2paDD)
            * [Create custom type and printout the value with Printf("%T", variable name)](https://play.golang.org/p/Tgz55p-RyW6)
            * [Output the variable in binary, decimal and hexadecimal.](https://play.golang.org/p/UYQc_28EYK0)
            * [Using operators in go language](https://play.golang.org/p/76R-poSzaY)
            * [Declaring constants in GO](https://play.golang.org/p/1JXxqY_gaGE)
            * [Raw string literal](https://play.golang.org/p/uEBXo3LGpOV)
            * [Iota is keyword which increments value for 1](https://play.golang.org/p/QWqnXcElqEV)
        
        
        
        ''')

    with st.expander("Scopes"):
        st.write(
            """    

                Main scopes in GO:

                * Package scope:
                  Variables, functions, and types that are defined at the package level have 
                  package scope, which means that they are visible to all files within the same 
                  package. Package-scoped identifiers are usually named with a capital letter at 
                  the beginning of the identifier, to indicate that they are exported and can be 
                  used by other packages.
                * File scope:
                  In addition to package scope, Go also has file scope, which means that variables, 
                  functions, and types that are defined at the top level of 
                  a file (but not within a package) are only visible within that file.
                * Function scope:
                  Variables that are defined inside a function have function scope, 
                  which means that they are only visible within that function. 
                  When the function returns, the variables are no longer accessible.  
                * Block scope:
                  Variables that are defined inside a block (i.e., a set of curly braces)
                  have block scope, which means that they are only visible within that block. 
                  This includes if statements, for loops, and other control structures.
            """
        )

    with st.expander("Modules"):
        st.write(
            """
            A module in Go is a collection of related packages that are versioned together as 
            a single unit. A module is defined by a go.mod file, which specifies the module's 
            name and the versions of its dependencies. Modules in Go provide a way to manage dependencies 
            between packages, and they allow developers to specify the exact versions of dependencies that 
            their code requires.

            """
        )

    with st.expander("Packages"):
        st.write(
            """
            A package in Go is a collection of related Go source code files that 
            are organized together in a single directory. Each package has a unique name, 
            which is usually a short, lowercase name that describes the functionality of 
            the package. Packages in Go are used to organize code into reusable and 
            maintainable units, and they provide a mechanism for encapsulation and information 
            hiding.

        """
        )

    

     

   
