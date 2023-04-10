import streamlit as st


def composits():
    st.header("Composit Types")
    st.write("")
    st.write(
        """
            Composite types are types that are composed of other type. In general these are:

            * Arrays
            * Slices
            * Strings as sub class of slices
            * Maps
            * Struct  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Types"):
        st.write(
            """

            In golang we have the following composite data types:
            
            |  Array                    | Slice                             | Strings : sequence of Unicode elements| Maps               | Structs             |
            |---------------------------|-----------------------------------|---------------------------------------|--------------------|---------------------|
            | fixed -length             | indexable                         | indexable                             | indexable          | groups of various   |
            | elemnts of specific type  | elemnts of specific type          | homogeneous                           | key - value pairs  | types of variables  |
            | iterable                  | iterable                          | iterable                              | iterable           | values accessed by .|
            | immutable                 | mutable                           | immutable                             | mutable            |                     |
            | fixed order               | arbitrary length                  | fixed length                          | arbitrary lenght   |                     |
            | indexable                 | arbitrary order                   | fixed order                           | arbitrary order    |                     |
            

            """
        )

    with st.expander("Strings"):
        st.write(
            f"""
            
            In GO strings are immutable sequences of Unicode characters. They are declared with
            the string type declaration. For example:

            ```
            var nameFirst string
            ```

            ###### Raw string literal

            String literals enclosed in double quotes are interpreted by GO, while raw string literals
            enclosed in backquots are unprocessed string data, which means that they can contain multiple lines
            and special characters. 

            ###### String Length

            To find out the lenght of the string in GO, we can use the built in len function. The
            len function returns the number of the bytes in a string. 

            For example:

            ```
            fmt.Println(len(someString))
            ``` 

            Non english letters can take more than one byte. If we want to count character, we can 
            call RuneCountInString function from the unicode/utf8 package

            ```
            import ("fmt"; "unocode/utf8")

            utf8.RuneCountInString(someString)

            ``` 
        """)
        st.write("---")
        st.write("""
            ###### Format Specifiers

            As in other languages we can use format specifiers in GO to replace variables in 
            a string. List of most common specifiers in go: 

            * %v: The value in a default format.
            * %d: Integer value in decimal notation.
            * %s: String value.
            * %f: Floating-point value with a decimal point.
            * %t: Boolean value, true or false.
            * %p: Pointer value, in hexadecimal notation.
            * %q: Quoted string value, with special characters escaped.
            * %x, %X: Integer value in hexadecimal notation (lowercase or uppercase).
            * %b: Integer value in binary notation.
            * %e, %E: Floating-point value in scientific notation (lowercase or uppercase).
            * %c: Rune (Unicode code point) value.
            * %T: type 
        """)

        st.write("---")
        st.write("""

            ###### Escape Sequences

            To represent special characters or characters which can not be represented in
            string literals we use the following escape sequences:

           * \ n: Newline character.
           * \ r: Carriage return character.
           * \ t: Tab character.
           * \ ': Single quote character.
           * \ ": Double quote character.
           * \ \: Backslash character.
           * \ a: Alert or bell character.
           * \ b: Backspace character.
           * \ f: Form feed character.
           * \ v: Vertical tab character.
           * \ xhh: Hexadecimal escape sequence, where hh represents two hexadecimal digits.
           * \ uhhhh: Unicode escape sequence, where hhhh represents four hexadecimal digits.
            

            """
        )

    with st.expander("Arrays"):
        st.write(
            '''
                ###### Arrays

                Array in GO represents fixed-length sequence of elements of the same type. Array elements
                are unnamed variables to which we can assign values.

                We can initialize arrays like this

                ```
                    var arrayName [size]elementType

                ```

                The lenght of an array is an inseparable part of it's type, which is very important
                in case of equality comparison.

                ```
                    ar1 := [5]int{1,2,3,4,5}

                    is equal to 

                ar2 := [5]int{1,2,3,4,5}

                ```

            We can assign one array to another array. This creates multidimensional array
            or array of arrays

            ```
            arrArr := [3][5]int{}

            ```
                
            '''
            )
        
    with st.expander("Slices"):
        st.write(
            '''
                ###### Slices

                In Go, a slice is a dynamic data structure that represents a sequence of elements of the same type. 
                Slices are similar to arrays, but with some important differences:

                * They have dynamic size, you can add or remove elements at runtime
                * They are reference type instead of value types like arrays

                When you assign slice to a variable or a function you are assigning a 
                reference to the underlying data.

                We can initialize slices like this

                ```
                    var sliceName[]elementType

                ```
                
                ---

                Slices have dynamic length which is why we don't need to declared it:


                ```
                    sliceNum := []int{1,2,3,4,5}
                ```
                ---

                Slices can grow and shrink in runtime. We can append elements with append function. 

                ```
                    nums := []int{1, 2, 3}

                    // append a new element to the slice
                    nums = append(nums, 4)
                ```
                ---

                Slice header is a type structure with 3 main attributes:

                * pointer - storing memory location of the backing array
                * lenght - storing length of the backing array
                * capacity - storing capacity of the backing array

                ---

                We can create a slice of a slice which holds new basic attributes id. new pointer,
                length and capacity. Sliced slice points to the same backing array but at a different
                elements 

                ```
                //This slice creates backing array in the memory
                sl := []int{1,2,3,4,5,6,7,8}

                //We can slice it like this
                //sliced := sl[starting point:end]

                sliced := sl[0:3]

                ```
                ---
                If you want to create a slice with defined length, you can use make function.

                ```
                // data type, length, capacity
                make ([]int, 0, 5)
                ```
                ---

                If you would like to copy the elements of one slice to another slice, you can use
                copy functions. Copy function copies only elements based on the lenght of the smallest
                slice.

                ```
                copy(destination slice, source slice)
                ```
                ---
                We can as well create multi-dimensional slices. In contrast to multidimensional arrays
                inner slices can have dynamic range of the elements.

                ```
                cost := [][]int{
                
                {25, 50},
                {350, 500, 700},
                {250, 360, 120}
                }
                ```

            '''
            )
        
    with st.expander("Maps"):
        st.write(
            '''
                Map is collection of indexable key-value pairs. It allows fast lookups.

                We can declare a map like this:

                ```
                    var name map[key type]value type
                    
                    var dictionary map[string]string
                    var telephoneNumber map[string]int
                ```
                ----

                ###### Map Internals
                
                Map value is only a pointer to a Map Header. Map Header cointains another pointer to 
                the real data.
            '''
        )

    