# Dependencies
import streamlit as st
st.set_page_config(page_title="Frontend")

from Frontend.Intro.intro import intro
from Frontend.CSS.css import css

def main():

    menu = [
        "Intro", 
        "CSS",
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "CSS":
        css()
    else:
        pass


if __name__ == "__main__":
    main()
