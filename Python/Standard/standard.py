import streamlit as st
import random
from collections import Counter
from datetime import date, datetime
from time import timezone

today = date.today()
now = datetime.now()


def standard_library():
    st.header("Standard Library")
    st.write("")
    st.write(
        """
            This section covers modules from the Python Standard Library. 
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Argparse"):
        st.write(
            """
        
        Argparse module is parser for CLI arguments, subcommands and options.

        CLI inputs are important if we want to allow users to execute various 
        parametres of the program by providing specific arguments.

        The most common CLI argument is --help which list array of all
        available arguments with description.

        **USAGE**:

        Industry Grade Python Modules 

        Example:

            import argparse

            #Fibonnaci function
            def fib(n): 
                a,b = 0,1   
                for i in range (n): 
                    a, b = b, a+b,  
                return a    
    
            def main(): 
                parser = argparse.ArgumentParser(description='Count Fibonacci') 
    
                #Define groups  
                group = parser.add_mutually_exclusive_group()   
                group.add_argument("-v", "--verbose", action="store_true")  
                group.add_argument("-q", "--quiet", action ="store_true")   
        
                #Define Arguments   
                parser.add_argument('Number', type=int, help='The fibonnaci number you wish to calculate')  
    
                #Optional Argument  
                parser.add_argument("-o", "--output", help="Output result to a fibonacci.txt file.",    
                action="store_true")    
    
                #Grab created arguments 
                args = parser.parse_args()  
    
                result = fib(args.Number)   
        
                if args.verbose:    
                    print(f'The {str(args.Number)} fibonacci number is {result}')   
                elif args.quiet:    
                    print(result)   
                else:   
                    print(f'Fib {str(args.Number)} = {str(result)}')    
    
                if args.output: 
                    f = open("fibonacci.txt", "a")  
                    f.write(str(result)+'newline')  
    
            if __name__ == '__main__':  
                main()  
                
        Resources:
         
        [Module Library](https://docs.python.org/3/library/argparse.html)
            
        [You Tube](https://www.youtube.com/watch?v=q94B9n_2nf0)
        
        """
        )

    with st.expander("Inspect"):
        st.write(
            """

            Inspect module in Python helps you gather additional information about the objects from the observed code.
            There are several available methods which you can use. The list below is not extensive, but
            gives a general perspective.

                import inspect

                #Check if object is a method
                inspect.ismethod(obj)

                #Check if object is function
                inspect.isfunction(obj)

                #Check if object is routine
                inspect.isroutine(obj)

                #Retrieve documentation 
                inspect.getdoc(obj)

                #Retrieve comments
                inspect.getcomments(obj)

                #Get module where object is stored
                inspect.getmodule(obj)

                #Check if object is function
                inspect.isfunction(obj)

            Resources:
            
            [Official Documentation](https://docs.python.org/3/library/inspect.html)    

            """
        )

    with st.expander("Operator"):
        st.write(
            """
            Operation module offers functions which corresponds to the intrinsic operators in Python.

            For example:
            
                1. a == b // operator.eq(a,b)
                2. a > b // operator.gt(a,b)
                3. a + b // operator.add(a,b)
            

            [Official Documentation](https://docs.python.org/3/library/operator.html)

         """
        )

    with st.expander("Logging"):
        st.write(
            """
            Logging is one of the most crucial features of every program. Without
            logs it is impossible to monitor, maintain and develop any application.
            Python offers logging module to address this issue.

            logging module provides log severity scale which range fro 10 to 50.

            * 10 low risk (debbuging)
            * 20 low risk (diagnostic)
            * 30 moderate risk (events which require attention)
            * 40 high risk (error, segment in application didn't work as expected)
            * 50 critical (mission critical event occured)\

            Logging messages can be divided into 3 main groups: WARNING, ERROR, CRITICAL.

            Configuration for the logging is set in the:
            
                import logging
                logging.basicConfig(level="INFO", filename="", filemode="", format="")


            Since formatting can be very important, there are several available attributes.

            * Level: defines at which level message is shown or stored
            * Filename: defines file which is created to hold logs
            * Filemode: defines mode of storing files (w: overwrite), (a:append)
            * Format: defines log format parametres.

            
            [Formatting attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)

            [PEP 282](https://peps.python.org/pep-0282/)

            [Example](https://colab.research.google.com/drive/18p9h7z_E4Sm_3KGtcfK5LPDFPXd9OMKL#scrollTo=reNFE6WkEs9o)    


         """
        )

    with st.expander("Collections"):
        st.write(
            f"""
            
            Collections module provide various types of containers and corresponding methods to store
            and retreive items. It is sort of an extension to the build in data types.

            * NAMED TUPLES

            Named tuple is a class factory function from the collections module. It allows as to create 
            light-weight object types which can store items accesible by their names. 
            

                from collections import namedtuple

                Philosopher = namedtuple('Philosopher', ['name', 'surname', 'nationality'])

                baruch_spinoza = Philosopher('Baruch', 'Spinoza', 'Dutch')

            Namedtuples have default dunder_doc property. It is available for the properties as well.
            It is possible to override the default docstring by assigning new value to the namedtuple dunder_doc.
            Same is true for the attributes of the named tuple.

            [Code](https://colab.research.google.com/drive/13uT8EWYlVaMdzyxyUy7pEg--JhVGyKQA#scrollTo=rSHG3gU0-Lf5)

            * COUNTER

            Counter is subclass of dictionary, which helps to count hashable objects;

            Example: 

                #Count number of items in list of random number. 
                Counter(random.randint(1,10) for x in range(100)).
                {Counter(random.randint(1,10) for x in range(100))}


         """
        )

    with st.expander("Random"):
        st.write(
            f"""

            Random module provides pseudo-random number generator and the related functions.
            Values are produced by the given algorithm and they are based on the provided seed 
            number. Seed number should be random as well, otherwise we can predict results.
            All funtions from random module utilise same seed. Ussually seed is derived from the 
            system clock since it changes constantly.

            1. CHOSE RANDOM NUMBER:  

                random.randint(1,10) = 
                {random.randint(1,10)}

            2. MAKE RANDOM CHOICE:

                random.choice(sequence)=
                {random.choice('sequence')}

                Make 5 choices with choices
                {random.choices('sequence', k=5)}


           3. PICK SAMPLE FROM POPULATION WITHOUT REPETITION

                
                random.sample([1,2,3,4,5], k=3) = 
                {random.sample([1,2,3,4,5], k =3 )}


            

            [Random Module Documentation](https://docs.python.org/3/library/random.html)


        """
        )

    with st.expander("Datetime"):
        st.write(
            f"""

            Datetime module supplies various classes for dealing with the date and time.
            Date-time operations are crucial for various types of tasks, for example:

            * timestamping records
            * defining expiration periods for the tokens
            * calculating trends between specific periods
            * analyse historical data and prediction of the future trends

            Below are some common operations with the date-times.  

            1. GET CURRENT DAY:  

                date.today() = 
                {date.today()}

                Attributes belonging to the date.today class are day | month | year

                today = date.today()

                * today.day = {today.day}
                * today.month = {today.month}
                * today.year = {today.year}

                datetime.now() = {datetime.now()}

                Attributes belonging to the datetime.now class are hour | minute | second

                now = datetime.now()

                * now.hour = {now.hour}
                * now.minute = {now.minute}
                * now.second = {now.second}

            2. STRING FORMATTING

                We can format datetime outputs with the strftime method which provides several parametres.

                today.strftime("%A %d %B %Y") = {today.strftime("%A %d %B %Y")}                
                now.strftime ("%A %d %B %Y %H":%m:%d) = {now.strftime ("%A-%d-%B-%Y %H:%m:%d")}

            3. CALCULATING DELTAS

                    Adding and subtracting days from given date
                
                    init_date = datetime.date(2000,1,1)
                    plus_100 = datetime.timedelta(100)
                    sum_date = (init_date+plus_100)

                    Timedeltas
                
                    date_1 = datetime.date(2022, 1, 30)
                    date_delta = datetime.timedelta(days = 29)
                    date_delta_year = datetime.timedelta(days = 360)
                    print(date_1 - date_delta)
                    print(date_1 + date_delta)
                    print(date_1+date_delta_year)

                    Arithmetic operations
                
                    bd_date = datetime.date(1978, 1, 27)
                    days_lived_so_far = (datetime.date.today() - bd_date)
                    print(days_lived_so_far) 




            

            [Datetime Module Documentation](https://docs.python.org/3/library/datetime.html)


        """
        )
