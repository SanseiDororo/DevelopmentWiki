import streamlit as st


def numeric_types():
    st.header("Numeric Types")
    st.write("")
    st.write(
        """
            This section covers numeric types. 
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Numeric Types"):
        st.write(
            """
            Numeric types has the following coresponding objects in Python:

            | Number Type            | Object                                       |
            |------------------------|----------------------------------------------|
            | Integer                | int                                          |
            | Rational Numbers       | fractions.Fraction                           |
            | Real Numbers           | float or decimal.Decimal                     |
            | Complex  Numbers       | complex                                      |
            | Boolean truth values   | False(0), True(1)                            |
                
        
        """
        )

    with st.expander("Integers"):
        st.write(
            """
            Integers are integral numbers. In Python they are represented as the instance of the int class.
            In the memory they are stored as base2 digits.     

            Since Python is dynamically typed language, the size of an integer you can use depends on the available
            memory.

            We can check the memory size of the integer with the getsizeof() function from the sys module.

            Python 3.6 or above allows underscores between the sections of the
            large integers in order to make it readable. We can write 10m as
            10_000_000. 
            
            Integers support all the standard arithmetic operations:

            | Operation              | Symbol                                       |
            |------------------------|----------------------------------------------|
            | Addition               |   +                                          |
            | Subtraction            |   -                                          |
            | Floor Division         |   //                                         |
            | Modulo                 |   %                                          |             
            | Multiplication         |   *                                          |
            | Exponents              |   **                                         |


           

        """
        )

    with st.expander("Rational Numbers"):
        st.write(
            """
                Rational numbers are fractions of integer numbers. Fraction of two rational
                numbers is as-well rational number. Fraction class from fraction module is
                used to represent rational numbers. Constructor takes 2 arguments,
                numerator and denominator. Fractions are automatically reduced by
                the Fraction class. For example: Fraction (9, 6) returns fraction(3, 2). 
                Fraction class support basic arithmetic operations. Fraction class has numerator and denominator
                attributes which can be retreived.

                Resources:

                [Code Sample](https://colab.research.google.com/drive/1uL0oU3oD5-3vT27PeMZbVisPyABYMsSa?usp=sharing)


        
        """
        )

    with st.expander("Floats"):
        st.write(
            """
                Python uses float class for representing real numbers. Floats can be
                infinite as for example 3.33... .The problem is that computers can store
                only finit length which is defined by the available resources. On many
                occasions we deal with approximate representation which can be verified
                by checking bigger number of decimal positions. 

                In order to check relative equality of the two floats, we can use
                isclose function from the math module.

                Resources:

                [PEP 485](https://peps.python.org/pep-0485/)

                [Code Sample](https://colab.research.google.com/drive/1APqyx71Bx_f5u2dxV2t7AHF-hOXWi6Tn?usp=sharing)

        
        """
        )

    with st.expander("Decimals"):
        st.write(
            """
                As it is quoted in the PEP327 decimals data type is used where decimals 
                are needed but binary floating point is too inexact. Decimals in Python are covered
                in the decimal module which contains the Decimal class and takes integers, strings or even 
                tuples to construct decimal numbers. Important parametres which define outcome of
                arithmetic operatios, such as precision, rounding method and others can be defined with the decimal.getcontext() function
                on the level of the decimal module or specific context.


                Resources:

                [PEP 327](https://peps.python.org/pep-0327/)

                [Code Sample](https://colab.research.google.com/drive/1s5PUnCyJ4MP_oVmD8wJ1BLApvJQs_Rot?usp=sharing)

        
        """
        )
    with st.expander("Booleans"):
        st.write(
            """
                Booleans in Python are represented with the bool class which is a subclass of 
                int class. Boolean True and False are associated with 0 and 1 and fuction
                as truth values. Each class in Python has the corresponding truth value. For example
                every instance of int class which is not a 0 has a truth value of True. Booleans
                are of utmost importance for any kind of consistent ontology or epistemology.
                In most cases default truth value of an object is true. This isn't the case for
                None, False, 0, empty sequences and empty mappings. 

                Resources:

                [PEP 285](https://peps.python.org/pep-0285/)

                [Code Sample](https://colab.research.google.com/drive/1MZ9sPLtEAwGbx2caCRzpbcE-JcfyNfLV?usp=sharing)

        
        """
        )
