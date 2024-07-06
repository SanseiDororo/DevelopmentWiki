#Dependencies
import streamlit as st
st.set_page_config(page_title="Linux")


from Linux.Intro.intro import intro
from Linux.Administration.administration import administration
from Linux.Containerization.container import containers

def main():
    
    menu = ['Intro', 'Administration','Containerization']

    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    if sub_page == 'Administration':
        administration()
    if sub_page == 'Containerization':
        containers()
    
    else:
        pass
    

if __name__ == '__main__':
    main()