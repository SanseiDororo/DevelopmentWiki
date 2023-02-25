import streamlit as st


def external_libraries():
    st.header("External Libraries")
    st.write("")
    st.write(
        """
            This section covers external Python Libraries. External libraries extends
            the toolset of the standard library and can be used to solve specific
            challenges as for building command line interfaces, encryption, data wrangling
            database connections etc.
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Typer"):
        st.write(
            """
        
            Typer is external library for building command line interfaces. It can 
            be used as an out-of-the-box alternative to the Argparse module.

                Basic Usage

                import typer

                #Create and instance of the object
                app = typer.Typer()

                #Make a simple command with @app.command decorator
                @app.command
                def hello_world()
                    return ("This will be the cli output")

                #We can use function parametres as well
                @app.command
                def name_age(name:str, age:int):
                    print(f'Hello {name}, your age is {age}')

                if __name__ == '__main__':
                    app()

            Check available arguments:

            file_name.py --help

            Run file with available arguments

            file_name.py name age

            [Hompage](https://typer.tiangolo.com/)
        
        """
        )
