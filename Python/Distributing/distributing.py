import streamlit as st


def distributing():
    st.header("Distributing")
    st.write("")
    st.write(
        """
            This section covers different ways to package and distribute python code.
            By convenction python files are considered as modules, while folders containing
            __init__.py file are considered as packages. There are several ways to organise
            and automatically package your code and add additional metadata information.

            Setuptools library provides toolset to build, package and distribute python code.
            It is a thin wraper build around distutils. 

    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Setup.py"):
        st.write(
            """

            In order to build a python code as a consistent package we can use setup.py file. 
            Setup.py file should contain all the neccessary data associated with the build process
            of the package. Most important segments of the setup file are (requirements, python version,
            license, author etc.) 
            
                Non extensive example of the setup.py file

                # !/usr/bin/env python
                # type: ignore

                from setuptools import setup, find_packages
                from itertools import chain


                requirements = [
                    'python_package 1.7.*',
                    'can be github repo,
                ]


                extras = dict(
                    dev=[
                        'additional package for specific purpose',
                    ],
                    
                    debug=[
                        'debug_package',
                    ],
                    
                    test=[
                        'testing_package'
                    ],
                )


                # generate an extras entry that installs all requirements
                extras['all'] = list(chain.from_iterable(extras.values()))

                #Additional metadata
                setup(
                    name='name of the package',
                    version='0.1.0',
                    description='',
                    keywords='',
                    classifiers=[
                        'Programming Language :: Python',
                    ],
                    author='',
                    author_email='',
                    license='',
                    url='',
                    packages=find_packages(),
                    include_package_data=True,
                    python_requires='>=3.10',
                    # data_files=[],
                    zip_safe=False,
                    install_requires=requirements,
                    extras_require=extras,
                )

            Package is installed with:

                    pip install -e .

            Dot stands for the current directory, while -e flag means editable.

            Additional resources:

            [Practical guide](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)

            [Writting setup script](https://docs.python.org/3/distutils/setupscript.html)

            [Extensive template](https://github.com/pypa/sampleproject) 
        
        """
        )

    with st.expander("Pyproject.toml"):
        st.write(
            """
            Pyproject.toml is the succesor of the setup.py file. The main reasons
            for updating the main approach of building python projects with the setuptools
            and corresponding setup.py file are covered in the (PEP 517)[https://peps.python.org/pep-0517/]
            and (PEP 517)[https://peps.python.org/pep-0518/].

            Pyproject.toml creates ad-hoc virtual environment in order to execute the build.

        """
        )

    with st.expander("Poetry"):
        st.write(
            """
        
        """
        )
