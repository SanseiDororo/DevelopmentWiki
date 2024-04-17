import streamlit as st

def administration():
    st.header('Linux Administration')
    st.write("")
    st.write('''
            
        This section covers most importan aspects of Linux Administration. The content is divided into
        topics such as properties, steps, examples. Detailed explanation of each topic is 
        provided in the extensions below. 


            ''')
    
    st.write(''' ''')
    st.write(''' ''')

    with st.expander('Create & Manage Users'):
        st.write(
            '''
               Linux is the most comprehensive os. There is almost infinte list of operations for
               performing basic and advanced operations. The following section lists most common
               operation we need to know in order to be able to start using linux. Linux is multiuser 
               system. Administrator is super user. If we want to perform the operations as administrators,
               we need to use keyword SUDO

               * ADDING USERS
                
                ```
                    sudo adduser username
                ```
                -------------------------
               * SWITCHING USERS

                ```
                    #Switching user
                    su username

                    #Executing command as a different user
                    sudo -u username command
                ```
                -------------------------
               * CHANGING PASSWORDS

                ```
                    #Change password
                    passwd

                    #Change password for a different user
                    sudo passwd username
                ```
                -------------------------

                * CREATING GROUPS

                ```
                    sudo groupadd groupname
                ```
                -------------------------
                PUTTING USERS IN A GROUP

                ```
                    sudo usermod -a -G groupname username
                ```
            '''
            )

    with st.expander('Folders & Files'):
        st.write(
            '''
                * CREATE FILE
                
                ```
                    touch filename
                ```
                -------------------------
                * CREATE FOLDER
                
                ```
                    mkdir folder name
                ```
                -------------------------
                * LIST FILES & FOLDERS

                ```
                    ls -al (alias can be ll)

                * LIST CONTENT OF A FILE

                ```
                    cat filename
                ```
                -------------------------
            '''
            )
        
    