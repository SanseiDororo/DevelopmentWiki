import streamlit as st

st.set_page_config(
    page_title="Development Wiki",
)

st.sidebar.info("Select a subsection above.")

st.write("# Welcome to Development Wiki")
st.write(" ")
st.write(" ")


st.markdown(
    """
    This is development wikipedia, covering various fields of IT technologies from programing languages
    to version control system, databases, linux, cloud etc. Topics are organised in form of subsections
    listed as separate pages on the sidebar. Each subpage has its own subsections listed in the dropdown
    menu. Content is updated constantly.
    
    """
)
st.write(" ")
st.write(" ")

with st.expander("Support"):
    st.write(
            """

            If you like this project and you would like to support it's further development, you
            can make a donation by sending ERG, ADA or BTC:

            ##### ERG
        
                9gzJYSDzkULXgCgAp6GGMeKtxo4ELGDi4TPauJfJLTUqJ2GWbBg
            """
        )

    st.write(
            """

            ##### ADA
        
                addr1qya93t4rcz70e5fh3pamcc33ge89yykjwsfl8arxmepx2ndnqlhalm5s3n6wyt3yq60a3uyhuws34t39qakwl6gcvvzqec2ske
            """
        )

    st.write(
            """
            ##### BTC
        
                16T8KzvJ6LZVJSsDv6ntad3gXAESCKvb7t
            """
        )