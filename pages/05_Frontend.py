# Dependencies
import streamlit as st
st.set_page_config(page_title="Frontend")

from Frontend.Intro.intro import intro
from Frontend.CSS.css import css
from Frontend.Sass.sass import sass

def main():

    menu = [
        "Intro", 
        "CSS",
        "Sass"
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "CSS":
        css()
    if sub_page == "Sass":
        sass()
    else:
        pass


if __name__ == "__main__":
    main()
