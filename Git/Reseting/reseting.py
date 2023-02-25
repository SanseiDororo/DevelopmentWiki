import streamlit as st

def reseting():
    st.header('Reseting')
    st.write("")
    st.write('''
            
            Git allows to discard unwanted changes. This is performed with the git reset command
            which takes three arguments:

            * Hard
            * Mixed (default)
            * Soft

            Reseting specific number of commits is performed with the command:

                    git reset HEAD~5

            ''')
            
    st.write('''''')
    st.write('''''')

    with st.expander('Hard'):
        st.write('''

            Hard reset:

            * discards commit
            * discards changes in the staging area
            * discards changes in the working directory

                    git reset --hard <sha_hash_of_the_commit>
            

            ''')

    with st.expander('Mixed'):
        st.write('''

            Mixed reset discards:

            * discards commit
            * discards changes in the staging area
            * keeps changes in the working directory

                    git reset --mixed <sha_hash_of_the_commit>

            ''')

    with st.expander('Soft'):
        st.write('''

            Hard reset discards:

            * discards commit
            * keeps changes in the staging area
            * keeps changes in the working directory

                    git reset --soft <sha_hash_of_the_commit>

            ''')

    


   


    

   

        
        
