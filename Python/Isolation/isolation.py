import streamlit as st


def isolation():
    st.header("Isolating python environments")
    st.write(
        """
    
        Isolating environments is crucial segment of the development in python. This topic is widely underrated and online 
        tutorials mostly offer semi-structured solutions. It is important to underline that:

        * Most of the popular OS distributions comes with the system python pre-installed.
        * It is most important to create isolated python environment per each project to avoid poluting system level python with
          non-necessary packages.
        * There are build-in and external packages for managing python versions and isolating environments. 
    
    """
    )
    st.write("")
    st.write("")

    with st.expander("Pyenv"):
        st.write(
            """

             ### Description

             Pyenv is a simple python version management tool which allows you to install and execute various types of python versions
             without taking the risk to lose overview of the state of each version. 

             #### Installation

             [Installation guide for various OS types](https://github.com/pyenv/pyenv#installation) 

             #### Usage

             Commands:

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            | pyenv                                 | Shows all the available flags                                 |
            | pyenv commands                        | Shows all the available commads                        |
            | pyenv install -l                      | Prints available python versions                         |
            | pyenv install version-string          | Install defined python versions                              |
            | pyenv versions                        | Shows available versions on the system                       |
            | pyenv global version-string           | Defines global version on the system level                       |
            | pyenv local                           | Defines pyenv version on the folder level                          |
            | pyenv virtualenv version-string  name of the venv      | Creates virtual environment with the defined interpreter                              |
            | pyenv activate                        | Activates python virtual environment               |
            | pyenv deactivate                      | Deactivates virtual environment        |
            | pyenv virtualenvs                     | Shows created virtualenvs                      |
            |                                       |                                              |

            
            If we set available virtual environment as the local python version project it gets activate when we open the folder.


            

        """
        )

    with st.expander("Pipenv"):
        st.write(
            """
                ##### Description
                
                Pipenv is officialy recommended package for managing project dependecies. It is replacement for the virtualenv. Pipenv
                makes it easy to initialise python project from the provided Pipenv file. It also allows to freeze specific
                dependecy versions with Pipenv.lock file. Pyenv package for managing python versions makes pipenv even more powerful
                since it allows you total control over your development and production environments.

                [Official documentation](https://pipenv.pypa.io/en/latest/) 

                
                ##### Installation

                Pipenv can be installed with the specific active version of python.

                python -m pip install pipenv:

                ##### Basic commands

                In case of using **pyenv** it is extremely important to define which python interpreter pipenv should use. 
                This is achieved with the pipenv --python[version string] command

                |COMMAND                | COMMAND            |
                |-----------------------|--------------------|
                | Create virtual environment environment    | pipenv shell|
                | Delete pipenv virtual environment | pipenv --rm|
                | Deactivate virtualenvironment | exit |
                | Install project dependencies | pipenv install [package name] |
                | Install development project dependecies | pipenv install --dev [package name] |
                | Installing from Pipfile | pipenv install|
                | Installing development dependecies in editable mode | pipenv install --dev -e .|
                | Uninstalling files| pipenv uninstall (--all-dev)|
                | Creating lock file to freeze used dependecies | pipenv lock |
                |                                       |                                              |
                


                ##### Basic Workflows

                [Official Documentation](https://pipenv-fork.readthedocs.io/en/latest/basics.html)

            """
        )
    
    with st.expander("Virtualenv"):
        st.write(
            """
             ##### Description
             
             Virtualenv module is part of the standard library and allows you to create virtual python environments

             ##### Installation

             python3 -m venv /path/to/new/virtual/environment

             ##### Usage
             
             Commands:

            | Command                               | Description                                  |
            |---------------------------------------|----------------------------------------------|
            |python3 -m venv /path/to/new/virtual/environment                               | Creates nev virtual environment at defined path                                 |
            |source /path/to/new/virtual/environment/bin/activate | Activates new virtual environment |
            |source /path/to/new/virtual/environment/bin/deactivate | Deactivates new virtual environment |
            |                                       |                                              |


            In most cases virtual environment is created on the project folder level. Some developers utilise direnv to establish automated activation when
            the project folder is open. For this purpose direnv should be installed and .envrc file which includes source /path/to/new/virtual/environment/bin/activate command
            created. To enable direnv direnv allow command must be executed.

            [Virtualenv modulde](https://docs.python.org/3/library/venv.html)
            [Direnv](https://direnv.net/)


            


            

        """
        )
