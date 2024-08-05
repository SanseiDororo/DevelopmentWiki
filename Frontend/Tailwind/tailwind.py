import streamlit as st

def tailwind():
    st.header('Styling with Tailwind')
    st.write("")
    st.write('''
            Tailwind provides simple utility classes which make styling smoother.
            Many contemporary libraries are based on the Tailwind.
            ''')
    st.write(''' ''')
    st.write(''' ''')
    
    with st.expander("Globals"):
        st.write(
            '''
                Main styling declarations are stored in the globals.css file.

                We have 3 main layers in tailwind:

                * Base
                * Components
                * Utilities
                --------

                Base layer allows us to target any html class. In Components layer, we can
                define styles for specific components. In utilities layer we can create 
                utility classes.

                ```
                #Applying style to more html elements:

                h1,h2,h3,h4,h5,h6 {
                  @apply font-bold;
                }

                Applying style to a single element:

                h1 {
                    font-size:2.5 rem
                }
                ```
                --------

            '''
            )
   

          
          
