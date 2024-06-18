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
from Python.Polars.polars import polars
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
        "Polars",
        "Numpy",
        "TensorFlow",
        "Altair",
    ]
    
    functions_map = {
        "Intro": intro,
        "Building Blocks": building_blocks,
        "Numeric Types": numeric_types,
        "Functions": functions,
        "Sequences": sequences,
        "Standard Library": standard_library,
        "External Libraries": external_libraries,
        "Distributing": distributing,
        "Isolation": isolation,
        "Pandas": pandas,
        "Polars": polars,
        "Numpy": numpy,
        "TensorFlow": tensor,
        "Altair": altair,
    }

    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page in functions_map:
        functions_map[sub_page]()

if __name__ == "__main__":
    main()
