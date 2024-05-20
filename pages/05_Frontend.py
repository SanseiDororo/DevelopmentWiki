# Dependencies
import streamlit as st
st.set_page_config(page_title="Frontend")

from Frontend.Intro.intro import intro
from Frontend.CSS.css import css
from Frontend.Sass.sass import sass
from Frontend.Javascript.javascript import javascript
from Frontend.React.react import react
from Frontend.NextJS.nextjs import nextjs
from Frontend.Zod.zod import zod

def main():

    menu = [
        "Intro", 
        "CSS",
        "Sass",
        "Javascript",
        "React",
        "Next",
        "Zod",
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
    if sub_page == "Next":
        nextjs()
    if sub_page == "Zod":
        zod()
    else:
        pass


if __name__ == "__main__":
    main()
