import streamlit as st


def os():
    st.header("Interacting with Operating System in Python")
    st.write("")
    st.write(
        """
            Python provides built-in module called os which provides wide range of functions for working with files and directories, launching and managing processes, and other system-related tasks.

            Some common operations that can be performed using the os module include:

            *Creating, deleting, renaming, and listing files and directories
            *Changing the current working directory
            *Launching and managing subprocesses
            *Accessing environment variables
            *Managing file permissions and ownership
            *Retrieving system information, such as the current user, the host name, and the current time. 
    
        """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Environmental Variables"):
        st.write(
            """
            An environmental variable is a named value that is stored in an operating system and can be 
            accessed by various programs and processes running on that system. Environmental variables are 
            used to provide a way for software applications to share information with the operating system
            and other programs.

            We often use environmental variables to store important iformations such as API keys and similiar.

            To store environment variable on linux, we use export, to call it we use $echo and to unset it
            we use unset:

            ```
            export ENV_VALUE=somevalue
            echo $ENV_VALUE outputs somevalue
            unset ENV_VALUE deletes somevalue

            ```

            To access environmental variables with python, we use environ object from os module,
            which contains environmental variables. It's worth noting that any changes made to "os.environ" 
            are specific to the current process and do not affect the environment variables of other 
            processes or the system as a whole. Additionally, some environmental variables may be read-only 
            or have restrictions on their values, so modifying them may not always have the desired eff

            ```
            import os

            env_value = os.environ["ENV_VALUE"]

            ``` 

            If using classical virtual environment, you can set environmental variable on the environment level
            by editing env/bin/activate file.

            ```
            vim env/bin/activate

            export ENV_VALUE=somevalue
            ``` 

            If using pipenv to manage python project, you can store environmental variables in .envfile

            ```
            echo ENV_VALUE=some_value >.env  
            
            ```

            """
        )
        