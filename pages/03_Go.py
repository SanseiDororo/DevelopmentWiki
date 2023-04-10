# Dependencies
import streamlit as st
st.set_page_config(page_title="Golang")


from Go.Intro.intro import intro
from Go.Blocks.building_blocks import building_blocks
from Go.Composits.composits import composits
from Go.Examples.examples import examples   
from Go.Control_Flows.control_flows import control_flows
from Go.Functions.functions import functions


def main():

    menu = [
        "Intro", 
        "Blocks",
        "Composits",
        "Control Flows",
        "Functions",  
        "Examples",
    ]
    
    sub_page = st.sidebar.selectbox("Menu", menu)

    if sub_page == "Intro":
        intro()
    if sub_page == "Blocks":
        building_blocks()
    if sub_page == "Composits":
        composits()
    if sub_page == "Control Flows":
        control_flows()
    if sub_page == "Functions":
        functions()
    if sub_page == "Examples":
        examples()
    
    else:
        pass


if __name__ == "__main__":
    main()
