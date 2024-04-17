#Dependencies
import streamlit as st
st.set_page_config(page_title="Git")


from Git.Intro.intro import intro
from Git.Initialisation.initialisation import initialisation
from Git.Branching.branching import branching
from Git.Sharing.sharing import sharing
from Git.Inspecting.inspecting import inspecting
from Git.Merging.merging import merging
from Git.Reseting.reseting import reseting
from Git.Commiting.commiting import commiting

def main():
    
    menu = ['Intro', 'Initialisation', 'Branching', 'Merging', 'Reseting', 'Sharing', 'Inspecting']

    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    if sub_page == 'Initialisation':
        initialisation()
    if sub_page == 'Branching':
        branching()
    if sub_page == 'Merging':
        merging()
    if sub_page == 'Reseting':
        reseting()
    if sub_page == 'Sharing':
        sharing()
    if sub_page == 'Inspecting':
        inspecting()
    else:
        pass
    


if __name__ == '__main__':
    main()