# Dependencies
import streamlit as st
st.set_page_config(page_title="Python")


from Python.Intro.intro import intro
from Python.Blocks.building_blocks import building_blocks
from Python.Numeric.numeric import numeric_types
from Python.Functions.functions import functions
from Python.Sequences.sequences import sequences
from Python.Zen.zen import zen
from Python.Standard.standard import standard_library
from Python.External.external import external_libraries
from Python.Distributing.distributing import distributing
from Python.Isolation.isolation import isolation
from Python.Tensor.tensor import tensor
from Python.Pandas.pandas import pandas
from Python.Numpy.numpy import numpy
from Python.Altair.altair import altair



the_truth = zen()


def main():

    menu = [
        "Intro",
        "Building Blocks",
        "Numeric Types",
        "Functions",
        "Sequences",
        "Standard Library",
        "External Libraries",
        "Distributing",
        "Isolation",
        "Pandas",
        "Numpy",
        "TensorFlow",
        "Altair",
        
    ]
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    elif sub_page == "Building Blocks":
        building_blocks()
    elif sub_page == "Numeric Types":
        numeric_types()
    elif sub_page == "Functions":
        functions()
    elif sub_page == "Sequences":
        sequences()
    elif sub_page == "Standard Library":
        standard_library()
    elif sub_page == "External Libraries":
        external_libraries()
    elif sub_page == "Distributing":
        distributing()
    elif sub_page == "Isolation":
        isolation()
    elif sub_page == "Pandas":
        pandas()
    elif sub_page == "Numpy":
        numpy()
    elif sub_page == "TensorFlow":
        tensor()
    elif sub_page == "Altair":
        altair()
    else:
        pass


if __name__ == "__main__":
    main()
