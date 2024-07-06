import streamlit as st

def containers():
    st.header('Containers')
    st.write("")
    st.write('''
            
        A container is a lightweight, portable, and consistent environment for running applications.

        It has several key characteristics, which help to efficiently create, execute and ship 
        software:

        * **Isolation** : 
            Containers encapsulate an application and its dependencies, 
            isolating them from the host system and other containers. 
            This ensures that the application runs consistently regardless of 
            where it is deployed 
        * **Lightweight**: 
            Containers share the host system's kernel, making them more lightweight and 
            efficient compared to virtual machines (VMs). 
            They typically start up faster and use fewer resources.
        * **Portability**
            Containers can run on any system that supports the container runtime (e.g., Docker). 
            This portability ensures that applications can move seamlessly
             across different environments (development, testing, production).
        * **Scalability**
            Containers can be easily scaled up or down to handle varying loads. 
            Orchestrators like Kubernetes can manage container scaling, load balancing, and self-healing.


            ''')
    
    st.write(''' ''')
    st.write(''' ''')

    with st.expander('Docker'):
        st.write(
            '''
            '''
        )