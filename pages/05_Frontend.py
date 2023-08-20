# Dependencies
import streamlit as st
st.set_page_config(page_title="Frontend")

from Frontend.Intro.intro import intro
from Frontend.CSS.css import css
from Frontend.Sass.sass import sass
from Frontend.Javascript.javascript import javascript
from Frontend.React.react import react

def main():

    menu = [
        "Intro", 
        "CSS",
        "Sass",
        "Javascript",
        "React",
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "CSS":
        css()
    if sub_page == "Sass":
        sass()
    if sub_page == "Javascript":
        javascript()
    if sub_page == "React":
        react()
    else:
        pass


if __name__ == "__main__":
    main()
