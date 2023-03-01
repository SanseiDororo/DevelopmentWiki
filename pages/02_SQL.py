# Dependencies
import streamlit as st
st.set_page_config(page_title="SQL")


from SQL.Intro.intro import intro
from SQL.Blocks.building_blocks import building_blocks

def main():

    menu = [
        "Intro",
        "Building Blocks"  
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "Building Blocks":
        building_blocks()
    else:
        pass


if __name__ == "__main__":
    main()
