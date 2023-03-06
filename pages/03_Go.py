# Dependencies
import streamlit as st
st.set_page_config(page_title="Golang")


from Go.Intro.intro import intro
from Go.Blocks.building_blocks import building_blocks


def main():

    menu = [
        "Intro", 
        "Blocks", 
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "Blocks":
        building_blocks()
    
    else:
        pass


if __name__ == "__main__":
    main()
