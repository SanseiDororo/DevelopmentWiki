# Dependencies
import streamlit as st
st.set_page_config(page_title="Golang")


from Go.Intro.intro import intro


def main():

    menu = [
        "Intro",  
        
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    
    else:
        pass


if __name__ == "__main__":
    main()
