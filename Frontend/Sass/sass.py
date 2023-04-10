import streamlit as st

def sass():
    st.header('Sass')
    st.write("")
    st.write('''
            
        Sass (short for "Syntactically Awesome Style Sheets") is a CSS preprocessor 
        that allows developers to write more efficient and maintainable CSS code. 
        It extends the functionality of CSS by providing features such as variables, 
        nested rules, mixins, and functions.t.


            ''')

    st.write(''' ''')
    st.write(''' ''')
    with st.expander("7 - Architecture"):
        st.write('''

        The "7-1" Sass structure is a file architecture system for organizing Sass code. 
        It's called "7-1" because it involves dividing your stylesheets into seven different folders 
        and one main file:

        * base/: contains styles for basic HTML elements, such as headings, paragraphs, and links.
        * components/: contains styles for individual UI components, such as buttons, forms, and navigation menus.
        * layout/: contains styles for the overall layout of the site, such as grids and positioning.
        * pages/: contains styles specific to individual pages, such as page-level styles for a home page, contact page, or product page.
        * themes/: contains styles specific to different themes, such as light and dark themes.
        * utils/: contains utility classes and mixins that can be reused throughout the project.
        * vendors/: contains styles from third-party libraries and frameworks.
        * The eighth file is the main file, which imports all the partials in the correct order.

        This structure can help make your code more modular, organized, and easier to maintain, especially in larger projects.


        ''')

    

   

        
        
