import streamlit as st


def altair():
    st.header("Altair Charting")
    st.write('''
    
        Altair is statistical visualization library. It is based on Vega and Vega-Lite
        visualisation grammars.

        Vega is based on grammar graphics which defines several basic chart components as:

        * Data
        * Encodings
        * Geometric Objects (Bar, Points, Lines)
        * Scale
        * Statistics

        [Basic Charts Example](https://colab.research.google.com/drive/1b6CXYck3cO-D4e6oBojmAcX-VBO76I7d?usp=sharing)
        [Additional Explanation](https://www.featureranking.com/tutorials/python-tutorials/altair/)
    ''')