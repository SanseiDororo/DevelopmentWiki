# Dependencies
import streamlit as st
st.set_page_config(page_title="SQL")


from SQL.Intro.intro import intro
from SQL.Blocks.building_blocks import building_blocks
from SQL.Syntax.syntax import basic_syntax

def main():

    menu = [
        "Intro",
        "Building Blocks",
        "Syntax",  
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "Building Blocks":
        building_blocks()
    if sub_page == "Syntax":
        basic_syntax()
    else:
        pass


if __name__ == "__main__":
    main()
