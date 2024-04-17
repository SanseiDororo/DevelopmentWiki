#Dependencies
import streamlit as st
st.set_page_config(page_title="Linux")


from Linux.Intro.intro import intro
from Linux.Administration.administration import administration

def main():
    
    menu = ['Intro', 'Administration',]

    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    if sub_page == 'Administration':
        administration()
    
    else:
        pass
    

if __name__ == '__main__':
    main()